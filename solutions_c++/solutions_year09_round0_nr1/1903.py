#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define pb push_back
#define sz(c) (int)c.size()
#define all(c) c.begin(),c.end()

#define mp make_pair
#define X first
#define Y second

typedef long int Int;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = 1000000000;
const double PI = acos(-1.0);

char text[5000][10];
bool was[5000];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int l, d, n;
	scanf("%d%d%d\n", &l, &d, &n);
	
	FOR(i, 0, d){
		FOR(j, 0, l)
			scanf("%c", &text[i][j]);
		scanf("\n");
	}

	FOR(i, 0, n)
	{
		FILL(was, 1);
		FOR(j, 0, l)
		{
			char c;
			scanf("%c", &c);
			if (c == '(')
			{
				string s;
				scanf("%c", &c);
				while (c != ')'){
					s.pb(c);
					scanf("%c", &c);
				}
				FOR(ii, 0, d)
					if (was[ii])
					{
						bool good = false;
						FOR(k, 0, sz(s))
							if (text[ii][j] == s[k])
								good = true;
						if (! good)
							was[ii] = false;
					}
			}
			else
			{
				FOR(ii, 0, d)
					if (was[ii] && text[ii][j] != c)
						was[ii] = false;
			}
			scanf("\n");
		}
		int res = 0;
		FOR(j, 0, d)
			if (was[j])
				++res;
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}