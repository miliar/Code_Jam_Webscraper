#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
#define M	120
int pos[M];
int w[M];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,n,t=1;
	scanf("%d",&T);
	while(T--)
	{
		char who[2];
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s%d",who,pos+i);
			if(who[0]=='O')
				w[i]=0;
			else	w[i]=1;
		}
		int po=1,pb=1,to=0,tb=0;
		if(w[0]==0)
		{
				to=pos[0];
				po=pos[0];
		}
		else
		{
				tb=pos[0];
				pb=pos[0];
		}
		//printf("%d %d %d %d\n",to,tb,po,pb);
		for(int i=1;i<n;i++)
		{
			if(w[i]==w[i-1])
			{
				if(w[i]==0)
				{
					to=abs(pos[i]-po)+to+1;
					po=pos[i];
				}
				else
				{
					tb=abs(pos[i]-pb)+tb+1;
					pb=pos[i];
				}
			}
			else
			{
				if(w[i]==0)
				{
					to=max(abs(pos[i]-po)+to+1,tb+1);
					po=pos[i];
				}
				else
				{
					tb=max(abs(pos[i]-pb)+tb+1,to+1);
					pb=pos[i];
				}
			}
		}
		printf("Case #%d: %d\n",t++,max(to,tb));	
	}
	return 0;
}
