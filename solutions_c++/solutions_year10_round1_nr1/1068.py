// initializing C++
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

// declaring function prototypes
int get_variables(ifstream &iFile, unsigned int &n_by_n, unsigned int &k_in_a_row, vector<vector<char>> &rotated_board);
string calculate_result(unsigned int &n_by_n, unsigned int &k_in_a_row,  vector<vector<char>> &rotated_board);
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
		vector<vector<char>> rotated_board;
		unsigned int n_by_n = 0;
		unsigned int k_in_a_row = 0;
		get_variables(iFile, n_by_n, k_in_a_row, rotated_board);

		string result;
		result = calculate_result(n_by_n, k_in_a_row, rotated_board);

		//cout << "Case #" << i+1 << ": " << result << endl;
		oFile << "Case #" << i+1 << ": " << result << endl;
	}

	//cin.ignore( 80, '\n' );
	return 0;
}

string calculate_result(unsigned int &n_by_n, unsigned int &k_in_a_row,  vector<vector<char>> &rotated_board)
{
	string result;
	char temp_char;
	unsigned int row = 0;
	bool red = 0;
	bool blue = 0;

	//check vertical
	for( unsigned int i = 0; i < n_by_n; i++)
	{
		temp_char = '.';
		for( unsigned int j = 0; j < n_by_n; j++)
		{
			if (rotated_board[i].size() > j)
			{
				if( temp_char == rotated_board[i][j] )
				{
					row++;
					if(row>=k_in_a_row)
					{
						if(temp_char == 'B')
							blue=1;
						if(temp_char == 'R')
							red=1;
					}
				}
				else
				{
					temp_char = rotated_board[i][j];
					row=1;
					if( red && blue )
						return "Both";
					if(temp_char=='R' && red)
						continue;
					if(temp_char=='B' && blue)
						continue;
				}
			}
		}
	}

	//check horizontal
	for( unsigned int j = 0; j < n_by_n; j++)
	{
		temp_char = '.';
		for( unsigned int i = 0; i < n_by_n; i++)
		{
			if (rotated_board[i].size() > j)
			{
				if( temp_char == rotated_board[i][rotated_board[i].size()-j-1] )
				{
					row++;
					if(row>=k_in_a_row)
					{
						if(temp_char == 'B')
							blue=1;
						if(temp_char == 'R')
							red=1;
					}
				}
				else
				{
					temp_char = rotated_board[i][rotated_board[i].size()-j-1];
					row=1;
					if( red && blue )
						return "Both";
					if(temp_char=='R' && red)
						continue;
					if(temp_char=='B' && blue)
						continue;
				}
			}
		}
	}

	//check diagonal 1
	row = 0;
	for( unsigned int i = 0; i < n_by_n; i++)
	{
		for( unsigned int j = 0; j < n_by_n; j++)
		{
			if (rotated_board[i].size() > j)
			{

				temp_char = rotated_board[i][rotated_board[i].size()-j-1];
				if( red && blue )
					return "Both";
				if(temp_char=='R' && red)
					continue;
				if(temp_char=='B' && blue)
					continue;

				unsigned int temp_i = i;
				unsigned int temp_j = j;		
				do
				{
					temp_i++;
					temp_j++;
					row++;
					if(row>=k_in_a_row)
					{
						if(temp_char == 'B')
							blue=1;
						if(temp_char == 'R')
							red=1;
					}
					if( temp_i >= rotated_board.size() || temp_j >= rotated_board[temp_i].size() )
						break;
				}
				while(temp_char == rotated_board[temp_i][rotated_board[temp_i].size()-temp_j-1]);
				row = 0;

				temp_i = i;
				temp_j = j;		
				do
				{
					temp_i++; //proxima
					temp_j--;
					row++;
					if(row>=k_in_a_row)
					{
						if(temp_char == 'B')
							blue=1;
						if(temp_char == 'R')
							red=1;
					}
					if( temp_i >= rotated_board.size() || temp_j > 100 )
						break;
				}
				while(temp_char == rotated_board[temp_i][rotated_board[temp_i].size()-temp_j-1]);
				row = 0;
			}
		}
	}


	if( red && blue )
		return "Both";
	else if(red)
		return "Red";
	else if(blue)
		return "Blue";
	else
		return "Neither";
}

int get_variables(ifstream &iFile, unsigned int &n_by_n, unsigned int &k_in_a_row, vector<vector<char>> &rotated_board)
{
	iFile >> n_by_n;
	iFile >> k_in_a_row;
	char temp_char;
	for(unsigned int i=0; i<n_by_n; i++) //get board
	{
		vector<char> line;
		for(unsigned int j=0; j<n_by_n && iFile >> temp_char; j++) //get this line
		{
			if(temp_char == '.')
				continue;
			line.push_back(temp_char);
		}
		rotated_board.push_back(line);
	}
	return 0;
}
