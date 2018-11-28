#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
int n,d;vector<int> a;
bool can(double p)
{
	double le=a[0]-p;
	for(int i=1;i<a.size();i++)
	{
		int x=a[i];
		double nw=le+d;
		if(nw>x+p)return 0;
		le=max(nw,x-p);
	}
	return 1;
}
double round(double x){long long p=ceil(x);if(p-x<=0.5) return p;else return p-1;}
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		scanf("%d%d",&n,&d);
		a.clear();
		for(int i=0;i<n;i++)
		{
			int x,y;scanf("%d%d",&x,&y);
			for(int j=0;j<y;j++)a.push_back(x);
		}
		sort(a.begin(),a.end());
		double L=0,R=1e18;
		while(R-L>1e-3)
		{
			double M=(L+R)/2;
			if(can(M))R=M;else L=M;
		}
		printf("Case #%d: %.9lf\n",__,round(L*2)/2);
	}
	return 0;
}

