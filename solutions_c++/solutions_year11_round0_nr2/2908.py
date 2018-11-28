#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i,a) for (int i = 0; i < a.size(); i++)
#define sz size()
#define mp make_pair
#define pb push_back
#define VI vector< int >
#define PII pair< int, int>
#define inf (100000000)
#define all(a) a.begin(),a.end()
#define have(msk, i) (!!((1<<(i)) & msk))
#define pi 3.1415926535897932384626433832795
#define sqr(a) ((a) * (a))
#define eps 1e-9
using namespace std;
map< string, string > mm;
set< string > todelete;
void solve(int testNumber) {
	mm.clear();
	todelete.clear();
	int c;
	cin >> c;
	forn(i,c) {
		string u;
		cin >> u;
		mm[u.substr(0, 2)] = u.substr(2);
		mm[u.substr(1, 1) + u.substr(0, 1)] = u.substr(2);
	}

	int q;
	cin >> q;
	forn(i,q) {
		string u;
		cin >> u;
		todelete.insert(u);
		reverse(all(u));
		todelete.insert(u);
	}

	int n;
	cin >> n;
	string uu;
	cin >> uu;

	vector< string > st;
	forv(i, uu) {
		st.push_back(uu.substr(i, 1));
		if (st.size() > 1) {
			string qq = st[st.size() - 2] +  st[st.size()-1];
			if (mm.find(qq) != mm.end()) {
					st.pop_back();
					st.pop_back();
					st.push_back(mm[qq]);
					continue;
			}

		}
		string x = uu.substr(i, 1);
		forv(i, st)if (todelete.count(st[i] + x)) {
			st.clear();
			break;
		}
	}

	printf("Case #%d: [", testNumber);
	int was =  0;
	forv(i, st) {
		if (st[i].size() == 0)continue;
		if (was > 0)printf(", ");
		printf("%s", st[i].c_str());
		was = 1;
	}
	
	printf("]\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);

	forn(i, t) {
		solve(i+1);
	}

	return 0;
}
