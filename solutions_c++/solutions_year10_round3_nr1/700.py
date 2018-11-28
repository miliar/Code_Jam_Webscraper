#include <iostream>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <string>
#include <vector>
using namespace std;

const int maxn = 1000+5;
int n;
struct Wire{
	int l, r;
};
Wire wr[maxn];
bool ok( const Wire &a, const Wire &b ){
	return ( a.l-b.l)*(a.r-b.r)<0;
}

void read(){
	int i, j, ans=0;
	scanf("%d", &n);
	for( i=1; i<=n; ++i )
		scanf("%d%d", &wr[i].l, &wr[i].r );
	for( i=1; i<=n; ++i ){
		for( j=i+1; j<=n; ++j )
			ans += ok(wr[i], wr[j] );
	}
	printf("%d\n", ans );
}

void solve(){
}

int main(){
	//freopen("d:\\in.txt", "r", stdin );

	freopen("d:\\A-small-attempt0.in", "r", stdin );
	freopen("d:\\A-small-attempt0.out", "w", stdout );

	//freopen("d:\\A-large.in", "r", stdin );
	//freopen("d:\\A-large.out", "r", stdin );

	int num_case;
	scanf("%d", &num_case);
	for( int i=1; i<=num_case; ++i ){
		printf("Case #%d: ", i );
		read();
		solve();
	}
	return 0;
}
