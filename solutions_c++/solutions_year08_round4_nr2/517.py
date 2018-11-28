#include <iostream>

using namespace std;

int i,u,k,j,m,n,x,z,a,b,c,d,e,f,t,ans;
double dk,dj;

bool pig()
{
	for (a=0;a<=n;a++) for (b=0;b<=m;b++) for (c=0;c<=n;c++) for (d=0;d<=m;d++)
	{
		x=0;
		for (e=0;e<=n;e++) 
		{
			k=ans+d*e+b*c-a*d-b*e;
			dk=k;
			dj=c-a;
			if ((c-a)!=0&&k%(c-a)==0)
			{
				if (k/(c-a)>=0&&k/(c-a)<=m)
				{
					printf("%d %d %d %d %d %d",a,b,c,d,e,k/(c-a));
					printf("\n");
					return 0;
				}
			}
			if (dk/dj>m+1-10) break;
			
		}
	}
	return 1;
}

			
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	t=0;
	cin>>z;
	while (z--)
	{
		t++;
		scanf("%d%d%d",&n,&m,&ans);

		printf("Case #%d: ",t);
		if (pig()) printf("IMPOSSIBLE\n");
	}
	return 0;
}
		
