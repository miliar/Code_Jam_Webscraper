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

#define TEST_NAME "C-large"

const int maxN=500;
const int modulo=100003;

int binomial[maxN+1][maxN+1];
int cnt[maxN+1][maxN+1];

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
     
     for(int n=0;n<=maxN;++n) {
          binomial[n][0]=binomial[n][n]=1;
          for(int k=1;k<n;++k)
               binomial[n][k]=(binomial[n-1][k]+binomial[n-1][k-1])%modulo;
     }
          cnt[1][0]=1;
          for(int i=2;i<=500;++i) 
               for(int j=0;j<i;++j) { 
                    cnt[i][j]=0;
                    for(int k=0;k<j;++k) 
                         cnt[i][j]=(cnt[i][j]+cnt[j][k]*(long long)binomial[i-j-1][j-k-1])%modulo;
               }
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int n;
          cin>>n;               
          int res=0;
          REP(i,n)res=(res+cnt[n][i])%modulo;
          cout<<"Case #"<<test<<": "<<res<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
