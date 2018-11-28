#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <iostream>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

int T,i,a,b,n,s,k,p;

int main()
{
//	freopen("2.in","r",stdin);
//	freopen("2.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		a = b  = 0;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&k);
			if(k>=3*p-2)
				a++; else
			if(k>=3*p-4 && (p!=1 || k>=1))
				b++;
		}
		printf("Case #%d: %d\n",t,a + min(b,s));
	}
	return 0;
}