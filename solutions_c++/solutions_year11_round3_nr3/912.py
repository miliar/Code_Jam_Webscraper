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

int t,n,l,h,ans;
bool ktmu;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d%d%d",&n,&l,&h);
		int bil[n];
		FORN(j,n)
			scanf("%d",&bil[j]);
		ktmu = false;
		FORS(j,l,h)
		{
			FORN(k,n)
			{
				if ((j%bil[k]) && (bil[k]%j))
					break;
				if (k == n-1)
				{
					ktmu = true;
					ans = j;
					break;
				}
			}
			if (ktmu)
				break;
		}
		if (ktmu)
			printf("Case #%d: %d\n",i+1,ans);
		else
			printf("Case #%d: NO\n",i+1);
	}
}
