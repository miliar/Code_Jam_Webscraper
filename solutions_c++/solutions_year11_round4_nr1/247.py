#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
const double ee=0.00000001;
int w[1100],ww[1100];
int tot,x,s,r,ti,m;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int bi,ei,wi;
	scanf("%d",&tot);
	for(int t=1;t<=tot;t++)
	{
		double ans=0;
		scanf("%d %d %d %d %d",&x,&s,&r,&ti,&m);
		w[m]=0;
		ww[m]=x;
		double tim=ti;
		for(int i=0;i<m;i++)
		{
			scanf("%d %d %d",&bi,&ei,&w[i]);
			ww[m]-=(ei-bi);
			ww[i]=ei-bi;
		}
		for(int i=0;i<=m;i++)
			for(int j=m;j>i;j--)
				if(w[j]<w[j-1])
				{
					int temp=w[j];w[j]=w[j-1];w[j-1]=temp;
					temp=ww[j];ww[j]=ww[j-1];ww[j-1]=temp;
				}
		for(int i=0;i<=m;i++)
		{
			double si=double(ww[i])/double(r+w[i]);
			if(tim>=si+ee)
			{
				tim-=si;
				ans+=si;
			}else
			if(tim<=ee)
			{
				ans+=(double(ww[i])/double(s+w[i]));
			}else
			{
				ans+=tim;
				double wlen=double(ww[i])-tim*double(r+w[i]);
				ans+=(wlen/double((s+w[i])));
				tim=0;
			}
		}
		printf("Case #%d: %.9lf\n",t,ans);
	}
	return 0;
}
