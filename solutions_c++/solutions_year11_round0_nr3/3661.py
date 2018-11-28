#include <cstdio>
using namespace std;

const int MAXN = 1050;
int candy[MAXN];

void solve(void)
{
	int n, r, s, Min, i;
	Min = 2000000;
	scanf("%d", &n);
	r = s = 0;
	for(i=0; i<n; i++){
		scanf("%d", &candy[i]);
		if(candy[i]<Min) Min = candy[i];
		r ^= candy[i];
		s += candy[i];
	}
	if(r!=0) printf("NO");
	else {
		printf("%d", s-Min);
	}
	return;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int t, i;
	scanf("%d", &t);
	for(i=1; i<=t; i++){
		printf("Case #%d: ", i);
		solve();
		puts("");
	}
	return 0;
}
