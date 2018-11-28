#include <iostream>
#include <map>
using namespace std;
map<pair<int,int>,char> hash;
#define MAX 110
#define INF 20000
int mat[MAX][MAX];
char ans[MAX][MAX],base;
int f[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int H,W;
bool valid(int x,int y) {
  if (x>=0 && x<H && y>=0 && y<W) return true;
  else return false;
}
char basin(int x,int y) {
  if (ans[x][y]!=' ') return ans[x][y];
  int min = INF,minx,miny;
  for (int i = 0;i<4;++i) {
    int tx = x+f[i][0],ty = y+f[i][1];
    if (!valid(tx,ty)) continue;
    if (mat[tx][ty]<min && mat[tx][ty]<mat[x][y]) {
      min = mat[tx][ty];
      minx = tx;
      miny = ty;
    }
  }
  if (min==INF){
    pair<int,int> tmp(x,y);
    if (hash.find(tmp)==hash.end()) {
      hash[tmp] = base;
      ++base;
    }
    ans[x][y] = hash[tmp];
    return ans[x][y];
  } else return ans[x][y] = basin(minx,miny);
}
int main(void) {
  int T;
  freopen("fdin.txt","r",stdin);
  freopen("fdin.out","w",stdout);
  scanf("%d\n",&T);
  for (int i = 1;i<=T;++i){
    hash.clear();
    base = 'a';
    printf("Case #%d:\n",i);
    scanf("%d%d",&H,&W);
    for (int j = 0;j<H;++j)
      for (int k = 0;k<W;++k)
        scanf("%d",&mat[j][k]);
    memset(ans,' ',sizeof(ans));
    for (int j = 0;j<H;++j) {
      for (int k = 0;k<W;++k){
        if (ans[j][k]==' ')
          ans[j][k] = basin(j,k);
      }
    }
    for (int j = 0;j<H;++j){
      for (int k = 0;k<W;++k){
        putchar(ans[j][k]);
        if (k!=W-1) putchar(' ');
      }
      putchar('\n');
    }
  }
  return 0;
}