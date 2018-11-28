#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn = 1; cn <= cases; cn++){
    int h, w, d; cin>>h>>w>>d;

    vector<vector<int> > bd(h, vector<int>(w, 0));

    for (int y=0; y<h; y++){
      for (int x=0; x<w; x++){
        char c; cin>>c;
        bd[y][x] = c-'0'+d;
      }
    }

    int ans=0;

    for (int y=0; y<h; y++){
      for (int x=0; x<w; x++){
        for (int k=3; ; k++){
          int cx = x*2+k;
          int cy = y*2+k;
          long long mx = 0, my = 0;
          for (int yy = y; yy<y+k; yy++){
            for (int xx = x; xx<x+k; xx++){
              if (!(yy>=0 && xx>=0 && yy < h && xx < w)){
                  goto _next;
              }
              if (xx == x     && yy == y     ||
                  xx == x+k-1 && yy == y     ||
                  xx == x     && yy == y+k-1 ||
                  xx == x+k-1 && yy == y+k-1 )
                continue;
                  
              int dx = xx*2+1-cx;
              int dy = yy*2+1-cy;
              mx += dx * bd[yy][xx];
              my += dy * bd[yy][xx];
            }
          }
          //cout<<x<<" "<<y<<" "<<k<<": "<<mx<<", "<<my<<endl;
          if (mx == 0 && my == 0){
            ans = max(ans, k);
          }
        }
      _next:;
      }
    }

    cout<<"Case #"<<cn<<": ";

    if (ans>0) cout<<ans<<endl;
    else cout<<"IMPOSSIBLE"<<endl;
  }

  return 0;
}
