#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); i++)
#define sz(a) int((a).size()) 
#define all(c) (c).begin(), (c).end() 
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c, x) ((c).find(x) != (c).end()) 
#define cpresent(c, x) (find(all(c), x) != (c).end())
template<class T> T sqr(T x){return x*x;}
int toint(string s){istringstream sin(s); int x; sin>>x; return x;}
string tostring(int x){ostringstream sout; sout<<x; return sout.str();}


int main()
{
	int t, n, k, m;

	scanf("%d", &t);
	
	for(int i = 1; i <= t; i++) {
		scanf("%d %d", &n, &k);
		m = (1 << n) - 1;
		printf("Case #%d: %s\n", i, (k & m) == m ? "ON" : "OFF");
	}

	return 0;
}
