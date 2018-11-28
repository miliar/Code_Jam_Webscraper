#include<iostream>
#include<string>
#include<algorithm>
using namespace std ;
struct Node{
	int state ;
	int val ;
};
Node node[10005] ;
int DP[10005][2] ;
int n;
int Max;

void slove( int kk ){
	bool leaf = false ;
	int i ;	
	if( 2*kk + 1 <= n ){
		leaf = true ;
		slove( 2*kk ) ;
		slove( 2*kk + 1 ) ;
		if( node[kk].val == 1 ){
			DP[kk][0] = min( min(DP[2*kk][0] + DP[2*kk+1][1] ,  DP[2*kk][1] + DP[2*kk+1][0] ), DP[2*kk][0] + DP[2*kk+1][0] ) ;
			DP[kk][1] = DP[2*kk][1] + DP[2*kk+1][1] ;
			if( node[kk].state == 1 )
				DP[kk][1] = min( min(DP[kk][1] ,  DP[2*kk][1] + DP[2*kk+1][0] + 1 ), DP[2*kk][0] + DP[2*kk+1][1] + 1 ) ;
		}
		else{
			DP[kk][1] = min( min(DP[2*kk][0] + DP[2*kk+1][1] ,  DP[2*kk][1] + DP[2*kk+1][0] ), DP[2*kk][1] + DP[2*kk+1][1] ) ;
			DP[kk][0] = DP[2*kk][0] + DP[2*kk+1][0] ;
			if( node[kk].state == 1)
				DP[kk][0] = min( DP[kk][0] , min( DP[2*kk][1] + DP[2*kk+1][0] + 1 , DP[2*kk][0] + DP[2*kk+1][1] + 1 ))  ;
		}
	}
	if( !leaf ){
		if( node[kk].val == 0 ){
			DP[kk][1] = Max ;
			DP[kk][0] = 0 ;
		}
		else{
			DP[kk][0] = Max ;
			DP[kk][1] = 0 ;
		}
		return ;
	}
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	int test ;
	scanf("%d",&test) ;
	int Case = 0 ;
	while( test -- ){
		int root ;
		Case++;
		scanf("%d",&n);
		scanf("%d",&root) ;
		int i ;
		for( i = 1 ; i <= (n -1)/2 ; i ++ )
			scanf("%d%d",&node[i].val,&node[i].state) ;
		for( i = (n - 1)/2 + 1 ; i <= n ; i ++ ){
			scanf("%d",&node[i].val) ;
			node[i].state = -1 ;
		}
		Max = 10006;
		for( i = 0  ; i <= n ; i ++ ){
			DP[i][0] = Max;
			DP[i][1] = Max ;
		}
		////////////////////////////////////////////////
		slove(1) ;//Ê÷ÐÎDP
		printf("Case #%d: " , Case) ;
		if( DP[1][root] < Max )
			printf("%d\n" , DP[1][root] ) ;
		else
			printf("IMPOSSIBLE\n") ;
	}
	return  0;
}