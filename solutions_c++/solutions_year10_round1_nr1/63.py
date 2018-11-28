#include<iostream>

#include<fstream>


using namespace std;

ifstream in("A.in");
ofstream out("A.out");

int N,K;

char board[80][80];
char b2[80][80];

void rotate()
{
	for(int x=0;x<N;x++)
		for(int y=0;y<N;y++)
		{
			b2[y][N-1-x] = board[x][y];
		}
}
void drop()
{
	for(int y=0;y<N;y++)
	{
		int to=N-1;
		int from=N-1;
		for(;from>=0;from--)
		{
			if(b2[from][y]!='.')
			{
				char tmp = b2[from][y];
				b2[from][y]='.';
				b2[to--][y]=tmp;
			}
		}
	}
}

bool check(char target)
{
	int dir[4][2] = {{0,1},{1,0},{1,1},{1,-1}};
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
		{
			if(b2[i][j]==target)
			{
				for(int d=0;d<4;d++)
				{
					bool good = true;
					int pi=i;
					int pj=j;
					for(int t=1;t<=K-1;t++)
					{
						pi += dir[d][0];
						pj += dir[d][1];
						if(pi>=0 && pi<N && pj>=0 && pj<N &&b2[pi][pj]==target)
						{
							good = true;
						}
						else
						{
							good =false;
							break;
						}

					}
					if(good)
						return true;
				}

			}

		}
	return false;
}
int main()
{
	int T;
	in>>T;
	
	for(int c=0;c<T;c++)
	{
		in>>N>>K;
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
			{
				in>>board[i][j];
			}
		rotate();
		drop();
		bool r = check('R');
		bool b = check('B');
		out<<"Case #"<<c+1<<": ";
		if(r && b)
			out<<"Both\n";
		else if(r)
			out<<"Red\n";
		else if(b)
			out<<"Blue\n";
		else
			out<<"Neither\n";

	}
	return 0;
}