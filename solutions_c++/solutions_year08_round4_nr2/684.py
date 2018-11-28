#include <cstdio>

using namespace std;

int n,m,a;

int os(int x1,int y1,int x2,int y2,int x3,int y3)
{
	int s=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2);
	if(s<0) s*=-1;
	return s;
}

void read(int ind)
{
	scanf("%d %d %d",&n,&m,&a);
	for(int i=0;i<=n;i++)
		for(int j=0;j<=m;j++)
			for(int k=0;k<=n;k++)
				for(int l=0;l<=m;l++)
					if(os(0,0,i,j,k,l)==a)
						{printf("Case #%d: 0 0 %d %d %d %d\n",ind,i,j,k,l);return;}
	printf("Case #%d: IMPOSSIBLE\n",ind);
	
}

int main()
{
	int nt;
	scanf("%d",&nt);
	for(int i=1;i<=nt;i++)
	{
		read(i);
	}
	return 0;
}
