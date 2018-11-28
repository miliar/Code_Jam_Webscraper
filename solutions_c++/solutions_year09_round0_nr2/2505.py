#include <iostream>
#include <algorithm>
#define oo 9999999
using namespace std;
int n,m,d[111][111];
int par[111111];
int wuow[111111];

int carimin(int x,int y){
    int arah=0;
    int mins=d[x][y];
    if (mins>d[x-1][y]+1) {arah=1; mins=d[x-1][y]+1;}
    if (mins>d[x][y-1]+2) {arah=2; mins=d[x][y-1]+2;}
    if (mins>d[x][y+1]+3) {arah=3; mins=d[x][y+1]+3;}
    if (mins>d[x+1][y]+4) {arah=4; mins=d[x+1][y]+4;}   
    return arah;
    }
int bapak(int zzz){
    if (zzz!=par[zzz]) par[zzz]=bapak(par[zzz]);
    return par[zzz];
    }    

void merge(int x,int y,int X,int Y){
     int A=bapak(100*x+y);
     int B=bapak(100*X+Y);
     par[A]=B;
     }
void tulis (){
     int ind='a'-0;
     int tmp2;
     for (int i=1;i<=n;i++){
     for (int j=1;j<=m;j++){
     tmp2=bapak(i*100+j);
     if (wuow[tmp2]==0){
                        wuow[tmp2]=ind;
                        ind++;
                        }
     if (j==1)
     printf("%c",(char) wuow[tmp2]); else
     printf(" %c",(char) wuow[tmp2]);
     }
     printf("\n");
     }
     
     }
     
     
void mainkan(){
     for (int i=1;i<=n;i++)
     for (int j=1;j<=m;j++){
         int tmp=carimin(i,j);
         if (tmp!=0) {
                     if (tmp==1) merge(i,j,i-1,j);
                     else
                     if (tmp==2) merge(i,j,i,j-1);
                     else
                     if (tmp==3) merge(i,j,i,j+1);
                     else merge(i,j,i+1,j);
                     }
         }
     
     tulis();
     }

int main(){
    int TC;
    freopen("air.in.txt","r",stdin);
    freopen("air.out","w",stdout);
    
    scanf("%d",&TC);
    for (int iii=1;iii<=TC;iii++){
    printf("Case #%d:\n",iii);
    scanf("%d%d",&n,&m);
    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++){
        scanf("%d",&d[i][j]);
        d[i][j]*=10;
        }
    for (int i=1;i<=(n*110)+m;i++) wuow[i]=0,par[i]=i;
    for (int i=0;i<=n+1;i++)
    d[i][0]=d[i][m+1]=oo;
    
    
    for (int i=0;i<=m+1;i++)
    d[0][i]=d[n+1][i]=oo;
    
    mainkan();
    }
   // system("pause");
    
    }
