// initializing C++
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <deque>
#include <stdlib.h>


using namespace std;

// declaring function prototypes
int get_variables(ifstream &iFile, int &no_of_events, deque<unsigned __int64> &t_events, unsigned __int64 &common_denominator);
unsigned __int64 calculate_time( int &no_of_events, deque<unsigned __int64> &t_events, unsigned __int64 &common_denominator);
unsigned __int64 GCD(unsigned __int64 x,unsigned __int64 y);

int main ()
{
	int no_test_cases;
	ifstream iFile("input.txt");        // input.txt has integers, one per line
	ofstream oFile("output.txt");

	//Acquire initial variables
	iFile >> no_test_cases ;
	//cout << "Number of test cases: " << no_test_cases << endl;

	for(int i=0; i<no_test_cases ; i++)
	{
		int no_of_events=0;
		deque<unsigned __int64> t_events;
		unsigned __int64 common_denominator = 0;

		get_variables(iFile, no_of_events, t_events, common_denominator);
		//cout << "n_snappers: " << no_of_events << endl;
		//cout << "common_denominator: " << common_denominator << endl;

		//for( int j = 0; j<no_of_events; j++)
		//	cout << "t_events[" << j << "]: " << t_events[j] << endl;

		unsigned __int64 result = 0;
		result = calculate_time(no_of_events, t_events, common_denominator);

		//cout << "Case #" << i+1 << ": " << result << endl;
		oFile << "Case #" << i+1 << ": " << result << endl;
	}

	//cin.ignore( 80, '\n' );
	return 0;
}

unsigned __int64 calculate_time( int &no_of_events, deque<unsigned __int64> &t_events, unsigned __int64 &common_denominator)
{
	unsigned __int64 result=0;
	unsigned __int64 temp;

	for( unsigned int i = 0; i < t_events.size(); i++)
	{
		temp = common_denominator - (t_events[i] % common_denominator);
		if (temp != common_denominator && temp>result)
			result = temp;
	}
	return result;
}

int get_variables(ifstream &iFile, int &no_of_events, deque<unsigned __int64> &t_events, unsigned __int64 &common_denominator)
{
	iFile >> no_of_events;
	unsigned __int64 temp_int;
	for(int i=0; i<no_of_events && iFile >> temp_int ; i++)
	{
		t_events.push_back(temp_int);

		if (i==0)
			continue;

		for(unsigned int j = 0; j < (t_events.size() - 1); j++)
		{
			unsigned __int64 difference = _abs64(t_events[j] - temp_int);
			if (common_denominator==0)
				common_denominator = difference;
			else
				common_denominator = GCD(common_denominator,difference);
		}
	}
	return 0;
}

unsigned __int64 GCD(unsigned __int64 x,unsigned __int64 y)
{
	if(y==0)  // base case, the programs stops if y reaches 0.
		return x;     //it returns the GCD
	else 
		return GCD(y,x%y); //if y doesn't reach 0 then recursion continues
}
