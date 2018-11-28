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

const string target="welcome to code jam";
const int modulo=10000;

int main() {
     int n,test;
     string text;
     VVI cnt;
     cin>>n;
     getline(cin,text);//skip newline
     for(test=1;test<=n;++test) {
          getline(cin,text);

          int n1=SZ(text),n2=SZ(target);
          cnt=VVI(n1+2,VI(n2+2,0));
          cnt[0][0]=1;
          REP(i,n1+1)REP(j,n2+1) {
               cnt[i+1][j]=(cnt[i+1][j]+cnt[i][j])%modulo;
               if(i<n1&&j<n2&&text[i]==target[j])cnt[i+1][j+1]=(cnt[i+1][j+1]+cnt[i][j])%modulo;
          }
          printf("Case #%d: %04d\n",test,cnt[n1][n2]);
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
