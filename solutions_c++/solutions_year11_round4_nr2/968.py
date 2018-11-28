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

const int maxRC=600;

int w[maxRC][maxRC];
ll sumr[maxRC][maxRC];
ll sumc[maxRC][maxRC];
ll sum[maxRC][maxRC];

PII corn[4]={PII(0,0),PII(0,1),PII(1,0),PII(1,1)};

inline ll gets(ll s[maxRC][maxRC],int i1,int j1,int i2,int j2) {
     ll res = s[i2][j2];
     if(i1>0)res-=s[i1-1][j2];
     if(j1>0)res-=s[i2][j1-1];
     if(i1>0&&j1>0)res+=s[i1-1][j1-1];
     return res;
}

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int r,c,d;
          string str;
          int ans = 0;
          cin>>r>>c>>d;
          d=0;
          REP(i,r) {
               cin>>str;
               REP(j,c)w[i][j]=d+str[j]-'0';
          }
          REP(i,r)REP(j,c) {
               sumr[i][j]=w[i][j]*i;
               sumc[i][j]=w[i][j]*j;
               sum[i][j] =w[i][j];
               if(i>0) {
                    sumr[i][j]+=sumr[i-1][j];
                    sumc[i][j]+=sumc[i-1][j];
                    sum [i][j]+=sum [i-1][j];
               }
               if(j>0) {
                    sumr[i][j]+=sumr[i][j-1];
                    sumc[i][j]+=sumc[i][j-1];
                    sum [i][j]+=sum [i][j-1];
               }
               if(i>0&&j>0) {
                    sumr[i][j]-=sumr[i-1][j-1];
                    sumc[i][j]-=sumc[i-1][j-1];
                    sum [i][j]-=sum [i-1][j-1];
               }
          }

          ll sr,sc, s;
          int k;
          int i1,j1;
          REP(i,r)REP(j,c) {
               for(k=3;i+k<=r&&j+k<=c;++k) {
                    sr=gets(sumr,i,j, i+k-1,j+k-1);
                    sc=gets(sumc,i,j, i+k-1,j+k-1);
                    s =gets(sum ,i,j, i+k-1,j+k-1);
                    REP(d,4) {
                         i1=i+(k-1)*corn[d].X;
                         j1=j+(k-1)*corn[d].Y;
                         sr-=w[i1][j1]*i1;
                         sc-=w[i1][j1]*j1;
                         s -=w[i1][j1];
                    }
//                     if(i==1&&j==1) {
//                          cerr<<"k="<<k<<" s="<<s<<" sr="<<sr<<" sc="<<sc<<endl;
//                     }
                    if(2*sr==(2*i+k-1)*s && 2*sc==(2*j+k-1)*s) 
                         ans=max(ans,k);                    
               }               
          }

          printf("Case #%d: ",test);
          if(ans<3)printf("IMPOSSIBLE\n");
          else printf("%d\n",ans);
     }
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
