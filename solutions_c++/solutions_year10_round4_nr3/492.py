#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<map>
#include<set>
#include<ctime>
#include<vector>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int a[200][200],b[200][200];
int nn,mm;
int n;
void init(){
    memset(a,0,sizeof(a));
    scanf("%d",&n);
    nn=0;
    mm=0;
    fo(i,1,n){
        int x1,y1,x2,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        if (x2>nn)nn=x2;
        if (y2>mm)mm=y2;
        fo(i,x1,x2)
            fo(j,y1,y2)
                a[i][j]=1;
    }
}
void work(){
    memset(b,0,sizeof(b));
    bool ff;
    ff=1;
    int tot=0;
    while (ff){
        tot++;
        fo(i,1,nn)
            fo(j,1,mm){
                if (a[i][j]==1){
                    if (a[i-1][j]==0 && a[i][j-1]==0)
                     b[i][j]=0;else b[i][j]=1;
                }
                else{
                    if (a[i-1][j]==1 && a[i][j-1]==1)
                    b[i][j]=1;else b[i][j]=0;
                }
            }
        ff=0;
        fo(i,1,nn)
            fo(j,1,mm){
                a[i][j]=b[i][j];
                if (a[i][j]==1)ff=1;
            }
    }
    printf("%d\n",tot);
}
int main(){
    freopen("csm.in","r",stdin);
    freopen("out.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    fo(i,1,ca){
        init();
        printf("Case #%d: ",i);
        work();
    }
	return 0;
}
