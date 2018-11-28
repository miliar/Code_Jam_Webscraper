#include<iostream>
using namespace std;

bool b[101][101];
char c[101][101];
int a[101][101];
int h,w,dre[][2]={-1,0,0,-1,0,1,1,0};

bool ok(int i,int j)
{
	return i>=0&&i<h&&j>=0&&j<w;
}

struct node
{
	int x,y;
}nd[10001];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	int t,i,j,k,T=0,len;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&h,&w);
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				scanf("%d",&a[i][j]);

		memset(b,0,sizeof(b));
		char ch='a';
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				if(!b[i][j])
				{
					len=0;
					nd[len].x=i;
					nd[len++].y=j;
					while(1)
					{
						int ma=9999999,xx,yy;
						for(k=0;k<4;k++)
						{
							int I=dre[k][0]+nd[len-1].x,J=dre[k][1]+nd[len-1].y;
							if(ok(I,J)&&a[I][J]<a[nd[len-1].x][nd[len-1].y]&&a[I][J]<ma)
							{
								ma=a[I][J];
								xx=I;
								yy=J;
							}
						}
						if(ma==9999999)
							break;
						else
						{
							nd[len].x=xx;
							nd[len++].y=yy;
							if(b[xx][yy])
								break;
						}
					}
					char cc;
					if(b[nd[len-1].x][nd[len-1].y])
					{
						cc=c[nd[len-1].x][nd[len-1].y];
						len--;
					}
					else
					{
						cc=ch;
						ch++;
					}
					for(k=0;k<len;k++)
					{
						c[nd[k].x][nd[k].y]=cc;
						b[nd[k].x][nd[k].y]=1;
					}

				}
		printf("Case #%d:\n",++T);
		for(i=0;i<h;i++,printf("\n"))
			for(j=0;j<w;j++)
			{
				printf("%c ",c[i][j]);
			}
			

	}
	return 0;
}