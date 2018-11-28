#include<iostream>
#include<set>
#include<sstream>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<utility>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<string, int> PSI;

#define CLEAR(t) memset((t),0,sizeof(t))
#define CLEARW(t,b) memset((t),b,sizeof(t))
#define FOR(i,a,b) for (int i=(int)(a),_t=int(b); i<=_t; i++)
#define FORD(i,a,b) for (int i=(int)(a),_t=int(b); i>=_t; i--)
#define REP(i,n) for (int i=0,_t=int(n); i<_t; i++)
#define sz size()
#define REPS(i,a) REP(i,a.sz)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(All(v))
#define pb push_back
#define strs stringstream
#define outp(k) cout<<k<<endl
#define outp2(k,k1) cout<<k<<" "<<k1<<endl

#define parseIntf int parseInt(string k){ strs inp(k); int ans=0; inp>>ans; return ans; }
#define parseDoublef double parseDouble(string k) { strs inp(k); double ans=0.0; inp>>ans; return ans;}
#define doubleFormatf string doubleFormat(double d) { char st[10]; sprintf(st,"%09.4f",d); string s(st); return s; }
