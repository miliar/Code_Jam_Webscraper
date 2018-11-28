#include <cstdio>
#define maxint 1000000
using namespace std;

void getand(int,int);
void getor(int,int);
int opt[30010][2],a[30010],v[30010],tot,m,req;

int main(){
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d%d",&m,&req);
        for (int i=1;i<=(m-1)/2;++i) scanf("%d%d",&a[i],&v[i]);
        for (int i=(m+1)/2;i<=m;++i){
            scanf("%d",&a[i]);
            opt[i][a[i]]=0;
            opt[i][1-a[i]]=maxint;
        }
        for (int i=(m-1)/2;i>0;--i){
            opt[i][0]=opt[i][1]=maxint;
            if (a[i]) getand(i,0);
            else getor(i,0);
            if (v[i]){
                if (a[i]) getor(i,1);
                else getand(i,1);
            }
        }
        if (opt[1][req]==maxint) printf("Case #%d: IMPOSSIBLE\n",cases+1);
        else printf("Case #%d: %d\n",cases+1,opt[1][req]);
    }
    return 0;
}

void getand(int x,int delta){
    int left=x*2,right=left+1;
    if (opt[left][0]+opt[right][0]+delta<opt[x][0]) opt[x][0]=opt[left][0]+opt[right][0]+delta;
    if (opt[left][1]+opt[right][0]+delta<opt[x][0]) opt[x][0]=opt[left][1]+opt[right][0]+delta;
    if (opt[left][0]+opt[right][1]+delta<opt[x][0]) opt[x][0]=opt[left][0]+opt[right][1]+delta;
    if (opt[left][1]+opt[right][1]+delta<opt[x][1]) opt[x][1]=opt[left][1]+opt[right][1]+delta;
}

void getor(int x,int delta){
    int left=x*2,right=left+1;
    if (opt[left][0]+opt[right][0]+delta<opt[x][0]) opt[x][0]=opt[left][0]+opt[right][0]+delta;
    if (opt[left][1]+opt[right][0]+delta<opt[x][1]) opt[x][1]=opt[left][1]+opt[right][0]+delta;
    if (opt[left][0]+opt[right][1]+delta<opt[x][1]) opt[x][1]=opt[left][0]+opt[right][1]+delta;
    if (opt[left][1]+opt[right][1]+delta<opt[x][1]) opt[x][1]=opt[left][1]+opt[right][1]+delta;
}
