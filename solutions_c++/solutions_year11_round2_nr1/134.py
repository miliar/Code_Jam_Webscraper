#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

#define TEST_NAME "A-large"

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int n;
          cin>>n;
          vector<string> res(n);
          vector<double> wp(n);
          vector<double> owp(n);
          vector<double> oowp(n);
          REP(i,n)cin>>res[i];

          // calc wp
          REP(i,n) {
               int w=0,c=0;
               REP(k,n)
                    if(res[i][k]=='1')w++,c++;
                    else if(res[i][k]=='0')c++;
               wp[i]=w/(double)c;
          }
          // calc owp
          REP(i,n) {          
               int cc = 0;
               REP(j,n)
                    if(res[i][j]=='1'||res[i][j]=='0') {
                         int w=0,c=0;
                         REP(k,n)
                              if(k!=i) {
                                   if(res[j][k]=='1')w++,c++;
                                   else if(res[j][k]=='0')c++;
                              }
                         owp[i]+=w/(double)c;               
                         cc++;                         
                    }
               owp[i]/=cc;
          }
          // calc oowp
          REP(i,n) {
               int cc=0;
               REP(j,n)
                    if(res[i][j]=='1'||res[i][j]=='0') {
                         oowp[i]+=owp[j];
                         ++cc;
                    }
               oowp[i]/=cc;                         
          }
          
          cout<<"Case #"<<test<<":"<<endl;
          REP(i,n) {
               cout.setf(ios::fixed);          
               cout.precision(10);
               cout<<0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]<<endl;
          }
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
