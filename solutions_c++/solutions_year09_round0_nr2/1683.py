#include <iostream>
#include <vector>
using namespace std;

const int MAX = 0x7ffffff;
vector< vector<int> > alti;
vector< vector<int> > label;

void init(int H, int W)
{
  int k = 0;
  for( int i = 1 ; i <= H ; ++i ) {
    for( int j = 1 ; j <= W ; ++j ) {
      cin >> alti[i][j];
      label[i][j] = k++;
    }
    alti[i][0] = alti[i][W+1] = MAX;
    label[i][0] = label[i][W+1] = MAX;
  }
  for( int j = 0 ; j <= W+1 ; ++j ) {
    alti[0][j] = alti[H+1][j] = MAX;
    label[0][j] = label[H+1][j] = MAX;
  }
}

void fill(int y, int x, int from, int to)
{
  static const int dx[] = {0, -1, 1, 0};
  static const int dy[] = {-1, 0, 0, 1};

  //cout << "fill(" << y << "," << x << "," << from << "," << to << ")\n";
  label[y][x] = to;
  for( int i = 0 ; i < 4 ; ++i ) {
    int yy = y + dy[i], xx = x + dx[i];
    if( label[yy][xx] == from ) {
      //cout << "Found lable[" << yy << "][" << xx << "] == " << from << "\n";
      fill(yy, xx, from, to);
    }
  }
}

void solve(int H, int W)
{
  const int dx[] = {0, -1, 1, 0};
  const int dy[] = {-1, 0, 0, 1};

  for( int y = 1 ; y <= H ; ++y ) {
    for( int x = 1 ; x <= W ; ++x ) {
      int low = MAX - 1, vlow = -1;
      for( int i = 0 ; i < 4 ; ++i ) {
        int yy = y + dy[i], xx = x + dx[i];
        if( alti[yy][xx] < low ) {
          vlow = i;
          low = alti[yy][xx];
        }
      }
      int yy = y + dy[vlow], xx = x + dx[vlow];
      if( low < alti[y][x] ) {
        fill(y, x, label[y][x], label[yy][xx]);
      }
    }
  }
}

void sink(int H, int W)
{
  vector<char> snk(H*W, '*');
  char basin = 'a';
  for( int i = 1 ; i <= H ; ++i ) {
    for( int j = 1 ; j <= W ; ++j ) {
      int lbl = label[i][j];
      if( snk[lbl] == '*' ) {
        snk[lbl] = basin++;
      }
      if( j != 1 ) cout << " ";
      cout << snk[lbl];
    }
    cout << "\n";
  }
}

int main(void)
{
  alti.resize(102);
  label.resize(102);
  for( int i = 0 ; i < alti.size() ; ++i ) {
    alti[i].resize(102);
    label[i].resize(102);
  }

  int T;
  cin >> T;
  for( int ca = 1 ; ca <= T ; ++ca ) {
    cout << "Case #" << ca << ":\n";
    int H, W;
    cin >> H >> W;
    init(H, W);
    solve(H, W);
    sink(H, W);
  }
}
