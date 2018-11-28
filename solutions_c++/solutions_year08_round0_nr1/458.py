#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
using namespace std;

#define FOR(a,b,c) for(int a=(int)(b);a<(int)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<int,int>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LINF 90000000000000000000LL
#define LLMAX ((unsigned long long)(-1))

void printArray(vector<int> &v){ FOR(i,0,v.size()) cout << v[i] << " "; cout << endl;}

int dp[100][1000];
int S, Q;

int solve(int which, int pos, vector<int> &v){
    if(pos == v.size()) return 0;
    if(dp[which][pos] != -1) return dp[which][pos];
    if(which != v[pos]) return dp[which][pos] = solve(which,pos+1,v);
    dp[which][pos] = INF;
    FOR(i,0,S) if(i!=which) dp[which][pos] = min(dp[which][pos],1 + solve(i,pos+1,v));
    return dp[which][pos];
}

int main(){
   int N;
   cin >> N;
   FOR(i,0,N){
	  cin >> S;
	  MEMSET(dp,-1);
	  map<string,int> hash; string str; getline(cin,str);
	  FOR(j,0,S) { getline(cin,str); hash[str] = j;
//		   cout << str << ":" << j << endl;
		}
	  cin >> Q; vector<int> stuff(Q); getline(cin,str);
//	  cout << "Q: " << Q << endl;
	  FOR(j,0,Q) { getline(cin,str); stuff[j] = hash[str];
//		cout << str << " - " << hash[str] << endl;

	  }
//	  printArray(stuff);
	  int best = 2*Q;
	  FOR(j,0,S) best = min(best,solve(j,0,stuff));
	  cout << "Case #" << (i+1) << ": " << best << endl;
	}
   return 0;
}
