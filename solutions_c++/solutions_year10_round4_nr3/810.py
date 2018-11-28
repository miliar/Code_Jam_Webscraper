#include<iostream>
using namespace std;

#define MAXN 515

int te,r,ans;
bool c[MAXN][MAXN];

void print()
{
	for(int i=0;i<10;++i)
	{
		for(int j=0;j<10;++j)
		{
			if(c[i][j])
			{
				cout<<'1';
			}
			else
			{
				cout<<'0';
			}
		}
		puts("");
	}
}

int main()
{
	freopen("Cl.in","r",stdin);
	freopen("Cl.txt","w",stdout);
	scanf("%d",&te);
	for(int ca=1;ca<=te;++ca)
	{
		scanf("%d",&r);
		memset(c,false,sizeof(c));
		ans=0;
		while(r--)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int i=y1;i<=y2;++i)
			{
				for(int j=x1;j<=x2;++j)
				{
					c[i][j]=true;
				}
			}
		}
		//print();
		while(1)
		{
			for(int i=MAXN-1;i>=1;--i)
			{
				for(int j=MAXN-1;j>=1;--j)
				{
					if(c[i-1][j]&&c[i][j-1])
					{
						c[i][j]=true;
					}
				}
			}

			for(int i=MAXN-1;i>=1;--i)
			{
				for(int j=MAXN-1;j>=1;--j)
				{
					if(!c[i-1][j]&&!c[i][j-1])
					{
						c[i][j]=false;
					}
				}
			}

			int cnt=0;
			for(int i=MAXN-1;i>=1;--i)
			{
				for(int j=MAXN-1;j>=1;--j)
				{
					if(c[i][j])
					{
						cnt++;
						break;
					}
				}
			}

			ans++;

			if(cnt==0)
			{
				break;
			}
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
