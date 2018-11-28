/******* vinay saini - IIITA ********/
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cmath>
#include <list>
#include <cstdlib>
#include <map>
#include <cstring>
#include <set>
#include <stack>
#include <sstream>
#include <queue>
#include <ctime>

using namespace std;

#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define   REP(i,n) for(int(i)=0;(i)<(n);(i)++)
#define  INF (1<<29)
#define         pb push_back
#define 	     sz size()
#define         mp make_pair
#define 	all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define       min(a,b) ((a)<(b)?(a):(b))
#define         max(a,b) ((a)>(b)?(a):(b))
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define xx first
#define yy second
typedef long long ll;
typedef pair<int,int>  pii;
typedef vector<string> vs;
ll s2i(string s) { istringstream iss(s); ll x;iss>>x; return x;}
string i2s(ll x) { ostringstream oss; oss<<x; return oss.str();}

int N, S, p;
int ar[105];
int ans;
void input()
{
	scanf("%d%d%d",&N, &S, &p);
	REP(i,N) scanf("%d",ar+i);
}

void solve()
{
	ans = 0;
	REP(i, N) {
		int x = ar[i] / 3;
		int rem = ar[i]%3;
		if(rem == 0) {
			if(x >= p) { ans++; continue; }
			if(x >= 1 && x+1 >= p && S > 0) ans++, S--; 
		}
		else if(rem == 1) {
			if(x+1 >= p) { ans++; continue;}
		}
		else {
			if(x+1 >= p) ans++;
			else {
				if(x+2 >= p && S > 0) ans++, S--;
			}
		}		
	}
}

int main()
{
	int T;
	scanf("%d",&T);
	getchar();
	for (int case_num = 1; case_num <= T; case_num++) {
		input();
 		solve();
		printf("Case #%d: %d\n",case_num, ans);
	}
	return 0;
}	
	
