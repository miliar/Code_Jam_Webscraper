#include <iostream>
using namespace std;
int ans[10000] ;
int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("ans1.out","w",stdout);
	int test , Case = 0;
	scanf("%d",&test);
	while ( test--){
		Case++;
		int n  ; 
		scanf("%d",&n) ; 
		int i;
		memset(ans , -1 , sizeof(ans)) ;
		int jishu = 0;
		int biaoji = 0 ;
		for (i = 1 ; i <= n ; i ++){
			jishu = 0 ;
			while (jishu != i){
				biaoji = biaoji + 1 ;
				if(biaoji > n)
					biaoji -= n ;
				if(ans[biaoji] == -1)
					jishu ++ ;
			
			}
			ans[biaoji] = i ;
		}
		int m ;
		scanf("%d",&m);
		printf("Case #%d:",Case);
		while(m--){
			int kk;
			scanf("%d",&kk) ;
			printf(" %d" , ans[kk]); 
		}
		printf("\n");	
	}
	return 0 ; 
}