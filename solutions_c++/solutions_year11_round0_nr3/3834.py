#include <iostream>
using namespace std;
int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int sum,mmin,xx,temp,num,i;
	int T;
	int cnt=0;
	scanf("%d",&T);
	while(T--)
	{
		cnt++;
		scanf("%d",&num);
		sum=0;
		xx=0;
		mmin=99999999;
		for(i=0;i<num;i++)
		{
			scanf("%d",&temp);
			sum+=temp;
			xx=(xx^temp);
			mmin=mmin<temp?mmin:temp;
		}
		if(xx==0)
		{
			printf("Case #%d: %d\n",cnt,sum-mmin);
		}
		else printf("Case #%d: NO\n",cnt);
	}
}