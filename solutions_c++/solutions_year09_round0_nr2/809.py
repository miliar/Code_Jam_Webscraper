#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)
#define FOR(i,s,e) for(int i = s; i < e; i++)
#define FORD(i,e,s) for(int i = e; i > s; i--)
#define ALL(x) x.begin(), x.end()
#define OUT(x) cout<<#x<<" = "<<x<<endl;
#define PB push_back
typedef long long ll;

int T[100][100];
char Output[100][100];

int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
int N, H, W;

bool CanFlowTo(int h1, int w1, int h2, int w2)
{
	int least = 1000000;
	REP(i,4)
	{
		int nh = h1+dy[i];
		int nw = w1+dx[i];
		if(!(nh>=0 && nh < H && nw >= 0 && nw < W))
			continue;
		else
			least = min(least, T[nh][nw]);
	}
	if(least>=T[h1][w1])
		return false;
	REP(i,4)
	{
		int nh = h1+dy[i];
		int nw = w1+dx[i];
		if(!(nh>=0 && nh < H && nw >= 0 && nw < W))
			continue;
		if(T[nh][nw] == least)
			return nh == h2 && nw == w2;
	}
	return false;
}

void FillWith(char letter, int h, int w)
{
	Output[h][w] = letter;
	int least = 1000000;
	REP(i,4)
	{
		int nh = h+dy[i];
		int nw = w+dx[i];
		if(!(nh>=0 && nh < H && nw >= 0 && nw < W))
			continue;
		else
			least = min(least, T[nh][nw]);
	}
	bool flowed = least >= T[h][w];
	REP(i,4)
	{
		int nh = h+dy[i];
		int nw = w+dx[i];
		if(!(nh>=0 && nh < H && nw >= 0 && nw < W) ||  T[nh][nw] == T[h][w])
			continue;
		if(Output[nh][nw] != 0 && T[nh][nw] == least)
			flowed = true;
		if(T[nh][nw] == least && flowed == false && T[nh][nw] < T[h][w])
		{
			FillWith(letter, nh, nw);
			flowed = true;
		}
		else if(T[nh][nw] > T[h][w] && CanFlowTo(nh, nw, h, w))
			FillWith(letter, nh, nw);
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin>>N;

	REP(tests, N)
	{
		cin>>H>>W;
		REP(i,H)
			REP(j,W)
			cin>>T[i][j];

		memset(Output,0,sizeof(Output));
		char literka = 'a';
		REP(i,H)
			REP(j,W)
			if(Output[i][j]==0)
				FillWith(literka++, i, j);

		cout<<"Case #"<<tests+1<<":"<<endl;
		REP(i,H)
		{
			REP(j,W-1)
				printf("%c ", Output[i][j]);
			printf("%c\n", Output[i][W-1]);
		}
	}

	return 0;
}

