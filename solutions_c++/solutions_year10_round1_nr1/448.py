#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream in("A.in");
ofstream out("A.txt");

int dx[4]={0,1,1,-1};
int dy[4]={1,1,0,1};

bool row(int x, int y, int count, int dir, vector<vector<char> > &M, int K, int N, char color)
{
	if (x>=0 && x<N && y>=0 && x<N)
	{
		if (M[x][y]==color)
		{
			count++;
			if (count == K)
				return true;
			if (row (x+dx[dir], y+dy[dir], count, dir, M, K, N, color))
				return true;
		}
		else
			return false;
		
	}
	return false;
}

int main()
{
	int T;
	in>>T;
	for (int t=1; t<=T; t++)
	{
		int N, K;
		in>>N>>K;
		
		vector<vector<char> > M(N, vector<char>(N));

		for (int y=N-1; y>=0; y--)
			for (int x=0; x<N; x++)
				in>>M[x][y];

		for (int y=0; y<N; y++)
			for (int x1=N-1; x1>0; x1--)
				if (M[x1][y]=='.')
					for (int x2=x1-1; x2>=0; x2--)
						if (M[x2][y]!='.')
						{
							M[x1][y]=M[x2][y];
							M[x2][y]='.';
							break;
						}

		bool blue=false, red=false;		
		for (int x=0; x<N; x++)
			if (!blue)
				for (int y=0; y<N; y++)
					for (int dir=0; dir<4; dir++)
						if (row(x,y,0,dir,M,K,N,'B'))
						{
							blue=true;
							break;
						}
					
		for (int x=0; x<N; x++)
			if (!red)
				for (int y=0; y<N; y++)
					for (int dir=0; dir<4; dir++)
						if (row(x,y,0,dir,M,K,N,'R'))
						{
							red=true;
							break;
						}

		out<<"Case #"<<t<<": ";
		if (blue && red)
			out<<"Both";
		else if (blue && !red)
			out<<"Blue";
		else if (!blue && red)
			out<<"Red";
		else
			out<<"Neither";
		out<<endl;
	}
    return 0;
}
