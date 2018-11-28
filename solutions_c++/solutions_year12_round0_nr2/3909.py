#include<stdio.h>
int n , s, p;
int a,ans;
int main(){
	int T;
	freopen("bans.out","w",stdout);
	scanf("%d",&T);
	for ( int t = 1 ; t <= T ; t ++ ){
		ans = 0;
		scanf("%d %d %d" , &n , &s , &p);
		for ( int i = 1 ;  i <= n ; i ++){
			scanf("%d" , &a ) ;
			if ( a / 3 >= p || ( a / 3 == p - 1 && a % 3 != 0 ))
				ans ++ ;
			else{
				if  ( !s )
					continue;
				int now = a / 3 ;
				a = a % 3 ;
				if ( a == 0 && now != 0 ){
					if ( now >= p - 1 ){
						s -- ;
						ans ++ ;
					}
				}
				else if ( a == 2 ){
					if ( now + 2 >= p ){
						s--;
						ans ++ ;
					}
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
