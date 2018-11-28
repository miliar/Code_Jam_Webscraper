#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

int main(){
	freopen("F://A-large.in","r",stdin);
	freopen("F://A-large.out","w",stdout);
	int t ;
	scanf("%d",&t);
	for(int cases =1 ; cases <= t ;++cases){
		int n ;
		scanf("%d",&n);
		char a ; 
		int b ; 
		int x = 1 , y = 1 ; 
		int tx = 0 , ty = 0 ;
		int res = 0 ,tmp; 
		for(int i = 0 ; i<n ;++i){
			scanf(" %c%d",&a,&b);
			if( a == 'O'){
				tmp = abs( b - x ) - tx ;
				if( tmp < 0 ) tmp = 0 ; 
				tmp++;
				x = b ; 
				res += tmp ;
				tx = 0 ; 
				ty += tmp ; 
			}
			else if( a == 'B' ){
				tmp = abs( b - y ) - ty ;
				if( tmp < 0 ) tmp = 0 ; 
				tmp++;
				y = b ; 
				res += tmp ; 
				ty = 0 ; 
				tx += tmp ;
			}
		}
		printf("Case #%d: %d\n",cases,res);
	}
	return 0 ;
}