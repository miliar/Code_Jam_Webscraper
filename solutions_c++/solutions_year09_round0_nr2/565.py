#define ONLINE_JUDGE
//#define GenerateTest

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <cmath>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <string>
#include <stack>
#include <list>
#include <sstream>
#include <hash_set>
#include <hash_map>

//#include "BigInteger\cbignum.h"

using namespace std;
#pragma comment(linker, "/STACK:64777216")

typedef long long LL;
const int size = 128;
int gr[size][size];
char res[size][size];
int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};
int h,w;
		
char dfs(int i,int j,char &ch)
{
	if(res[i][j]) return res[i][j];
	int r = 1000000000;
	int indi = -1;
	int indj = -1;
	for(int k = 0;k < 4;++k)
	{
		int li = i + di[k];
		int lj = j + dj[k];
		if(li >= 0 && li < h && lj >= 0 && lj < w)
		{
			if(gr[li][lj] < gr[i][j] && r > gr[li][lj])
			{
				r = gr[li][lj];
				indi = li;
				indj = lj;
			}
		}
	}
	if(indi != -1)
		res[i][j] = dfs(indi,indj,ch);
	else
		res[i][j] = ch++;
	return res[i][j];
}
void Solve()
{
	int T;
	cin >> T;
	for(int t = 0;t < T;++t)
	{
		cin >> h >> w;
		for(int i = 0;i < h;++i)
			for(int j = 0;j < w;++j)
				cin >> gr[i][j];
		memset(res,0,sizeof(res));
		char ch = 'a';
		for(int i = 0;i < h;++i)
			for(int j = 0;j < w;++j)
				dfs(i,j,ch);
		cout << "Case #" << t + 1 << ":" << endl;
		for(int i = 0;i < h;++i)
		{
			cout << res[i][0];
			for(int j = 1;j < w;++j)
				cout << " " << res[i][j];
			cout << endl;
		}
	}
}

int main()
{
#ifdef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);

	freopen("output.txt", "wt", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
//	freopen("output.txt", "wt", stdout);
	
#ifdef GenerateTest
	
	freopen("output.txt", "wt", stdout);

#endif

	clock_t start = clock();
#endif

	Solve();	

#ifndef ONLINE_JUDGE 
	clock_t end = clock();
	cout <<"\n\nTime: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
#endif
	return 0;
}