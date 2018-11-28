#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64

i64 caseno,cases,P,K,L,fr[1000000],val[1001];

void input()
{
	i64 i;

	scanf("%I64d %I64d %I64d",&P,&K,&L);
	for(i=0;i<L;i++) scanf("%I64d",&fr[i]);
	sort(fr,fr+L);
}

void process()
{
	i64 i,k;
	i64 res;

	CLR(val);
	k=res=0;
	for(i=L-1;i>=0;i--)
	{
		res+=fr[i]*(++val[k]);
		k=(k+1)%K;
	}
	printf("Case #%I64d: %I64d\n",++caseno,res);
}

int main()
{
	freopen("Inputs\\fk.txt","r",stdin);
	freopen("Inputs\\A2.txt","w",stdout);

	scanf("%I64d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}
