#include <iostream>
#include <string>
using namespace std;

int maxm_g(int n,int s,int p, int points[]);
int main()
{
	int t,cnt=0,i;
	int n,s,p,tp[150],high=0;
	freopen("B-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++)
			scanf("%d",&tp[i]);
		high=maxm_g(n,s,p,tp);
		scanf("\n");
		printf("Case #%d: %d\n",++cnt,high);
	}
	return 0;
}

int maxm_g(int n,int s,int p, int points[])
{
	int i,high=0,jdg[3];
	for(i=0;i<n;i++)
	{
		if(points[i]<p)
			continue;
		if(((float)points[i]/3)>=(float)(points[i]/3)+.5)
			jdg[0]=points[i]/3+1;
		else jdg[0]=points[i]/3;
		if(jdg[0]>=p)
		{
			high++;
			continue;
		}
		else
		{
			jdg[1]=jdg[0];
			jdg[2]=points[i]-(jdg[0]+jdg[1]);
			if(jdg[2]>jdg[0])
			{
				if(jdg[2]>=p)
				{
					high++;
					continue;
				}
			}
			else if(s>0)
			{
				if(jdg[0]+1>=p)
				{
					high++;
					s--;
					continue;
				}
			}
		}
	}
	return high;
}