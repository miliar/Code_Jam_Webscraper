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

int process()
{
	int n, ret = 0;
	vii a;

	scanf("%d", &n);

	a.resize(n);
	
	for(int i = 0; i < n; i++)
		scanf("%d %d", &a[i].first, &a[i].second);

	sort(a.begin(), a.end());

	for(int i = 0; i < n; i++)
		for(int j = i + 1; j < n; j++)
			if(a[i].second > a[j].second)
				ret++;

	return ret;
}

int main()
{
	int tc;

	scanf("%d", &tc);

	for(int i = 1; i <= tc; i++)
		printf("Case #%d: %d\n", i, process());
		
	return 0;
}
