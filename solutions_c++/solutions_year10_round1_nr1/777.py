#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;

#define MAXN 110

int d[MAXN][MAXN];
int N, K;
int td[MAXN][MAXN];
void print(int t[MAXN][MAXN])
{
	int i, j, k;
	for(i = 0; i < N; i++)
	{
		for(j = 0; j < N; j++)
		{
			cout<<t[i][j];
		}
		cout<<endl;
	}
			cout<<endl;
}
void rotate()
{
	CLR(td);
	int i, j, k;
	for(i = 0; i < N; i++)
	{
		k = N-1;
		for(j = N-1; j >= 0; j--)
		{
			if(d[i][j] == 0)
			continue;
			td[k--][N-i-1] = d[i][j];
		}
	}
	CLR(d);
	for(i = 0; i < N; i++)
	{
		for(j = 0; j < N; j++)
		{
			d[i][j] = td[i][j];
		}
	}
	
}

int inrow(int val, int K)
{
	int i, j, k;
	for(i = 0; i < N; i++)
	{
		for(j = 0; j < N; j++)
		{
			int flag = 0;
			for(k = 0; k < K; k++)
			{
				if(k+j < N && d[i][k+j] == val)
					continue;
				break;
			}
			if(k == K)
				return 1;
			for(k = 0; k < K; k++)
			{
				if(i+k < N && d[i+k][j] == val)
					continue;
				break;
			}
			if(k == K)
				return 1;
			for(k = 0; k < K; k++)
			{
				if(j+k < N && i+k < N && d[i+k][j+k] == val)
					continue;
				break;
			}
			if(k == K)
				return 1;
			for(k = 0; k < K; k++)
			{
				if(j+k < N  && i-k >= 0 && d[i-k][j+k] == val)
					continue;
				break;
			}
			if(k == K)
				return 1;
		}
	}
	return 0;			
}
int check()
{
	int t1 = inrow(1, K);
	int t2 = inrow(2, K);
	if(t1 && t2)
		return 3;
	else if(t1)
		return 1;
	else if(t2)
		return 2;
	return 0;
}
int main()
{
	int tes;
	cin >> tes;
	int tesnum = 0;
	while(tes--)
	{
		tesnum++;
		cin >> N >> K;
		vector<string> v;
		CLR(d);
		int i, j, k;
		for(i = 0; i < N; i++)
		{
			string s;
			cin >> s;
			v.PB(s);
		}
		for(i = 0; i < N; i++)
		{
			for(j = 0; j < N; j++)
			{
				if(v[i][j] == 'B')
					d[i][j] = 1;
				else if(v[i][j] == 'R')
					d[i][j] = 2;
			}
		}
		//print(d);

		rotate();
		//print(d);
		int val = check();
		string op = "";
		if(val == 0)
		op = "Neither";
		else if(val == 1)
		op = "Blue";
		else if(val == 2)
		op = "Red";
		else 
		op = "Both";
		printf("Case #%d: %s\n", tesnum, op.c_str());
	}
	return 0;
}
			
