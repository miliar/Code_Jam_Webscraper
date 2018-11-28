
#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
int dfs( int L , int R ){
	if( L + 1 == R )return 0;
	int mid = (L+R ) / 2 ;
	return max( dfs( L, mid) + 1, dfs(mid,R) + 1 ) ;
}
int main(){
	freopen("G:\\B-large.in","r",stdin);
	freopen("G:\\B-large.out","w",stdout);
	int  t ;
	scanf("%d",&t);
	for(int cases = 1; cases<=t;++cases){
		long long L , P , C ;
		scanf("%lld%lld%lld",&L,&P,&C);
		int i = 0 ; 
		while(L<P){
			L *=C;
			i++;
		}
		++i;
		int res = dfs(0 , i -1 );
		printf("Case #%d: %d\n",cases,res);
	}
	return 0 ;

}