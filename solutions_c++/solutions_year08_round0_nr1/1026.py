#include<stdio.h>
#include<map>
#include<string>
using namespace std;
const int oo=0X10101010;
map<string,int> my;
int z[1000+16][100+16];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int c,i,j,x,n,m,g,ans,o;
	char str[128];
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		my.clear();
		scanf("%d",&n);
		gets(str);
		g=1;
		while(n--)
		{
			gets(str);
			my[str]=g++;
		}
		memset(z,0X10,sizeof(z));
		for(i=1;i<g;i++)
			z[0][i]=0;
		scanf("%d",&m);
		gets(str);
		for(i=1;i<=m;i++)
		{
			gets(str);
			x=my[str];
			for(j=1;j<g;j++)
				if(j!=x)
				{
					if(z[i-1][j]<z[i][j])
						z[i][j]=z[i-1][j];
					if(z[i-1][x]+1<z[i][j])
						z[i][j]=z[i-1][x]+1;
				}
		}
		ans=oo;
		for(i=1;i<g;i++)
			if(z[m][i]<ans)
				ans=z[m][i];
		printf("Case #%d: %d\n",o,ans);
	}
	return 0;
}
