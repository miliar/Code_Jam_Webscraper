#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;
#define NN 10008

int canreach(int n, int d[], int l[])
{
	int minok, i, lastf;
	priority_queue< pair<int,int> > value;
	minok = n;
	for (i=n-1; i>=0; i--)
	{
		while (!value.empty() && (value.top()).first >= d[i]) {
			if (minok > (value.top()).second) minok = (value.top()).second;
			value.pop();
		}
		if (l[i] + d[i] >= d[minok]) {
			value.push( make_pair(d[i] - d[minok] + d[i], i) );
			lastf = d[minok] - d[i];
		} else lastf = d[i]+1;
//		printf(" i=%d minok=%d\n", i, minok);
	}
	if (d[0] < lastf) return 0;
	return 1;
}			

int main()
{
	int i,n,t,d[NN],l[NN];
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d",&t);
	for (int cas = 1; cas <= t; cas++)
	{
		scanf("%d",&n);
		for (i=0; i<n; i++) scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&d[n]);
		if (canreach(n,d,l)) printf("Case #%d: YES\n", cas);
		else printf("Case #%d: NO\n", cas);
	}
	return 0;
}

