#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int dr[] = {-1,0,1,-1,1,-1,0,1};
int dc[] = {1,1,1,0,0,-1,-1,-1};

bool inbounds(int r, int c, int R, int C)
{
	return (r<R&&c<C&&r>=0&&c>=0);
}

int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	int T, N, K;
	char orig_board[55][55], rot_board[55][55];
	int h[55];
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		fin>>N>>K;
		for(int i=0;i<N;i++)
		{
			string tmp;
			fin>>tmp;
			for(int j=0;j<N;j++)
			{
				orig_board[i][j] = tmp[j];
				rot_board[i][j] = '.';
			}
			h[i] = N-1;
		}
		for(int i=N-1;i>=0;i--)	for(int j=N-1;j>=0;j--)	if(orig_board[i][j] != '.')
		{
			rot_board[h[N-1-i]][N-1-i] = orig_board[i][j];
			h[N-1-i] --;
		}
		bool red = false, blue = false;
		
		for(int i=0;i<N;i++)	for(int j=0;j<N;j++)
		{
			if(rot_board[i][j] == 'R' && !red)
			{
				for(int dir=0;dir<8;dir++)
				{
					int nr = i, nc = j, num=0;
					while(inbounds(nr,nc,N,N) && rot_board[nr][nc]=='R')
					{
						num++;
						nr += dr[dir];
						nc += dc[dir];
					}
					if(num >= K)	red = true;
				}
			}
			if(rot_board[i][j] == 'B' && !blue)
			{
				for(int dir=0;dir<8;dir++)
				{
					int nr = i, nc = j, num=0;
					while(inbounds(nr,nc,N,N) && rot_board[nr][nc]=='B')
					{
						num++;
						nr += dr[dir];
						nc += dc[dir];
					}
					if(num >= K)	blue = true;
				}
			}
		}
		
		fout<<"Case #"<<t<<": ";
		
		if(red && blue)
		{
			fout<<"Both";
		}
		else if(red)
		{
			fout<<"Red";
		}
		else if(blue)
		{
			fout<<"Blue";
		}
		else
		{
			fout<<"Neither";
		}
		fout<<"\n";
	}
	
	return 0;
}