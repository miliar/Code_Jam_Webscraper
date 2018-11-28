#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

int gcd( int a , int b ){
	if( b == 0 )return a ; 
	return gcd( b , a%b);
}
int main(){
	freopen("D://A-small-attempt2.in","r",stdin);
    freopen("D://A-small-attempt2.out","w",stdout);
	
	int t; 
	scanf("%d",&t);
	for(int cases = 1 ; cases<=t;++cases){
		int n ; 
		scanf("%d",&n);
		int pd, pg ;
		scanf("%d%d",&pd,&pg);
		bool fl = 0; 
		for(int i = 1 ; i<=n;++i){
			if( ( i * pd ) % 100 == 0 ) {
				int a = pg , b = 100;
				int tc = i * pd / 100 ;
				int d = 100 * tc - pg * i ;
//				if( pd >= pg){
					if( d == 0 ) fl = 1 ; 
					else {
						for(int x = 0 ; x<10000&&fl == 0;++x)
							for(int y = 0 ; y<=x&&fl== 0;++y){
								if( a * x - b * y == d )
									fl = 1 ; 
							}
					}
				}
		//	}
		}
		if( fl == 1 ) printf("Case #%d: Possible\n",cases);
		else printf("Case #%d: Broken\n",cases);
	}

	return 0 ;
}