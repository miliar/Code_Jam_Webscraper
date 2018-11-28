// initializing C++
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

// declaring function prototypes
int get_variables(ifstream &iFile, int &C_size, int &D_size, int &N_size, vector<string> &combine, vector<string> &destroy, string &n_invocation);
string calculate_result(int &C_size, int &D_size, int &N_size, vector<string> &combine, vector<string> &destroy, string &n_invocation);
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
		vector<string> combine;
		vector<string> destroy;
		string n_invocation;
		int C_size, D_size, N_size;
		get_variables(iFile,  C_size, D_size, N_size, combine, destroy, n_invocation);

		string result;
		result = calculate_result(C_size, D_size, N_size, combine, destroy, n_invocation);


		//unsigned __int64 result;
		//vector<int> boards_size;
		//vector<int> boards_count;

		//cout << "Case #" << i+1 << ": " << result << endl;
		oFile << "Case #" << i+1 << ": " << result << endl;
	}

	//cin.ignore( 80, '\n' );
	return 0;
}

string calculate_result(int &C_size, int &D_size, int &N_size, vector<string> &combine, vector<string> &destroy, string &n_invocation)
{
	string result;
	
	int merged_this=0, merged_last=0, cleared_last=0;
	int found=0;
	for( int i=1; i < N_size; i++ )
	{

		if( merged_last!=1 && cleared_last!=1)
		{		
			for( int k =0; k < C_size; k++ )
			{
				char debug1=n_invocation[i];
				found = combine[k].find_first_of(n_invocation[i]);
				
				if(found == 0 || found == 1)
				{
					found = (found+1)%2;

					found = combine[k][found] == n_invocation[i-1];
					if( found )
					{
						result.push_back(combine[k][2]);
						merged_this=1;
						break;
					}
				}
			}
		}

		if( merged_this != 1 && cleared_last != 1 && merged_last!=1)
			result.push_back(n_invocation[i-1]);
		else
		{
			if ( merged_this == 1)
				merged_last=1;
			else
				merged_last=0;
		}

		if(cleared_last==1 || merged_this==1)
		{
			merged_this=0;
			cleared_last=0;
			continue;
		}
		
		
		for( int k=0; k < D_size; k++ )
		{
			found = destroy[k].find_first_of(n_invocation[i]);
			if(found == 0 || found == 1)
			{
				found = (found+1)%2;

				found = result.find_first_of(destroy[k][found]);;
				if( found != -1 )
				{
					result.clear();//CLEAR
					cleared_last=1;
					break;
				}
			}
		}
	}

	if( merged_last != 1 && cleared_last != 1)
		result.push_back(n_invocation[N_size-1]);

	string result_string="[";
	for(int i=0; i< result.length(); i++)
	{
		if(i!=0)
		{
			result_string.push_back(',');
			result_string.push_back(' ');
		}
		result_string.push_back(result[i]);
	}
	result_string.push_back(']');
	return result_string;
}

int get_variables(ifstream &iFile, int &C_size, int &D_size, int &N_size, vector<string> &combine, vector<string> &destroy, string &n_invocation)
{
	iFile >> C_size;
	for( int k =0; k < C_size; k++ )
	{
		string temp;
		iFile >> temp;
		combine.push_back(temp);
		//cout << "C_size: " << C_size << " - ";
		//cout << temp << endl;
	}

	iFile >> D_size;
	for( int k =0; k < D_size; k++ )
	{
		string temp;
		iFile >> temp;
		destroy.push_back(temp);
//		cout << "D_size: " << D_size << " - ";
//		cout << temp << endl;
	}

	iFile >> N_size;
	iFile >> n_invocation;
	//cout << "N_size: " << N_size << " - ";
	//cout << n_invocation << endl << endl;

	return 0;
}




