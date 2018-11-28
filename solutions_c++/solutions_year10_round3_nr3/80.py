#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
char map[515][515];
bool p[515][515];
int a[515];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
    int i,j,k,l,m,n,t,c,num,aa,bb,sx,sy,ex,ey,f,s,mmm=1;
	scanf("%d",&t);
	while(t--)
	{
		cin>>n>>m;
		memset(a,0,sizeof(a));
		memset(p,false,sizeof(p));
		for(i=0;i<n;i++)
		{
			for(j=0;j<m/4;j++)
				cin>>map[i][j];
		}
		for(i=0;i<n;i++)
		{
			num=m-1;
			for(j=m/4-1;j>=0;j--)
			{
				if(map[i][j]<='9' && map[i][j]>='0')c=map[i][j]-'0';
				else c=map[i][j]-'A'+10;
				for(k=1;k<=4;k++)
				{
					map[i][num]=c%2+'0';
					c/=2;
					num--;
				}
			}
		}
		
		if(n<m)bb=n;
		else bb=m;
		for(aa=bb;aa>=1;aa--)
		{
			for(i=0;i<=n-aa;i++)
			{
				for(j=0;j<=m-aa;j++)
				{
					sx=i;
					sy=j;
					ex=sx+aa-1;
					ey=sy+aa-1;
					f=0;
					for(k=sx;k<=ex;k++)
					{
						if(k>sx)
						{
							if(map[k][sy]==map[k-1][sy])
							{
								f=1;
								break;
							}
						}
						for(l=sy;l<=ey;l++)
						{
							if(p[k][l]){f=1;break;}
							if(l>sy)
								if(map[k][l]==map[k][l-1])
								{
									f=1;
									break;
								}
						}
						if(f==1)break;
					}
					if(f==0)
					{
						a[aa]++;
						for(k=sx;k<=ex;k++)
							for(l=sy;l<=ey;l++)
								p[k][l]=true;
					}

				}
			}
		}
		s=0;
		for(i=1;i<=bb;i++)
			if(a[i]>0)s++;
		printf("Case #%d: %d\n",mmm++,s);
		for(i=bb;i>=1;i--)
		{
			if(a[i]>0)
				printf("%d %d\n",i,a[i]);
		}
	}
	return 0;
}