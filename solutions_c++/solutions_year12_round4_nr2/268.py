#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

void solve(int t)
{
	int n,w,l;
	scanf("%d%d%d",&n,&w,&l);
	vector<pair<int,int> > r(n);
	for (int i=0;i<n;++i)
	{
		scanf("%d",&r[i].first);
		r[i].second = i;
	}
	sort(r.rbegin(),r.rend());
	bool sw = w>l;
	if (sw)
		swap(w,l);
	int x=0,y=0,md = r[0].first;
	printf("Case #%d:",t);
	vector<pair<int,int> > ans(n);
	for (int i=0;i<n;++i)
	{
		if (x!=0)
			x += r[i].first;
		if (x>w)
		{
			x = 0;
			y += md + r[i].first;
			md = r[i].first;
			if (y>l)
			{
				fprintf(stderr,"Error test #%d\n",t);
				exit(1);
			}
		}
		if (sw)
			ans[r[i].second] = make_pair(y,x);
		else
			ans[r[i].second] = make_pair(x,y);
		x += r[i].first;
	}
	for (int i=0;i<n;++i)
		printf(" %d.0 %d.0",ans[i].first,ans[i].second);
	printf("\n");
}

int main(int argc, char* argv[])
{
	if (argc>1)
		freopen(argv[1],"r",stdin);
	else
		freopen("input.txt","r",stdin);
	int T;
	scanf("%d",&T);
	for (int t=0;t<T;++t)
		solve(t+1);
	return 0;
}
