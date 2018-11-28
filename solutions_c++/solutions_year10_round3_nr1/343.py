#include<iostream>
using namespace std;
class ty
{
public:
	int x,y;
};
ty zz[2000];
int checking(ty a,ty b)
{
	if(a.x>b.x)
	{
		ty tem;
		tem=a;
		a=b;
		b=tem;
	}
	if(b.y<a.y)
		return 1;
	return 0;
}
int cas;
int main()
{
	int cc=0,n;
	//freopen("C:\\ee.txt","r",stdin);
//	freopen("C:\\out.txt","w",stdout);
	scanf("%d",&cas);
	while(cas--)
	{
		cc++;
		scanf("%d",&n);
		int i,j,k;
		int ans=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d %d",&zz[i].x,&zz[i].y);
			for(j=i-1;j>=1;j--)
				ans+=checking(zz[i],zz[j]);
		}
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
