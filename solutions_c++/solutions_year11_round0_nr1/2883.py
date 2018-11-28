#include<cstdio>
#include<cmath>

using namespace std;

int solve()
{
	int total=0,count,r,opos=1,bpos=1,cur=0,needed;
	char p,prevs='E';
	scanf("%d ",&count);
	for(int i=0;i<count;i++)
	{
		scanf("%c %d ",&p,&r);
		if(p=='O')
		{
			needed=abs(r-opos)+1;
			opos=r;
		}else{
			needed=abs(r-bpos)+1;
			bpos=r;
		}
		if(prevs==p)
		{
			cur+=needed;
		}else{
			if(needed<=cur)
			{
				needed=cur=1;
			}else{
				needed=cur=needed-cur;
			}
			prevs=p;
		}
		total+=needed;
	}
	return total;
}

int main()
{
	int t;
	scanf("%d\n",&t);
	for(int i=0;i<t;i++)
	{
		printf("Case #%d: %d\n",i+1,solve());
	}
	return 0;
}
