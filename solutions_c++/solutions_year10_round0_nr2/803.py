#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
using namespace std;

long long nod(long long a, long long b)
{
	long long c;
	while (b>0)
	{
		c=a%b; a=b; b=c;
	}
	return a;
}

long long a[1010];
vector<long long> d;
int t,tt;
int i,n,j;
long long res;

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);

	scanf("%d",&tt);
	for (t=1; t<=tt; t++)
	{
		scanf("%d",&n);
		for (i=1; i<=n; i++)
			scanf("%I64d",&a[i]);
		d.clear();
		for (i=1; i<n; i++)
			for (j=i+1; j<=n; j++)
				d.push_back(abs(a[j]-a[i]));
		res=d[0];
		for (i=1; i<d.size(); i++)
			res=nod(res,d[i]);
		res=(res-(a[1]%res))%res;
		printf("Case #%d: %I64d\n",t,res);
	}

    return 0;
}
