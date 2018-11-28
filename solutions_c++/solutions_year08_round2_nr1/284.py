#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<queue>
#include<set>
#include<map>

#define x first
#define y second

#define rep(i,n) for(ll i=0;i<ll(n);i++)

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;

int main() {
   ll N;
   cin >> N;
   for (ll Nc = 1; Nc <= N; Nc++) {
      ll n, A, B, C, D, x0, y0, M;
      cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
      vector<pii> v;
      ll X = x0, Y = y0;
      v.push_back(pii(X,Y));
      for (ll i = 1; i < n; i++) {
         X = (A * X + B) % M;
         Y = (C * Y + D) % M;
         v.push_back(pii(X,Y));
      }
      vector<vector<ll> > w(3,3);
      rep(i,n) w[(v[i].x%3)][v[i].y%3]++;
      ll cnt = 0;
      rep(i1,3) rep(j1,3) rep(i2,3) rep(j2,3) rep(i3,3) rep(j3,3) {
         if ((i1+i2+i3)%3==0 and (j1+j2+j3)%3==0) {
            vector<pii> vp(3);
            vp[0]=pii(i1,j1);
            vp[1]=pii(i2,j2);
            vp[2]=pii(i3,j3);
            if (vp[0] == vp[1] and vp[1] == vp[2]) {
               cnt += w[i1][j1]*(w[i2][j2]-1)*(w[i3][j3]-2);
            }
            else if (vp[0] == vp[1]) {
               cnt += w[i1][j1]*(w[i2][j2]-1)*(w[i3][j3]);
            }
            else if (vp[1] == vp[2]) {
               cnt += w[i1][j1]*(w[i2][j2]-1)*(w[i3][j3]);
            }
            else {
               cnt += w[i1][j1]*w[i2][j2]*(w[i3][j3]);
            }
         }
      }
      cout << "Case #" << Nc << ": " << cnt/6 << endl;
   }
}

