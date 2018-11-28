#include<algorithm>
#include<cstdio>
using namespace std;

const int mx=1010;

int n;
int a[mx];
int id[mx];

bool cmp(int p,int q)
{
	return a[p]<a[q];
}

int main()
{
	int t;
	int ca=0;
	int i;
	scanf("%d",&t);

	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			id[i]=i;
		}
		sort(id,id+n,cmp);
		double ans=0.0;
		for(i=0;i<n;i++)
		{
			if(id[i]!=i)
				ans+=1.0;
		}
		printf("Case #%d: %.12lf\n",++ca,ans);
	}

	return 0;
}
