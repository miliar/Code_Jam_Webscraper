#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAXN = 1010;
int x[MAXN],y[MAXN];
pair<int,int> r[MAXN];
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		int n,w,l;
		scanf("%d%d%d",&n,&w,&l);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&r[i].first);
			r[i].first=-r[i].first;
			r[i].second=i;
		}
		sort(r+1,r+n+1);
		for (int i=1;i<=n;i++) r[i].first=-r[i].first;
		bool flag=false;
		if (l>w) {
			swap(w,l); flag=true;
		}
		int xx=0,yy=0,last=r[1].first;
		for (int i=1;i<=n;i++)
		{
			int p=r[i].second;
			int rr=r[i].first;
			int rn=r[i+1].first;
			x[p]=xx; y[p]=yy;
			if (xx+rr+rn>w){
				xx=0;
				yy+=last+rn;
				last=rn;
			} else {
				xx += rr+rn;
			}
		}

		for (int i=1;i<=n;i++)
			if (flag) swap(x[i],y[i]);
		printf("Case #%d:",tcase);
		for (int i=1;i<=n;i++)
			printf(" %d %d",x[i],y[i]);			
		printf("\n");
	}
	return 0;
}
