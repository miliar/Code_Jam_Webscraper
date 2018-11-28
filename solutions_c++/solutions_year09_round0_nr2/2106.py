#include <stdio.h>
#include <string.h>
#define N 100
int a[N][N], par[N*N];
char label[N*N];
int dx[4] = {-1,0,0,1};
int dy[4]= {0,-1,1,0};

int find(int x){
  if (par[x]==x)return x;
  return par[x]=find(par[x]);
}

int uni(int x,int y){
  int px = find(x);
  int py = find(y);
  if (px==py){
  
  }else{
    par[px] = par[py];
  }
}

int main(){
  int T;scanf("%d",&T);
  for (int ti=1;ti<=T;ti++){
    int h,w; scanf("%d%d",&h,&w);
    for (int i=0;i<h;i++){
      for (int j=0;j<w;j++){
        scanf("%d",&a[i][j]);
        par[i*w+j]=i*w+j;
      }
    }
    for (int i=0;i<h;i++){
      for (int j=0;j<w;j++){
        int mi = i*w+j;
        for (int k=0;k<4;k++){
          int vx = i+dx[k], vy = j+dy[k];
          if (vx>=0 && vx<h && vy>=0 && vy<w && a[vx][vy]<a[mi/w][mi%w]){
            mi = vx*w+vy;
          }
        }
        uni(i*w+j, mi);
      }
    }

    memset(label,' ',sizeof(label));
    char curr='a';
    for (int i=0;i<h;i++){
      for (int j=0;j<w;j++){
        if (label[find(i*w+j)]==' '){
          label[find(i*w+j)]=curr;
          curr++;
        }
      }
    }

    printf("Case #%d:\n",ti);
    for (int i=0;i<h;i++){
      for (int j=0;j<w;j++){
        printf("%c",label[find(i*w+j)]); 
        if (j==w-1)puts("");
        else printf(" ");
      }
    }

  }

  return 0;
}
