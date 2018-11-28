#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
char a[4][4];
struct pos{
	int x[4],y[4];
}p[10];
bool f(char s[4])
{
	int cnt[3];
	int i;
	memset(cnt,0,sizeof(cnt));
	for(i=0;i<4;i++)
	{
		if(s[i]=='X')
		{
			cnt[0]++;
		}
		else if(s[i]=='O')
		{
			cnt[1]++;
		}
		else if(s[i]=='T')
		{
			cnt[2]++;
		}
	}
	if(cnt[0]==4||cnt[1]==4)
	{
		return 1;
	}
	else if(cnt[2]==1&&(cnt[0]==3||cnt[1]==3))
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
int main()
{
	freopen("OUTPUT.txt", "w", stdout);
	int n;
	int i,j,k;
	int ca;
	scanf("%d",&n);
	k=0;
	bool flag;
	for(i=0;i<8;i+=2)
	{
		for(j=0;j<4;j++)
		{
			p[k].x[j]=i/2;
			p[k].y[j]=j;
			p[k+1].y[j]=i/2;
			p[k+1].x[j]=j;
			
		}
		k+=2;		
	}
	for(i=0;i<4;i++)
	{
		p[k].x[i]=p[k].y[i]=i;
		p[k+1].x[i]=i;
		p[k+1].y[i]=3-i;
	}
	k+=2;
	int cnt;
	char s[4];
	ca=1;
	
	while(n--)
	{
		getchar();
		cnt=0;
		flag=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%c",&a[i][j]);
				if(a[i][j]=='X'||a[i][j]=='O')
				{
					cnt++;
				}
			}
			getchar();
		}
		for(i=0;i<10;i++)
		{
			for(j=0;j<4;j++)
			{
				s[j]=a[p[i].x[j]][p[i].y[j]];
			}
			if(f(s))
			{
				if(cnt%2==1)
				{
					printf("Case #%d: X won\n",ca++);
				}
				else
				{
					printf("Case #%d: O won\n",ca++);
				}
				flag=true;
				break;
			}
		}
		if(!flag)
		{
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(a[i][j]=='.')
					{
						flag=true;
					}
				}
			}
			if(!flag)
			{
				printf("Case #%d: Draw\n",ca++);
			}
			else
			{
				printf("Case #%d: Game has not completed\n",ca++);
			}
		}
	}
	return 0;
}