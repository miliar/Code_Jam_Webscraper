#include <stdio.h>
#include <string.h>

#include <algorithm>
using namespace std;

#define maxn 1010
int n;
int a[maxn];
int tt[maxn];
int ans[maxn];

bool cmp(int a,int b)
{
	return a<b;
}

int solve()
{
	int l,c;
	long long t;
	scanf("%d%I64d%d%d",&l,&t,&n,&c);
	for(int i=0;i<c;++i)
		scanf("%d",&a[i]);
	int num =0;
	int sum = 0;
	for(int i =0;i<n;++i)
		tt[i] = a[i%c] + a[i%c];
	for(int i=0;i<n;++i)
	{
		sum += tt[i];
		if(tt[i] > t)
		{
			tt[i] -= t;
			a[num++] = tt[i];
			t = 0;
		}
		else
			t -= tt[i];
	}
	make_heap(a,a+num,cmp);
	for(int i = 0;i<l && num > 0;++i)
	{
		sum -= a[0]/2;
		pop_heap(a,a+n,cmp);
		num--;
	}
	return sum;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
		printf("Case #%d: %d\n",i+1,solve());
	return 0;
}
