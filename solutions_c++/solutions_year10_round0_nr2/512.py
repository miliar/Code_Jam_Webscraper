#include <iostream>
#include <algorithm>
using namespace std;

int a[100];

int gcd( int x,int y) {
	if( x < y) {int t = x; x = y ;y = t;}
	if( y == 0) return x;
	return gcd( y , x%y );	
} 

int main() {
	int	test,i,j;		
	freopen("B-small.in","r",stdin);
	freopen("B-out.txt","w",stdout);
	scanf("%d",&test);
	for( i = 1; i <= test ;i++ ) {
		int n;
		scanf("%d",&n);
		for( j = 0 ; j < n ;j++ )	scanf("%d",&a[j]);
		sort( a , a+n );
		int ans = a[1]-a[0];
		for( j = 1; j < n ;j++ )
			ans = gcd( ans,a[j]-a[j-1]);
		printf("Case #%d: ",i);
		a[0] %= ans;
		a[0] = ans - a[0];
		cout<<a[0]%ans<<endl;
	}
		return 0;	
	
}
