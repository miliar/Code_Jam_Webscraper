#include<iostream>
#include<cmath>
using namespace std;

int x[100],y[100],r[100];
int xx[2],yy[2],rr[2];

int main()
{
    freopen("1.txt","r",stdin);//B-large.in
	freopen("2.txt","w",stdout);
	int cas,ca;
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		int i;
		int n;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d %d %d",x+i,y+i,r+i);
		if(n==0)
			printf("Case #%d: 0\n",ca);
		if(n==1)
			printf("Case #%d: %d\n",ca,r[0]);
		if(n==2)
			printf("Case #%d: %d\n",ca, max(r[0],r[1]));
		else
		{
			double res=1e100;
			for(i=0;i<3;i++)
			{
				double ma=r[i];
				int j,rn=0;
				for(j=0;j<3;j++)
					if(j!=i)
					{
						xx[rn] = x[j];
						yy[rn] = y[j];
						rr[rn] = r[j];
						rn++;
					}
				double dis = sqrt( (xx[1]-xx[0])*(xx[1]-xx[0]) + ( (yy[1]-yy[0])*(yy[1]-yy[0]) ) + 0.0 );
				dis = (dis + rr[0] + rr[1])/2;
				ma = max(dis,ma);
				res = min(res,ma);
			}
			printf("Case #%d: %lf\n",ca,res);
		}
	}
}
