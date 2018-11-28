#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int cases;
	int tCase;
	fin>>cases;
	tCase = 1;
	while(cases--)
	{
		int N,K;
		fin>>N>>K;
		vector <vector<int>> board;
		board.resize(N);
		char temp;
		for(int i = 0; i < N; i++)
		{
			board[i].resize(N);
			for(int j = 0; j < N; j++)
			{
				fin>>temp;
				if(temp != '.')
				{
					board[i].push_back(temp);
					board[i].erase(board[i].begin());
				}
			}
		}
		int resR=0, resB=0;
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < N; j++)
			{
				if(!resR && board[i][j] == 'R')
				{
					int countd = 1, countr = 1, countl = 1, counth = 1;
					for(int k = i+1; k < N; k++)
					{
						if((countd > 0) && board[k][j] == 'R')
							countd++;
						else
							countd -= 100;
						if((countl > 0) && (j-countl >= 0) && board[k][j-countl] == 'R')
							countl++;
						else
							countl -= 100;
						if((countr > 0) && (j+countr < N) && board[k][j+countr] == 'R')
							countr++;
						else
							countr -= 100;
						if(countd == K || countr == K || countl == K)
						{
							resR = 1;
							break;
						}
					}
					for(int k = j+1; k < N; k++)
					{
						if((counth > 0) && board[i][k] == 'R')
							counth++;
						else
							counth -= 100;
						if(counth == K)
						{
							resR = 1;
							break;
						}
					}
				}	

				if(!resB && board[i][j] == 'B')
				{
					int countd = 1, countr = 1, countl = 1, counth = 1;
					for(int k = i+1; k < N; k++)
					{
						if((countd > 0) && board[k][j] == 'B')
							countd++;
						else
							countd -= 100;
						if((countl > 0) && (j-countl >= 0) && board[k][j-countl] == 'B')
							countl++;
						else
							countl -= 100;
						if((countr > 0) && (j+countr < N) && board[k][j+countr] == 'B')
							countr++;
						else
							countr -= 100;
						if(countd == K || countr == K || countl == K)
						{
							resB = 1;
							break;
						}
					}
					for(int k = j+1; k < N; k++)
					{
						if((counth > 0) && board[i][k] == 'B')
							counth++;
						else
							counth -= 100;
						if(counth == K)
						{
							resB = 1;
							break;
						}
					}
				}
			}
		}
		if(resR && resB)
		{
			fout<<"Case #"<<tCase++<<": Both"<<endl;
		}
		else if(resR)
		{
			fout<<"Case #"<<tCase++<<": Red"<<endl;
		}
		else if(resB)
		{
			fout<<"Case #"<<tCase++<<": Blue"<<endl;
		}
		else
		{
			fout<<"Case #"<<tCase++<<": Neither"<<endl;
		}


	}
	return 0;
}