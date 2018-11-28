#include<cstdio>
#include<cstring>
#define KK 7000
#define K 3500

using namespace std;

const int fx[4]={0,1,0,-1};
const int fy[4]={1,0,-1,0};

class {
    public:
        int mi,ma;
        bool cz;
        void clear(){cz=false;}
        void set(int k){if (!cz) mi=k,ma=k,cz=1;else mi<?=k,ma>?=k;}
}xxl[KK],yxl[KK];

int map[KK][KK];
int I,T,i,x,y,dir,j,are,n,o,tot;
char str[10000];
main(){
    for (I=1,scanf("%d",&T);I<=T;++I){
        scanf("%d",&n);
        printf("Case #%d: ",I);
        memset(map,0,sizeof map);
        x=K;y=K;dir=0;
        for (i=0;i<KK;++i) yxl[i].clear(),xxl[i].clear();
        are=0;tot=0;
        for (i=0;i<n;++i){
            scanf("%s %d",str,&o);
            while (o--){
                for (j=0;str[j];++j){
                    if (str[j]=='F') {
                        are+=(x-K)*fy[dir]-(y-K)*fx[dir];
                        if (dir==2) yxl[y-1].set(x),--y;
                        else if (dir==0) yxl[y].set(x),++y;
                        else if (dir==1) xxl[x].set(y),++x;
                        else if (dir==3) xxl[x-1].set(y),--x;
                        
                    }
                    else if (str[j]=='R') (++dir)%=4;
                    else if (str[j]=='L') (dir+=3)%=4;
                }
            }
        }
        if (are<0) are=-are;
        for (i=0;i<KK;++i){
            if (xxl[i].cz)
                for (j=xxl[i].mi;j<xxl[i].ma;++j)
                    map[i][j]=1;
            if (yxl[i].cz)
                for (j=yxl[i].mi;j<yxl[i].ma;++j)
                    map[j][i]=1;
        }
        for (i=0;i<KK;++i)
            for (j=0;j<KK;++j)
                if (map[i][j])
                    ++ tot;
        printf("%d\n",tot-are/2);
    }
}
