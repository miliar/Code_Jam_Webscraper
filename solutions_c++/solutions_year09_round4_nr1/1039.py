#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
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
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); i++)
#define sz(a) int((a).size()) 
#define all(c) (c).begin(), (c).end() 
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c, x) ((c).find(x) != (c).end()) 
#define cpresent(c, x) (find(all(c), x) != (c).end())
template<class T> T sqr(T x){return x*x;}
int toint(string s){istringstream sin(s); int x; sin>>x; return x;}
string tostring(int x){ostringstream sout; sout<<x; return sout.str();}

enum {SIZE = 45};

void process(int tc)
{
	int n, cnt = 0;

	scanf("%d", &n);
	
	string s[SIZE];
	vi last(n, 0);
	
	FOR(i, 0, n)
		cin >> s[i];

	FOR(i, 0, n)
	FOR(j, 0, n)
		if(s[i][j] == '1')
			last[i] = j;
	
	FOR(i, 0, n) {
		int pos;
		FOR(j, i, n)
			if(last[j] <= i) {
				pos = j;
				break;
			}
		for(int j = pos; j > i; j--) {
			swap(last[j], last[j - 1]);
			cnt++;
		}
	}

	printf("Case #%d: %d\n", tc + 1, cnt);
}

int main()
{
	int tc;

	scanf("%d", &tc);

	FOR(i, 0, tc)
		process(i);
	
	return 0;
}
