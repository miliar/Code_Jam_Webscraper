#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define ALL(cont) cont.begin(), cont.end()

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<double> vd;

int main()
{
	int T;
	cin >> T;
	REP(t,T)
	{
		int N, M;
		cin >> N >> M;
		set<string> pre;
		string str;
		REP(i,N) { cin >> str; pre.insert(str); }
		int ans = 0;
		REP(i,M)
		{
			cin >> str;
			for(; !str.empty() && pre.insert(str).second; ++ans)
				str.erase(str.find_last_of('/'));
		}
		
		printf("Case #%d: %d\n", t + 1, ans);
	}
	
	return 0;
}
