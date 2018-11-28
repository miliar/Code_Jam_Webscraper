#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <fstream>
#include <istream>

using namespace std;


int main(int argc,char* argv[])
{
	ifstream infile;
        infile.open(argv[1]);
	string cases;
	getline(infile,cases);
	int count = atoi(cases.c_str());
	
		
	for(int i=0;i<count;i++) //loop for number of test cases
	{
		bool empty=false;
		int matrix[4][4];
		int x_count = 0;
		int o_count = 0;
		for(int j = 0; j < 4; j++) //4 lines per case
		{
			string line;
                	getline(infile,line);
			for(int k=0;k<4;k++)  
			{
				if(line[k]=='X')
				{
					matrix[j][k]=1;
					x_count++;
				}
				else if(line[k]=='O')
				{
					matrix[j][k]=2;
					o_count++;
				}
				else if(line[k]=='.')
				{	
					empty = true;
					matrix[j][k]=0;
				}
				else if(line[k]=='T')
				{
					matrix[j][k]=10;
				}
				
			}
		}

		bool found_winner = false;
		char winner;

		//compute rows
		for(int row=0;row<4;row++)
		{
			int row_sum = 0;
			int any_empty = false;
			for(int col=0;col<4;col++)
			{
				if(matrix[row][col]==0) 
				{
					any_empty=true;
					break;
				}
				row_sum += matrix[row][col];
			}
			if( (row_sum==4 || row_sum==13) && !any_empty )
			{
				found_winner=true;
				winner = 'X';
				break;
			}
			else if( (row_sum==8 || row_sum==16) && !any_empty )
			{
				found_winner=true;
				winner = 'O';
                                break;
			}
		}
		
		//compute columns
		if(!found_winner)
		{
			for(int col=0;col<4;col++)
			{
				int col_sum = 0;
				bool any_empty = false;
				for(int row=0;row<4;row++)
				{
					if(matrix[row][col]==0)
					{
						any_empty=true;
						break;
					}
					col_sum += matrix[row][col];
				}

				if( (col_sum==4 || col_sum==13) & !any_empty)
                        	{
                                	found_winner=true;
					winner = 'X';
                                	break;
                        	}
				else if( (col_sum==8 || col_sum==16) & !any_empty)
				{
					found_winner = true;
					winner = 'O';
					break;
				}
			}

		}

		//compute left diagonal
		if(!found_winner)
		{
			bool any_empty = false;
			if(matrix[0][0]==0 || matrix[1][1]==0 || matrix[2][2]==0 || matrix[3][3]==0) any_empty=true;
			int leftdiagonal = matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3];
			if( (leftdiagonal==4 || leftdiagonal==13) && !any_empty)
                        {
                        	found_winner=true;
                                winner = 'X';
                        }
                        else if( (leftdiagonal==8 || leftdiagonal==16) && !any_empty)
                        {
                                found_winner = true;
                                winner = 'O';
                        }
		}

		//compute right  diagonal
                if(!found_winner)
                {
			bool any_empty = false;
			if(matrix[0][3]==0 || matrix[1][2]==0 || matrix[2][1]==0 || matrix[3][0]==0) any_empty=true;
                        int rightdiagonal = matrix[0][3]+matrix[1][2]+matrix[2][1]+matrix[3][0];
                        if((rightdiagonal==4 || rightdiagonal==13) && !any_empty)
                        {
                                found_winner=true;
                                winner = 'X';
                        }
                        else if((rightdiagonal==8 || rightdiagonal==16) && !any_empty)
                        {
                                found_winner = true;
                                winner = 'O';
                        }
                }

		if(found_winner)
		{
			cout<<"Case #"<<i+1<<": "<<winner<<" won"<<endl;
		}
		else if(!empty)
		{
			cout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
		}

		string line;
		getline(infile,line);
	}
}
