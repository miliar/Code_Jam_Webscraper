#include<cstdio>
#include<cstring>

using namespace std;

int I,T,h,w,r,i,j,x,y;
int opt[1000][1000];

main(){
    scanf("%d",&T);
    for (int I=1;I<=T;++I){
        printf("Case #%d: ",I);
        scanf("%d%d%d",&h,&w,&r);
        memset(opt,0,sizeof opt);
        for (i=0;i<r;++i){
            scanf("%d%d",&x,&y);
            opt[x-1][y-1]=-1;
        }
        opt[0][0]=1;
        for (i=0;i<h;++i)
            for (j=0;j<w;++j)
                if (opt[i][j]==0){
                    if (i>1 && j>0)opt[i][j]+=opt[i-2][j-1];
                    if (i>0 && j>1) opt[i][j]+=opt[i-1][j-2];
                    opt[i][j]%=10007;
                }
                else if (opt[i][j]<0) opt[i][j]=0;
        printf("%d\n",opt[h-1][w-1]);
    }
}
