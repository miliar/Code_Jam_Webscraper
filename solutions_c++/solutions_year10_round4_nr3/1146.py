#include<stdio.h>
#include<string.h>
#define inf 0x7fffffff
bool _node[101][101],temp[101][101];
int main()
{
	int cas,n,x1,x2,y1,y2,i,j,ii,cnt,x,y;
	bool flag;
	//freopen("C-small-attempt3.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d",&n);
		memset(_node,false,sizeof(_node));
		x=y=-inf;
		while(n--)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x2>x)
				x=x2;
			if(y2>y)
				y=y2;
			for(j=y1;j<=y2;j++)
				for(i=x1;i<=x2;i++)
					_node[j][i]=true;
		}
		cnt=0;
		while(1)
		{
			cnt++;
			memset(temp,false,sizeof(temp));
			for(j=1;j<=y;j++)
				for(i=1;i<=x;i++)
					if(_node[j-1][i]&&_node[j][i-1])
						temp[j][i]=true;
					else if(_node[j-1][i]==false&&_node[j][i-1]==false)
						temp[j][i]=false;
					else
						temp[j][i]=_node[j][i];
			flag=false;
			for(j=1;j<=y;j++)
				for(i=1;i<=x;i++)
				{
					_node[j][i]=temp[j][i];
					if(_node[j][i])
						flag=true;
				}
			if(flag==false)
				break;
		}
		printf("Case #%d: %d\n",ii,cnt);
	}
	return 0;
}
			
