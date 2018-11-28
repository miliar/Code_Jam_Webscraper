
#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

int T, W, H;
int A[110][110];
char res[110][110];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

vector<int> gx[110][110], gy[110][110];

void df( int x, int y, char at ) {
  if ( res[x][y] != -1 )
    return;
  if ( A[x][y] > 10000 )
    return;
  res[x][y] = at;
  for ( int k = 0; k < gx[x][y].size(); ++k )
    df( gx[x][y][k], gy[x][y][k], at);    
}

int main() {
  freopen("B-large.in", "r", stdin);  
  freopen("B-large.out", "w", stdout);

  scanf("%d", &T);
  
  for ( int i = 1; i <= T; ++i ) {
    char at = 'a';
  
    scanf("%d %d", &W, &H);
    for ( int a = 0; a <= W + 1; ++a )
      for ( int b = 0; b <= H + 1; ++b ) {
        A[a][b] = 10001;
        gx[a][b].clear();
        gy[a][b].clear();
      }
        
    for ( int a = 1; a <= W; ++a )
      for ( int b = 1; b <= H; ++b ) {
        scanf("%d", A[a] + b);
      }

    memset( res, -1, sizeof( res ) );

    for ( int a = 1; a <= W; ++a )
      for ( int b = 1; b <= H; ++b ) {
        bool bSink = true;
        int tx = -1, ty = -1;
      
        for ( int r = 0; r < 4; ++r ) {
          int nx = a + dx[r];
          int ny = b + dy[r];
          
          if ( ( tx == -1 || A[nx][ny] < A[tx][ty] ) && A[nx][ny] < A[a][b] ) {
            tx = nx, ty = ny;
            
            bSink = false;
            //break;
          } 
        }
        
        //printf("(%d, %d)\n", a, b);
        //fflush( stdout );
        
        if ( bSink ) {
/*
          for ( int r = 0; r < 4; ++r ) {
            int nx = a + dx[r];
            int ny = b + dy[r];
          
            if ( A[nx][ny] == A[a][b] ) {
              gx[a][b].push_back(nx),
              gy[a][b].push_back(ny);
              gx[nx][ny].push_back(a),
              gy[nx][ny].push_back(b);
            } 
          }
*/
        } else {
          gx[a][b].push_back(tx),
          gy[a][b].push_back(ty);
          gx[tx][ty].push_back(a),
          gy[tx][ty].push_back(b);
        }
      }
      
    for ( int a = 1; a <= W; ++a )
      for ( int b = 1; b <= H; ++b ) {
        if ( res[a][b] == -1 ) {
          df( a, b, at);
          ++at;
        }
      }
      
    printf("Case #%d:\n", i);
    for ( int a = 1; a <= W; ++a ) {
      printf("%c", res[a][1]);
      for ( int b = 2; b <= H; ++b )
        printf(" %c", res[a][b]);
      printf("\n");
    }
  }

  return 0;
}
