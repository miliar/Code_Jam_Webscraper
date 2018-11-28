#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int m,n,tt,c,r;
char ch[10];
struct buttom
{
	char c;
	int node;
	int next;
};
buttom b[300];
int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{
		cin>>n;
		int i,fb=-1,fo=-1;
		for (i=1;i<=n;++i)
		{
			cin>>ch>>m;
			b[i].c=ch[0];
			b[i].next=-1;
			b[i].node=m;
		}
		for (i=1;i<=n;++i)
		{
			if (b[i].c=='B')
			{
				break;
			}
		}
		int last=i;
		fb=i;
		i++;
		for (;i<=n;++i)
		{
			if (b[i].c=='B')
			{
				b[last].next=i;
				last=i;
			}
		}
		for (i=1;i<=n;++i)
		{
			if (b[i].c=='O')
			{
				break;
			}
		}
		fo=i;
		last=i;
		i++;
		for (;i<=n;++i)
		{
			if (b[i].c=='O')
			{
				b[last].next=i;
				last=i;
			}
		}
		int stb=1,sto=1;
		int nextb,nexto;
		int ans=0;
		nextb=b[fb].node;
		nexto=b[fo].node;
		for (int i=1;i<=n;++i)
		{
			if (b[i].c=='B')
			{
				ans+=nextb;
				nexto=max(1,nexto-nextb);
				if (b[i].next==-1)
				{
					nextb=0;
				}
				else
				{
					nextb=abs(b[b[i].next].node-b[i].node)+1;
				}				
			}
			else
			{
				ans+=nexto;
				nextb=max(1,nextb-nexto);
				if (b[i].next==-1)
				{
					nexto=0;
				}
				else
				{
					nexto=abs(b[b[i].next].node-b[i].node)+1;
				}				
			}
		}

		
		printf("Case #%d: %d\n",kk,ans);			
	}	
	return 0;	
}