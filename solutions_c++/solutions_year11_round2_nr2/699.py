#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<math.h>
using namespace std;
int t,cc=1,c,cp,vm[201],h1;
double d,pm[201],xxx;
bool check(double time)
{
	double pre=-1e15,ll;
	for(h1=0;h1<cp;h1++)
	{
		ll=max(pre+d,pm[h1]-time);
		double ttt=fabs((ll+d*(vm[h1]-1))-pm[h1]);
		if(fabs((ll+d*(vm[h1]-1))-pm[h1])-(1e-10)>time)return false;
		pre=(ll+d*(vm[h1]-1));
	}
	return true;
}

int main(){
	freopen("out.txt","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%lf",&c,&d);
		cp=0;
		for(h1=0;h1<c;h1++)
		{
			scanf("%lf%d",&pm[h1],&vm[h1]);
			if(vm[h1])
			{
				pm[cp]=pm[h1];
				vm[cp++]=vm[h1];
			}
		}
		int h2;
		for(h1=0;h1<cp;h1++)
		{
			for(h2=h1+1;h2<cp;h2++)
			{
				if(pm[h1]>pm[h2])
				{
					swap(pm[h1],pm[h2]);
					swap(vm[h1],vm[h2]);
				}
			}
		}
		double upper=1e15,lower=0,xxx;
		int ccc=0;
		while(fabs(upper-lower)>1e-10)
		{
			double mid=(upper+lower)/2;
			if(check(mid))
				upper=mid;
			else
				lower=mid;
		}
		printf("Case #%d: %.10lf\n",cc++,upper);
	}
}
