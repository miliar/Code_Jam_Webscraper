#include <fstream>
using namespace std;

#define maxn 107
ifstream fin("problem.in"); ofstream fout("problem.out");

int Dp[maxn][maxn];
//0 = normal 1 = special
int val[2][maxn];
int N,S,P,T;

inline int max(int a, int b){ return (a > b) ? a : b; }

int dinamica()
{
	Dp[1][0] = (val[0][1] >= P)?1: 0;
	Dp[1][1] = (val[1][1] >= P)?1: 0;
	int i,j,x,y;
	for(i = 2; i <= N; i++)
	{
		x = (val[0][i] >= P)?1:0;
		y = (val[1][i] >= P)?1:0;
		Dp[i][0] = Dp[i - 1][0] + x;
		for(j = 1; j <= i; j++)
			Dp[i][j] = max(Dp[i - 1][j - 1] + y,Dp[i - 1][j] + x);
	}
	return Dp[N][S];
}

int main()
{
	int i,j,k,x;
	fin>>T;
	for(i = 1; i <= T; i++)
	{
		fout<<"Case #"<<i<<": ";
		fin>>N>>S>>P;
		for(j = 1; j <= N; j++)
		{
			fin>>x;
			switch(x % 3)
			{
				case 0: val[0][j] = x/3; val[1][j] = x/3 + 1; break;
				case 1: val[0][j] = x/3 + 1; val[1][j] = x/3 + 1; break;
				case 2: val[0][j] = x/3 + 1; val[1][j] = x/3 + 2; break;
			}
			if(x == 0) val[0][j] = val[1][j] = 0;
		}
		fout<<dinamica()<<'\n';
		
	}
}