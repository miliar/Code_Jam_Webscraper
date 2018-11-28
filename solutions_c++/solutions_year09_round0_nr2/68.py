/*
    Qualification Round 2009 -
    Watersheds
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
using namespace std ;

    const int direct[4][2] = {
        {-1,0},{0,-1},{0,1},{1,0}
    } ;
    int T , H , W , G[102][102] ;
    int ori[102][102] ;
    char out[100][101] ;

int flood(int y,int x){
    //if(ori[y][x]!=y*W+x) return ori[y][x] ;
    int ny = y+direct[0][0] , nx = x+direct[0][1] ;
    for(int i=1;i<4;++i){
        int ty = y+direct[i][0] ;
        int tx = x+direct[i][1] ;
        if(G[ty][tx]<G[ny][nx]){
            ny = ty ;
            nx = tx ;
        }
    }
    if(G[ny][nx]<G[y][x]){
        return ori[y][x] = flood(ny,nx) ;
    }
    return ori[y][x] ;
}

int main(){
    scanf("%d",&T) ;
    for(int z=1;z<=T;++z){
        memset(ori,0,sizeof(ori)) ;
        memset(out,'\0',sizeof(out)) ;
        scanf("%d %d",&H,&W) ;
        for(int i=1;i<=H;++i)
            for(int j=1;j<=W;++j)
                ori[i][j] = (i-1)*W + j - 1 ;
        for(int i=0;i<=H+1;++i)
            G[i][0] = G[i][W+1] = 50000 ;
        for(int i=0;i<=W+1;++i)
            G[0][i] = G[H+1][i] = 50000 ;
        for(int i=1;i<=H;++i)
            for(int j=1;j<=W;++j)
                scanf("%d",&G[i][j]) ;
        for(int i=1;i<=H;++i)
            for(int j=1;j<=W;++j){
                flood(i,j) ;
            }
        /*for(int i=1;i<=H;++i){
            for(int j=1;j<=W;++j){
                printf("%d ",ori[i][j]) ;
            }
            puts("") ;
        }*/
        char c = 'a' ;
        for(int i=0;i<H;++i){
            for(int j=0;j<W;++j){
                if(!out[i][j]){
                    for(int k=0;k<H;++k)
                        for(int l=0;l<W;++l)
                            if(ori[i+1][j+1]==ori[k+1][l+1])
                                out[k][l] = c ;
                    ++c ;
                }
            }
        }
        printf("Case #%d:\n",z) ;
        for(int i=0;i<H;++i){
            printf("%c",out[i][0]) ;
            for(int j=1;j<W;++j)
                printf(" %c",out[i][j]) ;
            puts("") ;
        }
    }
	return 0 ;
}
