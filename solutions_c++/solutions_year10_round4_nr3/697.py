#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iomanip>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
const double EPS = 1e-12;
const double PI = acos(-1.0);
const int INF  = 0x3f3f3f3f; // 1061109567, 1*10^9
const LL LINF = 0x3f3f3f3f3f3f3f3fLL; //4557430888798830399, 4*10^18
#define ST(x,b)  memset(x,b,sizeof(x))
#define SZ(x) ((int)(x).size())
#define forn(i,n) for(__typeof(n) i=0;i<n;i++)
#define forab(i,a,b) for(__typeof(a) i=a;i<b;i++)
#define foreach(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();it++)
template<class T>string toString(T s){ostringstream ost;ost<<s;return ost.str();}
template<class T>LL toLL(T s){stringstream st; st<<s; LL ret; st>>ret; return ret;}
template<class T>int toInt(T s){stringstream st; st<<s; int ret; st>>ret; return ret;}

#define READ_FROM_FILE
const string PROBLEM_NAME = "C";
const string SUB_TYPE = "small-attempt0";

char g[210][210];
bool check(){
     forn(i,210) forn(j,210) if(g[i][j]) return true;
     return false;
}
int main(){
    #ifdef READ_FROM_FILE
    freopen((PROBLEM_NAME+"-"+SUB_TYPE+".in").c_str(),"r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int cas; cin>>cas;
    forn(ca,cas) {
       ST(g,0);
       int k; cin>>k;
       forn(i,k){
          int x1,y1,x2,y2; cin>>x1>>y1>>x2>>y2;
          forab(r,x1,x2+1) forab(c,y1,y2+1) g[r][c] = 1;
       }
       int ans = 0;
       while(check()){
            for(int r=210-1;r>=0;r--)
              for(int c=210-1;c>=0;c--)
                  if(r==0 || c == 0) g[r][c] = 0;
                  else if( g[r][c] == 0 && g[r-1][c] && g[r][c-1]) g[r][c] = 1;
                  else if(g[r-1][c]==0 && g[r][c-1] ==0 ) g[r][c] = 0;
            ans ++;
       }
       
       cout<<"Case #"<<ca+1<<": "; cout<<ans<<endl; 
    }
}

