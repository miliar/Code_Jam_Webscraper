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
#define MAXN 510
int N, K, B, T;
int X[MAXN];
int V[MAXN];
int NX[MAXN];
int isreach[MAXN];
int solve()
{
	int i, j, k;
	int swaps = 0;
	CLR(NX);
	CLR(isreach);
	for(i = 0; i < N; i++)
	{
		LL finpos = (LL)X[i] + T*(LL)V[i];
		if(finpos >= B)
		isreach[i] = 1;
	}
	int count = 0;
	for(i = N-1; i >= 0; i--)
	{
		if(!isreach[i])continue;
		for(j = i+1; j < N; j++)
		{
			if(isreach[j] == 0)
			swaps++;
		}
		count++;
		if(count == K)
		break;
	}
	if(count < K)
		return -1;
	return swaps;
}
		
int main()
{
	int tes;
	int tesnum = 0;
	cin >>tes;
	while(tes--)
	{
		tesnum ++;
		int i, j, k;
		cin >> N >> K >> B >> T;
		for(i = 0; i < N; i++)
		{
			cin >> X[i];
		}
		for(i = 0; i < N; i++)
		{
			cin >> V[i];
		}
		int ans = solve();
		if(ans == -1)
		printf("Case #%d: IMPOSSIBLE\n", tesnum);
		else
		printf("Case #%d: %d\n", tesnum, ans);
		
	}
	return 0;
}
