#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

struct node {
	int pre , val , next;

};
node a[1005];

double fabs( double x ) {
	if( x < 0 ) return -x;
	return x;
}

bool cmp( node a,node b) {
	return a.val < b.val;
}

int main() {
	int  n , test ,i , j;
	int tc  =1;
	freopen("ds.in","r",stdin);
	freopen("ds.out","w",stdout);
	scanf("%d",&test );
	while( test-- && scanf("%d",&n) != EOF ) {
		double ans = 0 ;
		for( i = 0 ; i < n;i++ ) {
			scanf("%d",&j);
			a[i].val = j;
			a[i].pre = i;
		}	
		sort( a , a + n , cmp );
		for( i = 0 ; i < n;i++) {
			if( i != a[i].pre)
				ans ++;
		}
		printf("Case #%d: %0.6lf\n",tc ++ ,ans );
	}
	return 0;
}
