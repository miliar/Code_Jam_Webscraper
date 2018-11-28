#include<iostream>
#include<algorithm>
#include<string>
#include<map>
using namespace std;
struct W
{
	int a,b;
	bool operator<(W b)
	{
		return a<b.a;
	}
}d[1000];
int main()
{
	int T,cs,i,j,n,m,ans;
	string ss;
	freopen("A-Large.in","r",stdin);
	freopen("A-Large.out1","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d",&d[i].a,&d[i].b);
		std::sort(d,d+n);
		for(ans=i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				if(d[i].b>d[j].b)ans++;
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}