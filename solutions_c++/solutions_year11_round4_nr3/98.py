#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

#define FRsmall(x,y) freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);
#define FRlarge(x) freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);

typedef long long I;

int p[200];
int p2[200];

void factorization2(int n)
{
	int i;
	p[0]=0;
	for(i=2;i*i<=n;i++)
		if(n%i==0)
		{
			p[++p[0]]=i,p2[p[0]]=0;
			while(n%i==0)n/=i,p2[p[0]]++;
		}
		if(n>1)p[++p[0]]=n,p2[p[0]]=1;
}

int d[1000010];

int po[1000010];
int prime[1000010];


int prime_init(int n)
{
	int i,j,r=1;
	int n1=sqrt(n+0.5);
	memset(po,-1,sizeof(po));
	po[2]=0;prime[0]=2;
	for(i=3;i<=n;i+=2)
	{
		if(po[i])
		{
			po[i]=r;prime[r]=i;r++;
			if(i<=n1)for(j=i*i;j<=n;j+=i)po[j]=0;
		}
	}
	return r;
}

int main()
{
	//freopen("C.in","r",stdin);
	//FRsmall(C,0)
	FRlarge(C)
	int r=prime_init(1000000);

	int T,TC=0;
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d: ",TC);
		I N,k;
		I N1,i,mi=0,ma=1;
		scanf("%I64d",&N);
		if(N==1)
		{
			puts("0");
			continue;
		}
		memset(d,0,sizeof(d));
		N1=sqrt(N+0.5);
		
		for(i=0;i<r && prime[i]<=N1;i++)
		{
			k=N;
			while(k>=prime[i])
			{
				k/=prime[i];
				d[prime[i]]++;
			}
			mi++;
			ma+=d[prime[i]];
		}
		//printf("%I64d %I64d\n",mi,ma);
		printf("%I64d\n",ma-mi);
	}
	return 0;
}
