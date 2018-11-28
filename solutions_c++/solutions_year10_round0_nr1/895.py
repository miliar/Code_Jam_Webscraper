/*
    Qualification Round 2010 -
    Snapper Chain
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
using namespace std ;

    int T, K, N;

int main(){
    scanf("%d",&T);
    for(int z=1;z<=T;++z){
        scanf("%d %d",&N,&K);
        int M = 1<<N;
        if((K+1)%M==0)
            printf("Case #%d: ON\n",z);
        else
            printf("Case #%d: OFF\n",z);
    }
	return 0 ;
}
