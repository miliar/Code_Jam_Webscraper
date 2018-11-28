#include <iostream>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); ++i)
#define INF 32000
#define N(i,j) map[i-1][j]
#define W(i,j) map[i][j-1]
#define E(i,j) map[i][j+1]
#define S(i,j) map[i+1][j]

int T,H,W;
int map[102][102];
int code[102][102];
char trans[26];
int curCode=0;

int go(int i, int j)
{
	if (code[i][j]>=0) return code[i][j];
	int new_i=i,new_j=j;
	int current = map[i][j];
	int newLevel = current;
	if (N(i,j) < newLevel)
	{
		newLevel = N(i,j);
		new_i = i-1;
		new_j = j;
	}
	if (W(i,j) < newLevel)
	{
		newLevel = W(i,j);
		new_i = i;
		new_j = j-1;
	}
	if (E(i,j) < newLevel)
	{
		newLevel = E(i,j);
		new_i = i;
		new_j = j+1;
	}
	if (S(i,j) < newLevel)
	{
		newLevel = S(i,j);
		new_i = i+1;
		new_j = j;
	}
	//cout << "go(" << i << "," << j << ") current=" << current << " - newLevel=" << newLevel << " - new_i=" << new_i << " - new_j=" << new_j << endl;
	if (new_i == i && new_j == j) //sink
	{
		code[i][j]=curCode++;
	}
	else
	{
		code[i][j]=go(new_i, new_j);
	}
	//cout << "code[" << i << "][" << j << "]=" << code[i][j] << endl;
	return code[i][j];
}

int main()
{
	cin >> T;
	
	rep(t,T)
	{
		cin >> H >> W;
		
		rep(i,H+2)
		{
			map[i][0]=INF;
			map[i][W+1]=INF;
		}
		rep(j,W+2)
		{
			map[0][j]=INF;
			map[H+1][j]=INF;
		}
		rep(i,H)
		{
			rep(j,W)
			{
				cin >> map[i+1][j+1];
				code[i+1][j+1]=-1;
			}
		}
		
		rep(i,26) trans[i]='\0';
		curCode=0;
		
		rep(i,H)
		{
			rep(j,W)
			{
				code[i+1][j+1] = go(i+1,j+1);
			}
		}
		
		cout << "Case #" << (t+1) << ":" << endl;
		
		char c='a';
		rep(i,H)
		{
			rep(j,W)
			{
				if (j>0) cout << " ";
				if (trans[code[i+1][j+1]] == '\0')
				{
					trans[code[i+1][j+1]] = c++;
				}
				cout << trans[code[i+1][j+1]];
			}
			cout << endl;
		}
	}
}
