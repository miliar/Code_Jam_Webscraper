#include<iostream>
#include<vector>
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
  int root(int x) { // ‘ã•\Œ³‚ð•Ô‚·
    return data[x] < 0 ? x : data[x] = root(data[x]);
  }
  int size(int x) {
    return -data[root(x)];
  }
};

int X, Y;

int Encode(int x, int y) {
  return x * Y + y;
}

int table[128][128];

int main(){
  int T; cin >> T;
  for(int tno = 0; tno < T; tno++){
    printf("Case #%d:\n", tno + 1);

    cin >> X >> Y;
    for(int i = 0; i < X; i++)
      for(int j = 0; j < Y; j++)
        cin >> table[i][j];

    UnionFind uf(X*Y);

    const int dx[] = {-1, 0, 0, 1};
    const int dy[] = {0, -1, 1, 0};
    for(int i = 0; i < X; i++){
      for(int j = 0; j < Y; j++){

        int index = -1;

        for(int k = 0; k < 4; k++){
          int nx = i + dx[k];
          int ny = j + dy[k];
          if( 0 <= nx && nx < X && 0 <= ny && ny < Y ) {
            if( table[i][j] > table[nx][ny] ) {
              if( index == -1 ||
                  ( table[nx][ny] < table[i + dx[index]][j + dy[index]] ) ){
                index = k;
              }
            }
          }
        }

        if( index != -1 ) {
          uf.link( Encode(i + dx[index], j + dy[index]), Encode(i, j) );
        }
      }
    }

    int mark[X][Y];    
    for(int i = 0; i < X; i++){
      for(int j = 0; j < Y; j++){
        mark[i][j] = uf.root( Encode(i, j) );
      }
    }

    int n2c[X*Y]; memset(n2c, -1, sizeof(n2c));
    int p = 0;
    char ans[X][Y];
    for(int i = 0; i < X; i++){
      for(int j = 0; j < Y; j++){
        if( n2c[ mark[i][j] ] == -1 ) n2c[ mark[i][j] ] = 'a' + p++;
        ans[i][j] = n2c[mark[i][j]];
      }
    }

    for(int i = 0; i < X; i++){
      for(int j = 0; j < Y; j++){
        if( j == Y - 1 )
          cout << ans[i][j] << endl;
        else
          cout << ans[i][j] << " ";
      }
    }
  }
}

