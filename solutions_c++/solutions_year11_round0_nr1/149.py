#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long i64;
typedef vector<int> VI;
typedef vector<string> VS;
#define REP(i,n) for(int _n=n, i=0;i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define PB push_back

int n, P[100], F[100];
string C[100];

int main() {
  int Ts;
  cin>>Ts;
  FOR(cs, 1, Ts) {
    cin>>n;
    REP(i,n) {cin>>C[i]>>P[i];F[i]=P[i];}
    bool fg=true;
    while(fg) {
      fg=false;
      REP(i,n) FOR(j,i+1,n-1) {
        if (F[j]<=F[i]) {
          F[j]=F[i]+1; fg=true;
        }
        if (C[i]==C[j]) {
          int d=std::abs(P[i]-P[j]);
          if(F[j]<F[i]+d+1) {
            F[j]=F[i]+d+1; fg=true;
          }
        }
      }
    }
    cout << "Case #" << cs << ": " << F[n-1]<<endl;
  }
  return 0;
}
