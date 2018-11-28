// initializing C++
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <deque>

using namespace std;

// declaring function prototypes
int get_variables(ifstream &iFile, int &n_snappers, int &k_fingers);
bool calculate_snap( int &n_snappers, int &k_fingers);

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
		int n_snappers=0, k_fingers=0;

		get_variables(iFile, n_snappers, k_fingers);
		//cout << "n_snappers: " << n_snappers << endl;
		//cout << "k_fingers: " << k_fingers << endl;

		bool result = 0;
		result = calculate_snap(n_snappers, k_fingers);

		if (result)
		{
			//cout << "Case #" << i+1 << ": ON" << endl;
			oFile << "Case #" << i+1 << ": ON" << endl;
		}	
		else
		{
			//cout << "Case #" << i+1 << ": OFF" << endl;
			oFile << "Case #" << i+1 << ": OFF" << endl;
		}
		
	}

	//cin.ignore( 80, '\n' );
	return 0;
}

bool calculate_snap( int &n_snappers, int &k_fingers)
{
	if(n_snappers > 26)
		return 0;
	for( int i = 0; i < (n_snappers); i++)
	{
		if (k_fingers % 2 == 0)
		{
			return 0;
		}
		k_fingers = k_fingers >> 1;
	}
	return 1;
}

int get_variables(ifstream &iFile, int &n_snappers, int &k_fingers)
{
	int temp_int;
	for(int i=0; i<2 && iFile >> temp_int ; i++)
	{
		switch(i)
		{
		case 0:
			n_snappers = temp_int;
			break;
		case 1:
			k_fingers = temp_int;
			break;
		}
	}
	return 0;
}

