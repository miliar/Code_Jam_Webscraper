#include<stdio.h>
int n,p,s;
int ans = 0;
int main(){
	int t;
	scanf("%d",&t);
	for(int g = 0 ; g < t ; g++ ){
		scanf("%d %d %d",&n,&s,&p);
		ans = 0;
		for(int i = 0 ; i < n ; i++ ){
			int x;
			scanf("%d",&x);
			if( x % 3 == 0 && x / 3 >= p ){ ans++; continue; }
			if( x % 3 != 0 && x / 3 + 1 >= p ){ ans++; continue; }
			
			if( x < 2 ) continue;
			if( x % 3 == 0 ) x = x/3 + 1 ;
			else if( x % 3 == 1 ) continue ;
			else if( x % 3 == 2 ) x = x/3 + 2;
			if( x >= p ){
				if( s > 0 ){ ans++; s--; }
			}
		}
		printf("Case #%d: %d\n",g+1,ans);
	}
}
