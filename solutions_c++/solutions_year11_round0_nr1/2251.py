#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

struct info
{
	char ro;
	int bu;
};

info cmd[110];
int next[110];
int n,o,b;

void getdata(void);

int abs(int x)
{
	return x<0?-x:x;
}

int main()
{
	freopen("in.txt","w",stdout);
	freopen("test.txt","r",stdin);
	int ca,i,x,z,wb,wo,ans,ti,tp;
	scanf("%d",&ca);
	for (z=1;z<=ca;z++)
	{
		getdata();
		printf("Case #%d: ",z);
		ti=0;
		wb=1;
		wo=1;
		for (i=0;i<n;i++)
		{
			if (cmd[i].ro=='O')
			{
				tp=abs(wo-cmd[i].bu)+1;
				ti+=tp;
				wo=cmd[i].bu;
				o=next[i];
				if (abs(wb-cmd[b].bu)<=tp)
				{
					wb=cmd[b].bu;
				}
				else
				{
					if (wb<cmd[b].bu)
						wb+=tp;
					else
						wb-=tp;
				}
			}
			else
			{
				tp=abs(wb-cmd[i].bu)+1;
				ti+=tp;
				wb=cmd[i].bu;
				b=next[i];
				if (abs(wo-cmd[o].bu)<=tp)
				{
					wo=cmd[o].bu;
				}
				else
				{
					if (wo<cmd[o].bu)
						wo+=tp;
					else
						wo-=tp;
				}
			}
		}
		printf("%d\n",ti);
	}
	return 0;
}

void getdata(void)
{
	int i;
	scanf("%d",&n);
	for (i=0;i<n;i++)
		scanf(" %c %d",&cmd[i].ro,&cmd[i].bu);
	o=-1;
	b=-1;
	for (i=n-1;i>=0;i--)
	{
		if (cmd[i].ro=='O')
		{
			next[i]=o==-1?i:o;
			o=i;
		}
		else
		{
			next[i]=b==-1?i:b;
			b=i;
		}
	}
}