#include <iostream>
using namespace std;
int calc(int l,int p,int c)
{
	int ans=0;
	int haha=p;
	while (haha>l)
	{
		ans++;
		if (haha%c==0)
		{
			haha=haha/c;
		}
		else haha=haha/c+1;		
	}
	return ans;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,i;
	int l,p,c;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d%d%d",&l,&p,&c);
		int tmp=calc(l,p,c);
	//	cout<<tmp<<endl;
		int ans=0;
		while (tmp>1)
		{
			if (tmp%2==1)
			{
				tmp++;
			}
			tmp=tmp/2;
			ans++;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;	
}
