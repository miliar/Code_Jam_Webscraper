//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
using namespace std;

int t,n,x,sum,mini,c;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d",&n);
		x = 0;
		sum = 0;
		mini = 2000000000;
		FORN(j,n)
		{
			scanf("%d",&c);
			x ^= c;
			sum += c;
			mini = min(mini,c);
		}
		if (x)
			printf("Case #%d: NO\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,sum-mini);
	}
}
