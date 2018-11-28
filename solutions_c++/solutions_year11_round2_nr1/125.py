#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>
 
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<climits>
 
#define oo            (int)13e7
#define s(n)          scanf("%d",&n)
#define sl(n)         scanf("%lld",&n)
#define sf(n)         scanf("%lf",&n)
#define fill(a,v)     memset(a, v, sizeof a)
#define ull           unsigned long long
#define ll            long long
#define bitcount      __builtin_popcount
#define all(x)        x.begin(), x.end()
#define pb( z )       push_back( z )
#define gcd           __gcd
using namespace std;

int n;
char a[128][128];

int wins[128];
int total[128];
double owp[128];
double score[128];
int main(int argc, char** argv) {
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
  //freopen("A-small-attempt1.in", stdin, "r"); freopen("A-small-attempt1.out", stdout, "w");
  //freopen("A-small-attempt2.in", stdin, "r"); freopen("A-small-attempt2.out", stdout, "w");
  
  freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
  
  
  int runs;
  s(runs);
  for (int T=1; T <= runs; T++) {
    s(n);
    for (int i=0; i < n; i++) scanf("%s", a[i]);
    
    for (int i=0; i < n; i++) {
      score[i] = 0;
      int &T = total[i];
      int &W = wins[i];
      W = T = 0;
      for (int j=0; j < n; j++) 
      if (isdigit(a[i][j])) {
        T++;
        W += (a[i][j] == '1' ? 1 : 0);
      }
      score[i] += 0.25 * W / (T + 0.);
    }
    for (int i=0; i < n; i++) {
      owp[i] = 0;
      int T = 0;
      for (int j=0; j < n; j++) 
      if (isdigit(a[j][i])) {
        double num = wins[j] - (a[j][i] == '1');
        double den = total[j] - 1;
        owp[i] += num/den;
       // cout << i << " to " << j << " = " << num << "/" << den << endl;
        T++;
      }
      owp[i] /= T;
      //cout << "team " << i <<" -> owp = " << owp[i] << endl;
      score[i] += 0.5 * owp[i] ;
    }
    for (int i=0; i < n; i++) {
      int T = 0;
      double oowp = 0;
      for (int j=0; j < n; j++)
      if (isdigit(a[i][j])) {
        oowp += owp[j];
        T++;
      }
      oowp /= T;
      score[i] += oowp * 0.25;
    }
    printf("Case #%d:\n", T);
    for (int i=0; i < n; i++) {
      printf("%.10lf\n", score[i]);
    }
  }
  
	return 0;
}
