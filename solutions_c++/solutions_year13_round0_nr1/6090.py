#include <iostream>
#include <fstream>


using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

//ifstream fin("input.txt");
//ofstream fout("output.txt");


typedef struct 
{
	int o_sum;
	int x_sum;

}sum;

sum sum_data[6][6] = {0,};
int square[6][6] = {0,};
char c_square[6][6] = {0,};

int main()
{
	int T,t;
	int i,j;
	int ox_cnt,flag;
	


	char data;
	char result[10];

	fin >> T;

	for(t=1;t<=T;t++)
	{
		ox_cnt = flag = 0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				fin >> data;
				c_square[i][j] = data;

				if(data == 'X')
				{
					square[i][j] = 1;
					sum_data[i][5].x_sum += 1;
					sum_data[5][j].x_sum += 1;

					if(i == j)
					{
						sum_data[5][5].x_sum += 1;
						
					}
					else if( (5-i) == j)
					{
						sum_data[5][0].x_sum += 1;
					}

					ox_cnt++;
				}
				else if(data == 'O')
				{
					square[i][j] = -1;
					sum_data[i][5].o_sum += 1;
					sum_data[5][j].o_sum += 1;

					if(i == j)
					{
						sum_data[5][5].o_sum += 1;
						
					}
					else if( (5-i) == j)
					{
						sum_data[5][0].o_sum += 1;
					}

					ox_cnt++;
				}
				else if(data == 'T')
				{
					square[i][j] = 2;

					sum_data[i][5].o_sum += 1;
					sum_data[5][j].o_sum += 1;
					sum_data[i][5].x_sum += 1;
					sum_data[5][j].x_sum += 1;

					if(i == j)
					{
						sum_data[5][5].x_sum += 1;
						sum_data[5][5].o_sum += 1;
					}
					else if( (5-i) == j)
					{
						sum_data[5][0].x_sum += 1;
						sum_data[5][0].o_sum += 1;

					}
					ox_cnt++;
				}
				else
					square[i][j] = 0;
			}
		}

		for(i=0;i<6;i++)
		{
			if(sum_data[5][i].o_sum == 4)
			{
				fout << "Case #" << t << ": O won" << endl;
				flag = 1;
				break;
			}
			else if(sum_data[5][i].x_sum == 4)
			{
				fout << "Case #" << t << ": X won" << endl;
				flag = 1;
				break;
			}
			else if(sum_data[i][5].o_sum == 4)
			{
				fout << "Case #" << t << ": O won" << endl;
				flag = 1;
				break;
			}
			else if(sum_data[i][5].x_sum == 4)
			{
				fout << "Case #" << t << ": X won" << endl;
				flag = 1;
				break;
			}
		}

		if( flag != 1 && ox_cnt == 16)
			fout << "Case #" << t << ": Draw" << endl;
		else if(flag  != 1 && ox_cnt < 16)
			fout << "Case #" << t << ": Game has not completed" << endl;

	
		for(i=0;i<6;i++)
		{
			for(j=0;j<6;j++)
			{
				//cout << "<"<< sum_data[i][j].o_sum << ","<< sum_data[i][j].x_sum << ">";
				sum_data[i][j].o_sum = sum_data[i][j].x_sum =  0;
			}
			//cout << endl;
		}
		//cout << endl;
	
	}

	return 0;
}
