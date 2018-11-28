#include<iostream>
using namespace std;

const int N = 101;
int pl[N][N];
int deg[N][N];
int H,W;
int a[]={-1,0,0,1};
int b[]={0,-1,1,0};
int c[]={3,2,1,0};
int zn[N][N];
char z[N];

bool polok(int x, int y){
  return x>=1 && x<=H && y>=1 &&y <= W;
}

void searchuj(int x, int y, int znak){
  zn[x][y] = znak;
  for(int i=0;i<4;i++){
    if(polok(x+a[i],y+b[i]) && deg[x+a[i]][y+b[i]]==c[i]){
//      printf("z pola : %d,%d (kierunke : %d), c[kier] = %d, ide do : %d,%d,(DEG : %d)=\n",x,y,i,c[i],x+a[i],y+b[i],deg[x+a[i]][y+b[i]]);
      searchuj(x+a[i],y+b[i],znak);
    }
  }
}

main(){
  int t;
  scanf("%d",&t);
  for(int q=1;q<=t;q++){
    scanf("%d %d",&H,&W);
    for(int i=1;i<=H;i++)
      for(int j=1;j<=W;j++)
        scanf("%d",&pl[i][j]);
    for(int i=1;i<=H;i++){
      for(int j=1;j<=W;j++){
        deg[i][j] = -1; // nie ma zadnych krawedzi
        for(int k=0;k<4;k++)
          if(polok(i+a[k],j+b[k]) && pl[i+a[k]][j+b[k]]<pl[i][j]){
            if(deg[i][j] == -1) deg[i][j] = k;
            else{
              if(pl[i+a[k]][j+b[k]] < pl[i+a[deg[i][j]]][j+b[deg[i][j]]])
                deg[i][j] = k;
            }
          }
//        printf("%d ",deg[i][j]);
      }
//      printf("\n");
    }
    int nr = 0;
    for(int i=0;i<N;i++) z[i] = 100;
    int kt = 0;
    for(int i=1;i<=H;i++){
      for(int j=1;j<=W;j++){
        if(deg[i][j] == -1){
          searchuj(i,j,nr); nr++;
        }
      }
    }
    printf("Case #%d:\n",q);
    for(int i=1;i<=H;i++){
      for(int j=1;j<=W;j++){
        if(z[zn[i][j]] == 100){
          z[zn[i][j]] = kt + 'a';
          kt++;
        }
        printf("%c ",z[zn[i][j]]);
      }
      printf("\n");
    }
  }
}
