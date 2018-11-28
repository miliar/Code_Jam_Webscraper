#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

map<char, map<bool, vector<int> > > vect;

bool check(const vector<string> &bd,
           const vector<vector<bool> > &flg)
{
  int h = bd.size();
  int w = bd[0].length();
  vector<vector<bool> > done(h, vector<bool>(w, false));
  for (int y=0; y<h; y++){
    for (int x=0; x<w; x++){
      if (done[y][x]) continue;

      int cx=x, cy=y;
      do{
        done[cy][cx]=true;

        int dx = vect[bd[cy][cx]][flg[cy][cx]][0];
        int dy = vect[bd[cy][cx]][flg[cy][cx]][1];

        cx = (cx + dx + w-1) % w;
        cy = (cy + dy + h-1) % h;

      } while(!done[cy][cx]);

      if (cx!=x || cy!=y)
        return false;
    }
  }
  return true;
}

int main(int argc, char *argv[])
{
  vect['|'][true ].push_back(0);
  vect['|'][true ].push_back(1);
  vect['|'][false].push_back(0);
  vect['|'][false].push_back(-1);

  vect['-'][true ].push_back(1);
  vect['-'][true ].push_back(0);
  vect['-'][false].push_back(-1);
  vect['-'][false].push_back(0);

  vect['/'][true ].push_back(1);
  vect['/'][true ].push_back(-1);
  vect['/'][false].push_back(-1);
  vect['/'][false].push_back(1);

  vect['\\'][true ].push_back(1);
  vect['\\'][true ].push_back(1);
  vect['\\'][false].push_back(-1);
  vect['\\'][false].push_back(-1);

  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int h, w; cin>>h>>w;
    vector<string> bd(h);
    for (int i=0; i<h; i++)
      cin>>bd[i];

    int ans=0;
    int n = h * w;
    vector<vector<bool> > flg(h, vector<bool>(w, false));
    for (int p = 0; p < (1<<n); p++){
      //cout<<p<<endl;
      for (int y=0; y<h; y++){
        for (int x=0; x<w; x++){
          flg[y][x]=((p>>(y*w+x))&1)!=0;
        }
      }
      if (check(bd, flg)){
        ans++;
      }
    }

    cout<<"Case #"<<cn<<": "<<ans<<endl;
  }
  
  return 0;
}
