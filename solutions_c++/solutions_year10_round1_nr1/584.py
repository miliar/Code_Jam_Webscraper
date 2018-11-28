/*
    2010  Round 1A -
    Rotate
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
using namespace std ;

    int T, N, K;
    char tab[51][51], data[51][51], conv[51][51];
    bool blue, red;

bool check(int i, int j, int dx, int dy, char c){
    for(int z=0;z<K;++z){
        if(i>=N || i<0 || j>=N || j<0) return false;
        if(conv[i][j] != c) return false;
        i += dx;
        j += dy;
    }
    return true;
}

int main(){
    scanf("%d",&T);
    for(int z=1;z<=T;++z){
        scanf("%d %d",&N,&K);
        memset(data,0,sizeof(data));
        blue = red = false;
        for(int i=0;i<N;++i)
            scanf("%s",tab[i]);
        for(int i=0;i<N;++i)
            for(int j=0;j<N;++j)
                if(tab[i][j]!='.') data[i][j] = tab[i][j];
        for(int i=0;i<N;++i)
            for(int j=0;j<N;++j)
                conv[i][j] = data[N-1-j][i];

        //gravity
        for(int i=N-1;i>0;--i)
            for(int j=0;j<N;++j)
                if(conv[i][j]=='\0' && conv[i-1][j]!='\0'){
                    conv[i][j] = conv[i-1][j];
                    conv[i-1][j] = '\0';
                    if(i<N-1){
                        ++i;
                        --j;
                    }
                }

        for(int i=0;i<N;++i)
            for(int j=0;j<N;++j){
                if(check(i,j,0,1,'B') || check(i,j,1,0,'B') ||
                   check(i,j,1,1,'B') || check(i,j,1,-1,'B')) blue = true;
                if(check(i,j,0,1,'R') || check(i,j,1,0,'R') ||
                   check(i,j,1,1,'R') || check(i,j,1,-1,'R')) red = true;
            }

/*
        for(int i=0;i<N;++i){
            for(int j=0;j<N;++j)
                if(conv[i][j]!='\0') printf("%c",conv[i][j]);
                else printf(".");
            puts("");
        }
*/
        if(!blue && !red)
            printf("Case #%d: Neither\n",z);
        else if(blue && red)
            printf("Case #%d: Both\n",z);
        else if(blue)
            printf("Case #%d: Blue\n",z);
        else if(red)
            printf("Case #%d: Red\n",z);
    }
	return 0 ;
}
