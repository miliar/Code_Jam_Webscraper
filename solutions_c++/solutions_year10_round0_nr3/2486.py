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
#define STINF(x) memset(x,0x3f,sizeof(x))
#define CLR(x) (x).clear()
#define SZ(x) ((int)(x).size())
#define MP(a,b) make_pair((a),(b))
#define ALL(x) (x).begin(),(x).end()
#define PB(a) push_back(a)
#define X     first
#define Y     second
#define forn(i,n) for(typeof(n) i=0;i<n;i++)
#define forab(i,a,b) for(typeof(a) i=a;i<b;i++)
#define foreach(it,c) for(typeof(bg(c)) it=bg(c);it!=ed(c);it++)
template<class T>string toString(T s){ostringstream ost;ost<<s;return ost.str();}
template<class T>LL toLL(T s){stringstream st; st<<s; LL ret; st>>ret; return ret;}
template<class T>int toInt(T s){stringstream st; st<<s; int ret; st>>ret; return ret;}

#define READ_FROM_FILE
const string PROBLEM_NAME = "C";
const string SUB_TYPE = "small-attempt0";

map<int,PII> memo;  
int r,k,n;
LL g[1100];
int visit[1100];
LL  money[1100];

LL doit(int &p) {
   LL cnt = 0;
   int ext = p;
   while(cnt+g[p] <= k){
        cnt += g[p];
        p = (p+1)%n;
        if(p == ext) break;
   }
   return cnt;
}
int main(){
    #ifdef READ_FROM_FILE
    freopen((PROBLEM_NAME+"-"+SUB_TYPE+".in").c_str(),"r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int cas; cin>>cas;
    forn(ca,cas) {
       
       ST(visit,-1);
       scanf("%d%d%d",&r,&k,&n);
       forn(i,n) scanf("%d",&g[i]);
       
       visit[0] = 0; money[0]=0;
       int p = 0;
       LL totMoney = 0, rr = 0;
       while(1) {
          totMoney += doit(p); 
         // cout<<totMoney<<endl;
          rr ++;
          if(rr == r) break;
          
          if(visit[p]==-1){
             visit[p] = rr;
             money[p] = totMoney;
             continue;
          }
          int lastTime = visit[p], lastMoney = money[p]; 
          int loopSz = (r-rr)/(rr-lastTime), leftSz = r - (rr + loopSz*(rr-lastTime));
          totMoney += loopSz*(totMoney-lastMoney);
          forn(i,leftSz) totMoney += doit(p);
          break;
       }
       
       cout<<"Case #"<<ca+1<<": ";  cout<<totMoney<<endl;
    }
}

