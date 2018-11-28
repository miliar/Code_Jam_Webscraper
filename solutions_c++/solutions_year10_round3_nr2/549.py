#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <string>
#include <vector>
using namespace std;

const int maxn = 1000+5;
int L, P, C;
const int INFI = 0x7fffffff;

const double eps = 1e-9;

int sign( double a, double b ){
	if( a-b>eps ) return 1;
	if( a-b<-eps) return -1;
	return 0;
}

void read(){
	int i, j, ans=0;
	scanf("%d%d%d", &L, &P, &C);
	double x=1.0*P/L;
	while( sign(x,C)==1 ){
		x = sqrt(x);
		ans++;
	}
	printf("%d\n", ans );
}

void solve(){
}

int main(){
	//freopen("d:\\in.txt", "r", stdin );

	freopen("d:\\B-small-attempt0.in", "r", stdin );
	freopen("d:\\B-small-attempt0.out", "w", stdout );

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
