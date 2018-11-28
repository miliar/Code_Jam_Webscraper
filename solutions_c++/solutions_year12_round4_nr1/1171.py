#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 10005;
const int inf = 2000000001;

int n, m, D;
int l[N], d[N], best[N];

void Solve(){
	memset(best, 0, sizeof(best));
	if (l[1] < d[1]){
		printf("NO\n");
		return;
	}
	best[1] = min(d[1], l[1]);
	for(int i = 1; i < n; i++){
		for(int j = i+1; j <= n; j++)
			if (d[j]-d[i] <= best[i])
				best[j] = max(best[j], min(d[j]-d[i],l[j]));
			else break;
	}
	if (best[n] != 0) printf("YES\n");
	else printf("NO\n");
}

int main()
{
	freopen("large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int ntest;
	cin >> ntest;
	for(int test = 1; test <= ntest; test++){
		printf("Case #%d: ", test);
		scanf("%d", &n);
		for(int i = 1; i <= n; i++)
			scanf("%d %d", &d[i], &l[i]);
		cin >> D;
		n++;
		l[n] = inf; d[n] = D;
		Solve();		
	}
	
	return 0;
}
