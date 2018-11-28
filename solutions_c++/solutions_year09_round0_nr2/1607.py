#include <iostream>
#include <map>
#include <vector>
using namespace std;


struct UnionFind {
  vector<int> data;
  UnionFind(int size) : data(size, -1) { }
  bool link(int x, int y) { 
    x = root(x); y = root(y);
    if (x != y) {
      if (data[y] < data[x]) swap(x, y);
      data[x] += data[y]; data[y] = x;
    }
    return x != y;
  }
  bool isSameGroup(int x, int y) { 
    return root(x) == root(y);
  }
  int root(int x) { 
    return data[x] < 0 ? x : data[x] = root(data[x]);
  }
  int size(int x) { 
    return -data[root(x)];
  }
};

int T,H,W;
int di[]={-1,0,0,1};
int dj[]={0,-1,1,0};
int table[100][100];

bool valid(int i,int j){
  return (0<= i && i<H &&
          0<= j && j<W);
}

int main(){
  cin >> T;
  for (int ii=0;ii<T;ii++){
    cin >> H >> W;
    UnionFind uf(H*W+1);
    for (int i=0;i<H;i++){
      for (int j=0;j<W;j++){
        scanf("%d",&table[i][j]);
      }
    }
    for (int i=0;i<H;i++){
      for (int j=0;j<W;j++){
        int m=1<<20;
        for (int k=0;k<4;k++){
          int ni=i+di[k];
          int nj=j+dj[k];
          if (valid(ni,nj)) m = min(m,table[ni][nj]);
        }
        if (m < table[i][j])
          for (int k=0;k<4;k++){
            int ni=i+di[k];
            int nj=j+dj[k];
            if (valid(ni,nj) && table[ni][nj]==m){
              uf.link(i*W+j,ni*W+nj);
              break;
            }
          }
      }
    }
    printf("Case #%d:\n",ii+1);
    map<int,char> itoc;;
    char c = 'a';
    for (int i=0;i<H;i++){
      for (int j=0;j<W;j++){
        if (j!=0) putchar(' ');
        int d = uf.root(i*W+j);
        if (itoc.find(d) == itoc.end()){
          itoc[d] = c;
          c++;
        }
        putchar(itoc[uf.root(i*W+j)]);
      }putchar('\n');
    }
  }
}
