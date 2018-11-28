#include <iostream>  /* Provide support for stand input and output such as cout*/
#include <fstream>  /* Provide support for file input and output*/
#include <algorithm>
#include <set>
#include <stack>
#include <iterator>
#include <stdlib.h>

using namespace std; /* Use stand name space*/

typedef struct streak
{
	int B_left;
	int B_up_left;
	int B_up;
	int B_up_right;
	int R_left;
	int R_up_left;
	int R_up;
	int R_up_right;

}  streak;
 
char* solve(char ** board, int N, int K)
{	
		streak **streak_matrix;
		streak_matrix = new streak*[N];

		bool Red = false;
		bool Blue = false;

			for(int j=0; j<N; j++)
			{
					streak_matrix[j] = new streak[N];
			}


			for(int j=0; j<N; j++)
			{
					for(int k=0; k<N; k++)
					{
						streak_matrix[j][k].B_left = 0;
					    streak_matrix[j][k].B_up = 0;
					    streak_matrix[j][k].B_up_left = 0;
					    streak_matrix[j][k].B_up_right = 0;
						streak_matrix[j][k].R_left = 0;
					    streak_matrix[j][k].R_up = 0;
					    streak_matrix[j][k].R_up_left = 0;
					    streak_matrix[j][k].R_up_right = 0;
					}
			}


			for(int j=0; j<N; j++)
			{
					for(int k=0; k<N; k++)
					{

						if(board[j][k] == 'B')
						{	
							if(k-1 >=0)
								streak_matrix[j][k].B_left = 1 +streak_matrix[j][k-1].B_left;
							else
								streak_matrix[j][k].B_left = 1;					

							if(k-1 >=0 && j-1 >=0)
								streak_matrix[j][k].B_up_left = 1 +streak_matrix[j-1][k-1].B_up_left;
							else
								streak_matrix[j][k].B_up_left = 1;		

							if( j-1 >=0)
								streak_matrix[j][k].B_up= 1 + streak_matrix[j-1][k].B_up;
							else
								streak_matrix[j][k].B_up = 1;		

							if(k+1 <N && j-1 >=0)
								streak_matrix[j][k].B_up_right = 1 + streak_matrix[j-1][k+1].B_up_right;
							else
								streak_matrix[j][k].B_up_right = 1;		
						}

						if(streak_matrix[j][k].B_left == K ||
							streak_matrix[j][k].B_up_left == K ||
							streak_matrix[j][k].B_up == K ||
							streak_matrix[j][k].B_up_right == K)
						{
							 Blue = true;
						}

						if(board[j][k] == 'R')
						{	
							if(k-1 >=0)
								streak_matrix[j][k].R_left = 1 +streak_matrix[j][k-1].R_left;
							else
								streak_matrix[j][k].R_left = 1;					

							if(k-1 >=0 && j-1 >=0)
								streak_matrix[j][k].R_up_left = 1 +streak_matrix[j-1][k-1].R_up_left;
							else
								streak_matrix[j][k].R_up_left = 1;		

							if( j-1 >=0)
								streak_matrix[j][k].R_up= 1 + streak_matrix[j-1][k].R_up;
							else
								streak_matrix[j][k].R_up = 1;		

							if(k+1 <N && j-1 >=0)
								streak_matrix[j][k].R_up_right = 1 + streak_matrix[j-1][k+1].R_up_right;
							else
								streak_matrix[j][k].R_up_right = 1;		
						}

						if(streak_matrix[j][k].R_left == K ||
							streak_matrix[j][k].R_up_left == K ||
							streak_matrix[j][k].R_up == K ||
							streak_matrix[j][k].R_up_right == K)
						{
							 Red = true;
						}

					}
			}
		
		if(!Blue && !Red)
		{
				return "Neither";
		}

		if(Blue && !Red)
		{
				return "Blue";
		}

		if(!Blue && Red)
		{
				return "Red";
		}

	     if(Blue && Red)
		{
				return "Both";
		}

}

char** rotate(char ** board, int N)
{
	char **rotated;
	int l, m;
	
    rotated = new char*[N];

			for(int j=0; j<N; j++)
			{
					rotated[j] = new char[N];
			}

			m = 0;

            for(int j=N-1; j>=0; j--)
			{

				 l = N-1;

				for(int k=N-1; k>=0; k--)
				{

					if(board[j][k] != '.')	
					{
							rotated[l][m] = board[j][k] ;
							l--;
					}
				}

				while(l>=0)
				{
					rotated[l][m] = '.';
					l--;
				}

				m++;
			}
	
	return rotated;

}

int main(int argc, char** args)
{
		char* result;
		int T; /* Number of test cases */
		int N; /* Number of lines */
		long K;
		char **board;
		char **rotated;

	 /* Initialize input and output file */ 
		fstream input_file("A-large.in", ios_base::in);
		fstream output_file("output.txt", ios_base::out);
		if(!input_file.is_open() || !output_file.is_open())
		{
				cout << "Unalbe to open file!" << endl;
				return 1;
		}
 
	/* Read the number of test cases*/
		input_file >> T;
		cout << "The number of test cases is " << T << endl;

   /* For each test case, load variables*/
		for(int i=0; i<T; i++)
		{
// cout << "Test case: " << i+1 << endl;

			input_file >> N;
			input_file >> K;
		
			board = new char*[N];

			for(int j=0; j<N; j++)
			{
					board[j] = new char[N];
			}

            for(int j=0; j<N; j++)
				for(int k=0; k<N; k++)
				{
					input_file >> board[j][k] ;
				}

// Display matrix

   //         for(int j=0; j<N; j++)
			//{
			//	for(int k=0; k<N; k++)
			//	{
			//		cout << board[j][k] << ' ';
			//	}
			//		cout << endl;
			//}


// cout << endl << "Number N, K is: " << N << ", "<< K<< endl <<endl;

//			cout << endl << "After Rotate "<<endl <<endl;

			rotated = rotate(board, N);

// Display matrix

   //         for(int j=0; j<N; j++)
			//{
			//	for(int k=0; k<N; k++)
			//	{
			//		cout << rotated[j][k] << ' ';
			//	}
			//		cout << endl;
			//}

			result = solve(rotated, N, K);

//			cout << " The result is: "  <<  result << endl;


			for(int j=0; j<N; j++)
			{
					delete board[j];
					delete rotated[j];
			}

			delete board;
			delete rotated;

cout << "Case #" << i +1<< ":	" << result << endl<<endl<<endl;
output_file << "Case #" << i+1 << ":	" << result << endl;
		}

}