/*
    2009  Round 2 -
    Crazy Rows
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std ;

    int T , N , tmp , R[50] ;
    int ans ;

int main(){
    scanf("%d",&T) ;
    for(int z=1;z<=T;++z){
        ans = 0 ;
        scanf("%d",&N) ;
        for(int i=0;i<N;++i)
            R[i] = -1 ;
        for(int i=0;i<N;++i){
            for(int j=0;j<N;++j){
                scanf("%1d",&tmp) ;
                if(tmp) R[i] = j ;
            }
            //printf("%d\n",R[i]) ;
        }
        for(int i=0;i<N;++i){
            if(R[i]>i){
                for(int j=i+1;j<N;++j){
                    if(R[j]<=i){
                        for(int k=j;k>i;--k){
                            swap(R[k],R[k-1]) ;
                            //printf("%d %d\n",k,k-1) ;
                            ++ans ;
                        }
                        break ;
                    }
                }
            }
        }
        fprintf(stderr,"%d\n",z) ;
        printf("Case #%d: %d\n",z,ans) ;
    }
	return 0 ;
}
