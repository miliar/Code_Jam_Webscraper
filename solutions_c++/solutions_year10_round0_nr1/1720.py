/* Asyamov Igor
e-mail: igor9669@gmail.com*/

#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <cstdio>
#include <map>
#include <fstream>
#include <cstdlib>
#include <queue>
#include <bitset>
#include <set>
#include <stack>
#include <utility>
#include<cassert>
using namespace std;
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define PB push_back
#define A first
#define B second
#define Len(a) (int)a.length()
#define Sz(a) (int)a.size()
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI > VVI;
#define MAXN 11
const double Eps=1e-7;
const double Pi=2*acos(0.0);
const int inf=1000*1000*1000;

int main()
{
	//freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	freopen("input.in","r",stdin);freopen("output.out","w",stdout);
	int n,k;
	int t;
	scanf("%d",&t);
	LL dp[31];
	dp[0]=0;
	dp[1]=1;
	FR(i,2,31)dp[i]=2*dp[i-1]+1;
	FOR(cur,t)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",cur+1);
		if(k==0)
		{
			printf("OFF\n");
			continue;
		}
		if(n==1)
		{
			if(k&1)printf("ON\n");
			else printf("OFF\n");
		}
		else 
		{
			int off=k/(dp[n]+1);
			if(dp[n]*(off+1)+off==k)printf("ON\n");
			else printf("OFF\n");
		}
	}
	return 0;
}