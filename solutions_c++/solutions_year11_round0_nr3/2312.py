// initializing C++
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

// declaring function prototypes
int get_variables(ifstream &iFile, int &N_candy, vector<unsigned long int> &candy);
string calculate_result( int &N_candy, vector<unsigned long int> &candy);
//int find_biggest(vector<vector<short int>> &full_board, unsigned int &i_start, unsigned int &j_start, int N_biggest);


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
		vector<unsigned long int> candy;
		int N_candy;

		get_variables(iFile,  N_candy, candy);

		string result;
		result = calculate_result(N_candy, candy);


		//unsigned __int64 result;
		//vector<int> boards_size;
		//vector<int> boards_count;

		cout << "Case #" << i+1 << ": " << result << endl;
		//oFile << "Case #" << i+1 << ": " << result << endl;
	}

	//cin.ignore( 80, '\n' );
	return 0;
}

string calculate_result( int &N_candy, vector<unsigned long int> &candy)
{
	string result_string = "NO";

	unsigned long int result=0;
	for( int i = 0; i<N_candy; i++)
	{
		result ^= candy[i];
	}

	if( result == 0 )
	{
		unsigned long int smallest = candy[0];
		for( int i = 0; i<N_candy; i++)
		{
			if ( smallest > candy[i] )
				smallest = candy[i];
		}

		for( int i = 0; i<N_candy; i++)
		{
			result += candy[i];
		}
		result -= smallest;

		std::ostringstream string_small;
		string_small << result;
		result_string = string_small.str();
	}

	return result_string;
}

int get_variables(ifstream &iFile, int &N_candy, vector<unsigned long int> &candy)
{
	iFile >> N_candy;
	for( int k =0; k < N_candy; k++ )
	{
		unsigned long int temp;
		iFile >> temp;
		candy.push_back(temp);
		//cout << "N_candy: " << N_candy << " - ";
		//cout << temp << endl;
	}

	return 0;
}

