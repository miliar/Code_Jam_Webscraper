#include <cstdio>
#include <algorithm>

using namespace std;

int a[10],n;

int gcd( int x, int y ){
	if ( y==0 ) return x;
	return gcd(y,x%y);
}

int main(){
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d", &n);
		for ( int i=0; i<n; ++i )
			scanf("%d", a+i);
		sort(a,a+n);
		int t=0;
		for ( int i=1; i<n; ++i )
			t=gcd(t,a[i]-a[i-1]);
		printf("Case #%d: ", T);
		printf("%d\n", (t-a[0]%t)%t);
	}
}
