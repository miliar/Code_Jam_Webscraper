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
ll s2i(string s) { istringstream iss(s); int x;iss>>x; return x;}
string i2s(int x) { ostringstream oss; oss<<x; return oss.str();}

int A, B;
int ans;
void input()
{
	scanf("%d%d",&A, &B);
}

int cnt_dig(int n)
{
	int ret = 0;
	while(n) ret++, n /= 10;
	return ret;
}

void solve()
{
	ans = 0;
	for ( int i = A; i <= B; i++) {
		string s = i2s(i);
		int j;
		vector<pii> v;
		for(j = 1; j < s.sz; j++) {
			string temp = s.substr(j,s.sz) + s.substr(0,j);
			int num = s2i(temp);
			if(A <= i && i < num && num <= B) {
				if(find(all(v),mp(i,num)) == v.end()) v.pb(mp(i,num)), ans++;
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
	
