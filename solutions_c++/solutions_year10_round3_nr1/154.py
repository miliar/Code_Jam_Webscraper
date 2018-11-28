#include<iostream>
#include<algorithm>
using namespace std;

#define MAXN 1001

int te,n,ans;

struct LINE
{
	int a,b;
};

bool cmp(LINE x,LINE y)
{
	return x.a<y.a;
}

LINE l[MAXN];

int main()
{
	freopen("Al.in","r",stdin);
	freopen("Al.txt","w",stdout);
	cin>>te;
	for(int ca=1;ca<=te;++ca)
	{
		cin>>n;
		for(int i=0;i<n;++i)
		{
			cin>>l[i].a>>l[i].b;
		}
		sort(l,l+n,cmp);
		ans=0;
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<i;++j)
			{
				if(l[j].b>l[i].b)
				{
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
