#include<iostream>
#include<sstream>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

#define pb								push_back
#define s(n)							scanf("%d",&n)
#define sl(n) 							scanf("%lld",&n)
#define sf(n) 							scanf("%lf",&n)
#define fill(a,v) 						memset(a, v, sizeof a)
#define INF								(int)1e9
#define EPS								1e-9

typedef long long LL;
typedef pair<int, int > PII;

int testCases, testNum;
// here follow the sovle, input & main

void solve()
{

}

bool input()
{
	int N;
	s(N);
	int sum = 0, axor = 0, least = 1 << 30;
	
	for(int i = 1; i <= N; i++)
	{
		 int a; s(a);
		 axor ^= a;
		 sum += a;
		 least = min( least, a);
	}
	if(axor == 0)
	 printf("Case #%d: %d\n", testNum,sum-least);
	else
	  printf("Case #%d: NO\n", testNum);
	return true;
}

int main()
{
	s(testCases);
	for(testNum = 1; testNum <= testCases; testNum ++)
	{
		if(!input()) break;
		solve();
	}
}
