// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

#define pb(x) push_back(x)

#define mp(x, y) make_pair(x, y)

//string split given string a and delimiters
vs strsp(string a, string delim=" ")
{

  vs ret;
  string cr = "";
  for(int i = 0; i < a.size(); i++)
  {
    if(delim.find(a[i])==string::npos) cr += a[i];
    else { if(cr.size()) ret.push_back(cr); cr = ""; }
  }
  if(cr.size()) ret.push_back(cr);
  return ret;
}
int N,K;
int board[55][55];
void pboard()
{
	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < N; j++)
		{
			if(board[i][j] == 0) cout << ".";
			else if(board[i][j] == 1) cout << 'R';
			else cout << 'B';
		}
		cout << endl;
	}
	cout << endl;
}
void rotate()
{
	int nboard[55][55];
	for(int y = 0; y < N; y++)
	{
		for(int x = 0; x < N; x++)
		{
			nboard[x][N-1-y] = board[y][x];
		}
	}
	for(int c = 0; c < N; c++)
	{
		int steps = 0;
		for(int k = N-1; k >= 0; k--)
		{
			if(nboard[k][c] != 0)
			{
				nboard[N-1-steps][c] = nboard[k][c];
				steps++;
			}
		}
		for(int i = steps; i < N; i++) nboard[N-1-i][c] = 0;
	}
	memcpy(board,nboard,sizeof(board));
}


inline int INB(int y, int x)
{
	if(y < 0 || x < 0) return 0;
	if(y >= N || x >= N) return 0;
	else return 1;
}

int main()
{
	int T;
	cin >> T;
	for(int tcase = 1; tcase <= T; tcase++)
	{
		cin >> N >> K;
		string row = "";
		for(int i = 0; i < N; i++)
		{
			row = "";
			cin >> row;
			for(int j = 0; j < N; j++)
			{
				if(row[j] == '.') board[i][j] = 0;
				else if(row[j] == 'R') board[i][j] = 1;
				else board[i][j] = 100;
			}
		}
		rotate();
		int red = 0, blue = 0;
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < N; j++)
			{
				int type[4];
				memset(type,0,sizeof(type));
				for(int d = 0; d < K; d++)
				{
					if(INB(i+d,j)) type[0] += board[i+d][j];
					if(INB(i,j+d)) type[1] += board[i][j+d];
					if(INB(i+d,j+d)) type[2] += board[i+d][j+d];
					if(INB(i+d,j-d)) type[3] += board[i+d][j-d];
				}
				for(int k = 0; k < 4; k++)
				{
					if(type[k] == K) red = 1;
					if(type[k] == K*100) blue = 1;
				}
			}
		}
		cout << "Case #" << tcase << ": ";
		if(red && blue) cout << "Both\n";
		if(!red && blue) cout << "Blue\n";
		if(red && !blue) cout << "Red\n";
		if(!red && !blue) cout << "Neither\n";
	}
	return 0;
}
