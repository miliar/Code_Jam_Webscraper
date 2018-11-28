#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

struct node{
	int k,l;

	bool operator < (const node &a) const{
		return a.l<l;
	}
};

int main()
{
	int i,n,s,p,t,k,cas=0,ans;
	node f[105];

	//freopen("B-small-attempt2.in","r",stdin);
	//freopen("out.out","w",stdout);

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&k);
			f[i].k=k;
			if (k%3==0) f[i].l=k/3;
			else
				if ((k+1)%3==0) f[i].l=(k+1)/3;
				else f[i].l=(k+2)/3;
		}
		sort(f,f+n);
		ans=0;
		for(i=n-1;i>=0;i--)
			if (f[i].l>=p) ans++;
			else
				if (f[i].l>=1&&f[i].k>=2&&f[i].l==p-1&&s>0)
				{
					s--;
					ans++;
				}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}