/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

#define LET(x,a) __typeof(a) x (a)
#define ITER(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOREACH(it,v) ITER(it,v.begin(),v.end())

#define FILLA(a,x) memset(&a,x,sizeof(a))
#define FILL(a,x) memset(a,x,sizeof(a))
#define CLEARA(a,x) FILLA(a,0)
#define CLEAR(a) FILL(a,0)

#define m_p make_pair
#define fst first
#define snd second
typedef pair<int,int> PII;
typedef long long ll;
template<class T> void check_max( T&a, T b ){ if ( a < b ) a = b; }
template<class T> void check_min( T&a, T b ){ if ( a > b ) a = b; }

//#define debug
const int MAXN = 410;
bool g[MAXN][MAXN];
vector<int> e[MAXN];
int n;


vector<int> d;

vector<bool> conq, threat;

int min_threat;
void dfs( int i ){
	if ( threat[1] ){
		int t_threat = 0;
		REP(j,0,n)if(!conq[j]&&threat[j])
			t_threat++;
		check_max( min_threat, t_threat );
		return;
	}
	vector<bool> b_conq = conq;
	vector<bool> b_threat = threat;
	
	REP(x,0,e[i].size()){
		int j = e[i][x];
		if ( d[j] < d[1] && d[j] == d[i]+1 ){
			conq[j] = true;
			REP(xx,0,e[j].size())
				threat[e[j][xx]] = true;
			dfs(j);
			conq = b_conq;
			threat = b_threat;
		}
	}
}

int main(){
	int T;
	scanf("%d",&T);
	REP(Case,1,T+1){
		int m;
		scanf("%d%d",&n,&m);
		REP(i,0,n) e[i].clear();
		memset(g,false,sizeof(g));
		REP(i,0,m){
			int a,b;
			scanf("%d,%d",&a,&b);
			e[a].push_back(b);
			e[b].push_back(a);
			g[a][b] = g[b][a] = true;
		}
		
		min_threat = 0;
		d = vector<int> (n,-1);
		d[0] = 0;
		queue<int> q;
		q.push(0);
		while (!q.empty()){
			int i = q.front(); q.pop();
			REP(x,0,e[i].size()){
				int j = e[i][x];
				if (d[j]==-1){
					d[j] = d[i]+1;
					q.push(j);
				}
			}
		}
		
		conq = vector<bool> (n,false);
		threat = vector<bool> (n,false);
		conq[0]=true;
		REP(x,0,e[0].size())threat[e[0][x]]=true;
		dfs(0);
		printf("Case #%d: %d %d\n",Case,d[1]-1,min_threat);
	}
	return 0;
}
