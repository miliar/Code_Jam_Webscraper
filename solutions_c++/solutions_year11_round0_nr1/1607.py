#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<fstream>

using namespace std;

#define MAXN 110

struct Node
{
	int R;
	char p[2];
}s[MAXN];

int n;

int pos(int st,char ch)
{
	for(int i=st;i<n;i++)
	{
		if(s[i].p[0]==ch) return i;
	}
	return -1;
}

int main()
{
	int ct,text;
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	scanf("%d",&text);
	for(ct=1;ct<=text;ct++)
	{
		int i,j;
		int x,y,px,py,step=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",s[i].p,&s[i].R);
		}
		x=y=1;
		px=pos(0,'O'),py=pos(0,'B');
		for(i=0;i<n;step++)
		{
			bool pus=false;
			if(px!=-1)
			{
				if(x>s[px].R)
				{
					x--;
				}
				else if(x<s[px].R)
				{
					x++;
				}
				else
				{
					if(s[i].p[0]=='O')
					{
						pus=true;
						px=pos(++i,'O');
					}
				}
			}
			if(py!=-1)
			{
				if(y>s[py].R)
				{
					y--;
				}
				else if(y<s[py].R)
				{
					y++;
				}
				else
				{
					if(s[i].p[0]=='B' && !pus)
					{
						py=pos(++i,'B');
					}
				}
			}
		}
		printf("Case #%d: %d\n",ct,step);
	}
	return 0;
}
