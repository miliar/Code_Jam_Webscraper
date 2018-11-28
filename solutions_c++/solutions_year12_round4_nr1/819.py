//#pragma comment(linker, "/STACK:32777216")
#include <iostream> 
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
#include <memory.h>
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i))
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define PII pair<int,int>
#define CLEAR(a) memset((a),0,sizeof((a)))
#define X first
#define Y second
#define sz(a) (int)(a).size()

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;

const double pi=3.141592653589793;
const int INF=1000000000;
const ll mod=1000000007;

int dp[10005];

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	FOR(ttt,0,t){
		cout << "Case #" << ttt + 1 << ": ";
        int n;
        cin >> n;
        vector<pair<int,int> > a;
        FOR(i,0,n){
                   int l,d;
                  cin >> d >> l;
                  a.PB(MP(d,l)); 
                  }
        FOR(i,0,10005)
                      dp[i] = INF;
        dp[0] = 0;
        FOR(i,1,n){
                   FOR(j,0,i)
                              if (dp[j]!=INF){
                                              if (a[j].X-dp[j] >= a[i].X-a[j].X && max(a[j].X,a[i].X-a[i].Y) < dp[i])
                                                         dp[i] = max(a[j].X,a[i].X-a[i].Y);          
                   }           
        }
        int D;
        cin >> D;
        bool q = 0;
        FOR(i,0,n)
                  if (dp[i]!=INF && !q && D - a[i].X <= a[i].X - dp[i]){
                     cout << "YES" << endl;
                     q = 1;      
                  }
        if (!q) cout << "NO" << endl;
		cerr<<ttt+1;
	}
	return 0;
}
