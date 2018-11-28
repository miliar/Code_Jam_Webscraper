#include <stdio.h>
#include <string.h>

#define maxn 5

int R,C;

char m[maxn][maxn];
int in[maxn][maxn];

int dx[128];
int dy[128];

int sol(){
    int i,j,k,z;
    char b;
    int ni,nj,flag,e;
    int ret = 0;
    scanf("%d%d",&R,&C);
    for (i=0;i<R;i++) scanf("%s",m[i]);
    for (k=(1<<(R*C))-1;k>=0;k--){
        memset(in,0,sizeof(in));
        flag=1;
        for (i=0;i<R&&flag;i++) for (j=0;j<C&&flag;j++){
            b = m[i][j];
            e = i*C+j;
            if (k&(1<<e)){
                ni=(i+dx[b]+R)%R;
                nj=(j+dy[b]+C)%C;
            }else{
                ni=(i-dx[b]+R)%R;
                nj=(j-dy[b]+C)%C;
            }
            in[ni][nj]++;
            if (in[ni][nj]>1) flag=0;
        }
        ret+=flag;
    }
    return ret;
}

int main(){
    int c,cas;
    dx['|']=1; dy['|']=0;
    dx['-']=0; dy['-']=1;
    dx['/']=1; dy['/']=-1;
    dx['\\']=1; dy['\\'] =1;

    scanf("%d",&c);
    for (cas=1;cas<=c;cas++)
        printf("Case #%d: %d\n", cas,sol());
    return 0;
}

