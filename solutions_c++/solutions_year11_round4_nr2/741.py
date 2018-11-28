#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}
#define EPS pow(10.0,-8.0)

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

int main () {
  int test, T;

  cin >> T;
  REP (test, T) {
    //TODO
    int r,c;
    double d;
    int i,j,k;
    cin >> r >> c >> d;
    vector< vector<double> > m(r, vector<double>(c, 0.0));
    REP(i,r){
      REP(j,c){
        double temp;
        char tempc;
        cin >> tempc;
        temp = (double)tempc-'0';
        m[i][j] = temp;
      }
    }
    int maxr = 0;
    //printf("r=%d c=%d\n", r, c);
    REP(i,r-2){
      REP(j,c-2){
        int mlen = min(r-i, c-j);
        int len;
        for(len=3; len<=mlen; len++){
          // calc mass
          double resx=0;
          double resy=0;
          double cx=(double)i+(double)len/2.0F;
          double cy=(double)j+(double)len/2.0F;
          for(int p=i; p<i+len; p++){
            for(int q=j; q<j+len; q++){
              if((p==i&&q==j) || (p==i+len-1&&q==j+len-1) || (p==i&&q==j+len-1) || (p==i+len-1&&q==j)) continue;
              double pcx = (double)p+0.5;
              double pcy = (double)q+0.5;
              double mm = m[p][q] + d;
              resx += mm*(pcx-cx);
              resy += mm*(pcy-cy);
            }
          }
          //printf("##lefttop=(%d %d), len=%d\n", i, j, len);
          //printf("%f %f\n", resx, resy);
          if (abs(resx) < EPS && abs(resy) < EPS){
            // OK
            if(maxr < len){
              maxr = len;
            }
          }
        }
      }
    }
    if(maxr == 0){
      gp("IMPOSSIBLE");
    }else{
      gp(maxr);
    }
  }
  return 0;
}

