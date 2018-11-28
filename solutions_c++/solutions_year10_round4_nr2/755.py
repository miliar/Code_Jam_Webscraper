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
const string PROBLEM_NAME = "B";
const string SUB_TYPE = "small-attempt0";
int n;
int n2;
int m[10000];
int one;
int ans;
void solve(int lo,int hi){
     bool suc = true;
     forab(i,lo,hi+1)if(m[i]<n) { suc = false; break;}
     if(suc) return ;
     ans ++;
     forab(i,lo,hi+1) m[i]++;
     solve(lo,(lo+hi)/2);
     solve((lo+hi)/2+1,hi);
}
int main(){
    #ifdef READ_FROM_FILE
    freopen((PROBLEM_NAME+"-"+SUB_TYPE+".in").c_str(),"r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int cas; cin>>cas;
    forn(ca,cas) {
       cin>>n;
       n2 = 1<<n;
       forn(i,n2) cin>>m[i];
       forn(i,n){
         int sz = 1<<(n-1-i);
         forn(j,sz) cin>>one;
       }
       ans = 0;
       solve(0,n2-1);
       cout<<"Case #"<<ca+1<<": "; cout<<ans<<endl;
    }
}

