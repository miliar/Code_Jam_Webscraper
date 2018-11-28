#include <iostream>
using namespace std;
//const
const int hx[4]={-1,0,0,1};
const int hy[4]={0,-1,1,0};
const int oo=100000, maxn=111;
//var
int m,n,a[maxn][maxn],kt[maxn][maxn],cnt;
char check[30];

void nhap(void) {
     scanf("%d%d\n",&m,&n);
     int i,j;
     char ch;
     for (i=1;i<=m;i++) {
         for (j=1;j<=n;j++) scanf("%d",&a[i][j]);
         scanf("\n");
     };
     cnt=0;
     memset(kt,0,sizeof(kt));
     memset(check,false,sizeof(check));
     for (i=1;i<=m;i++) {
         a[i][0]=oo;
         a[i][n+1]=oo;
     };
     
     for (i=1;i<=n;i++) {
         a[0][i]=oo;
         a[m+1][i]=oo;
     };
};

void duyet(int x, int y) {
     int i,u,v,getmin=oo,h;
     for (i=0;i<=3;i++) {
         u=x+hx[i];
         v=y+hy[i];
         if (a[u][v]<getmin) {
            getmin=a[u][v];
            h=i;
         };
     };
     if (getmin>=a[x][y]) {
        cnt++;
        kt[x][y]=cnt;
     }
     else {
          u=x+hx[h];
          v=y+hy[h];
          if (kt[u][v]==0) duyet(u,v);
          kt[x][y]=kt[u][v];
     };
};

int xuli(void) {
    nhap();
    int i,j;
    for (i=1;i<=m;i++)
        for (j=1;j<=n;j++)
            if (kt[i][j]==0) 
               duyet(i,j);
            
    for (i=1;i<=26;i++) check[i]=';';
    char ch;
    ch=char('a'-1);
    for (i=1;i<=m;i++)
        for (j=1;j<=n;j++) {
            if (check[kt[i][j]]!=';') printf("%c ",check[kt[i][j]]);
            else {
                 ch++;
                 printf("%c ",ch);
                 check[kt[i][j]]=ch;
            };
            if (j==n) printf("\n"); else printf(" ");
        };
};

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i;
    scanf("%d",&t);
    for (i=1;i<=t;i++) {
        printf("Case #%d:\n",i);
        xuli();
    };
    return 0;
};
