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

#define TEST_NAME "B-large"

vector<string> combine;
vector<string> oppose;

vector<char> magic;

void transform() {
     bool found = true;
     int n;
     do {
          found=false;
          n=SZ(magic);
          if(n<2)break;
          REP(k,SZ(combine)) 
               if(combine[k][0]==magic[n-1]&&combine[k][1]==magic[n-2] ||
                  combine[k][0]==magic[n-2]&&combine[k][1]==magic[n-1]) {
                    found=true;
                    magic.pop_back();
                    magic.pop_back();
                    magic.push_back(combine[k][2]);
                    break;
               }               
     }while(found);
     bool present[256]={0};
     n=SZ(magic);
     REP(i,n)present[magic[i]]=true;
     REP(k,SZ(oppose))
          if(present[oppose[k][0]]&&present[oppose[k][1]]) {
               magic.clear();
               break;
          }
}

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int c,d,n;
          string str;
          cin>>c;
          combine.resize(c);
          REP(i,c)cin>>combine[i];
          cin>>d;
          oppose.resize(d);
          REP(i,d)cin>>oppose[i];
          cin>>n>>str;
          magic.clear();
          REP(i,n) {
               magic.pb(str[i]);
               transform();
          }
          cout<<"Case #"<<test<<": [";
          REP(i,SZ(magic)) {
               if(i)cout<<", ";
               cout<<magic[i];
          }
          cout<<"]"<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
