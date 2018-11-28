#include<stdio.h>
#include<map>
#include<algorithm>
using namespace std;
int r[128*128];
int get(int x)
{
	if(x==r[x])
		return x;
	return r[x]=get(r[x]);
}
int v[128][128];
map<int,int> my;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int kk[4][2]={-1,0,0,-1,0,1,1,0};
	int c,o,n,m,i,j,k,rr,x,y,d;
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		printf("Case #%d:\n",o);
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",v[i]+j);
		for(i=0;i<n*m;i++)
			r[i]=i;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				rr=-1;
				for(k=0;k<4;k++)
				{
					x=kk[k][0]+i;
					y=kk[k][1]+j;
					if(x>=0&&x<n&&y>=0&&y<m)
						if(v[x][y]<v[i][j])
							if(rr==-1)
							{
								rr=x*m+y;
								d=v[i][j]-v[x][y];
							}
							else if(v[i][j]-v[x][y]>d)
							{
								d=v[i][j]-v[x][y];
								rr=x*m+y;
							}
				}
				if(rr!=-1)
				{
					x=get(i*m+j);
					y=get(rr);
					if(x!=y)
						r[x]=y;
				}
			}
		rr=1;
		my.clear();
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				x=get(i*m+j);
				if(!my[x])
					my[x]=rr++;
				printf("%c",my[x]-1+'a');
				if(j==m-1)
					printf("\n");
				else
					printf(" ");
			}
	}
	return 0;
}

