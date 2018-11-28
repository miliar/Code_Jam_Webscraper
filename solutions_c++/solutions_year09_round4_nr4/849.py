#include <iostream>
#include <cmath>

using namespace std;

struct Cir
{
	double x,y,r;
};

Cir data[10];
int cd;

double dist(const Cir &c1,const Cir&c2)
{
	return sqrt((c1.x-c2.x)*(c1.x-c2.x)+(c1.y-c2.y)*(c1.y-c2.y));
}

double solve()
{
	if(cd==1) return data[0].r;
	else if(cd==2)
	{
		if(data[0].r>data[1].r) return data[0].r;
		return data[1].r;
	}
	else
	{
		int i,j,k;
		double ret=1e10;
		for(i=0;i<3;i++)
		{
			for(j=i+1;j<3;j++)
			{
				for(k=0;k<3;k++)
				{
					if(k!=i&&k!=j) break;
				}
				double r1=data[i].r+data[j].r+dist(data[i],data[j]);
				r1/=2;
				double r2=data[k].r;
				if(r1<r2) swap(r1,r2);
				if(r1<ret) ret=r1;
			}
		}
		return ret;
	}
	return 0;
}

int main()
{
	int t;
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		scanf("%d",&cd);
		int i;
		for(i=0;i<cd;i++)
		{
			scanf("%lf%lf%lf",&data[i].x,&data[i].y,&data[i].r);
		}
		double ret=solve();
		printf("Case #%d: %.6f\n",cse,ret);
	}
	return 0;
}

