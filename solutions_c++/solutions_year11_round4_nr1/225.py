#include<cstdio>
#include<algorithm>
using namespace std;
typedef pair<int,int> PII;
#define fi first
#define se second
PII a[1111];
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		int X,S,R,T,N;
		scanf("%d%d%d%d%d",&X,&S,&R,&T,&N);
		for(int i=0,x,y,z;i<N;i++)
			scanf("%d%d%d",&x,&y,&z),
			a[i].fi=z,a[i].se=y-x,
			X-=y-x;
		a[N++]=make_pair(0,X);
		sort(a,a+N);
		double SS=0;
		double TT=T;
		for(int i=0;i<N;i++)
		{
			double F=(double)(a[i].se)/(R+a[i].fi);
			if(F<=TT)TT-=F,SS+=F;else
			{
				SS+=TT+(double)(a[i].se-TT*(R+a[i].fi))/(S+a[i].fi);
				TT=0;
			}
		}
		printf("Case #%d: %.9lf\n",__,SS);
	}
	return 0;
}

