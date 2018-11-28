#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <set>
#include <list>
#include <queue>
#include <memory.h>
#include <stdio.h>
#include <time.h>
 
using namespace std;
 
#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int, int>
#define mp make_pair
#define PI 3.14159265358979
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned
int a[1010],b[1010];
int r,n,k;
long long count(int cnt, int pp)
{
	int c=0;
	if (cnt==0)
		return 0;
	long long res=0,p=pp,sum=0;
	while (1)
	{
		sum+=a[p];
		if (sum>k)
		{
			res+=sum-a[p];
			sum=0;
			++c;
			if (c==cnt)
				break;
		}
		else
			++p;
		if (p==n)
			p=0;
	}
	return res;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(it,0,t)
	{
		scanf("%d%d%d",&r,&k,&n);
		FOR(i,0,n)
			scanf("%d",&a[i]);
		long long s=0,res;
		FOR(i,0,n)
			s+=a[i];
		if (s<=k)
			res=s*1ll*r;
		else
		{
		MEMS(b,-1);
		b[0]=0;
		int p=0,sum=0,c,cnt=0,pp,u;
		while (1)
		{
			sum+=a[p];
			if (sum>k)
			{
				sum=0;
				cnt++;
				if (b[p]!=-1)
				{
					c=cnt;
					pp=cnt-b[p];
					u=p;
					break;
				}
				else
					b[p]=cnt;
				--p;
			}
			p++;
			if (p==n)
				p=0;
		}
		if (r<=c)
			res=count(r,0);
		else
		{
			res=count(c,0);
			r-=c;
			res+=(r/pp)*1ll*count(pp,u)+count(r%pp,u);
		}
		}
		printf("Case #%d: ",it+1);
		cout<<res<<endl;
	}
	return 0;
}