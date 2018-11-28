#include <iostream>

using namespace std;

int i,a,b,t,c,d,u,k,j,m,n,z,xx,yy;
_int64 x,y;
int v[200][2];

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("1.out","w",stdout);
	t=0;
	cin>>z;
	while (z--)
	{
		t++;
		scanf("%d%d%d%d%d%d%d%d",&n,&a,&b,&c,&d,&xx,&yy,&m);

		x=xx;
		y=yy;
		v[0][0]=x;
		v[0][1]=y;
		for (i=1;i<n;i++)
		{
			x=x*a+b;
			x=x%m;
			y=y*c+d;
			y=y%m;
			v[i][0]=x;
			v[i][1]=y;
		}

		k=0;
		for (i=0;i<n;i++) for (u=i+1;u<n;u++)  for (j=u+1;j<n;j++) 
		{
			if ((v[i][0]+v[u][0]+v[j][0])%3==0&&(v[i][1]+v[u][1]+v[j][1])%3==0)
			{
				k++;
			}
		}
		printf("Case #%d: %d\n",t,k);
	}
	return 0;
}



