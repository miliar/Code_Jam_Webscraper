#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i,n) for( int i = 0, _n = (n); i < _n; i++ )
#define fori(i,a,b) for( int i = (a), _n = (b); i <= _n; i++ )
#define ford(i,a,b) for( int i = (a), _n = (b); i >= _n; i-- )
#define tr(it,c) for( __typeof((c).begin()) it = (c).begin(); it != (c).end(); it++ )

#define debug(x) cout << ">>" << #x << " = " << x << endl;

#define two(x) (1<<(x))
#define contain(S,x) (((S)&two(x)) > 0)
#define twoll(x) (1LL<<(x))
#define containll(S,x) (((S)&twoll(x))>0)

#define pb push_back
#define mp make_pair

char invoked[105];

char combine[256][256];
int opposed[256][256];

vector<char> element;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int ntc;
	scanf("%d", &ntc);
	rep(T, ntc) {
		int c, d, n;
		
		memset(combine, 0, sizeof(combine));
		scanf("%d", &c);
		rep(i, c) {
			char str[5];
			scanf("%s", str);
			combine[str[0]][str[1]] = str[2];
			combine[str[1]][str[0]] = str[2];
		}
		
		memset(opposed, 0, sizeof(opposed));
		scanf("%d", &d);
		rep(i, d) {
			char str[5];
			scanf("%s", str);
			opposed[str[0]][str[1]] = 1;
			opposed[str[1]][str[0]] = 1;
		}
		
		scanf("%d", &n);
		scanf("%s", invoked);
		
		element.clear();
		rep(i, strlen(invoked)) {
			element.pb(invoked[i]);
			
			int sz = element.size();
			if (sz > 1) {
				if (combine[element[sz-1]][element[sz-2]] != 0) {
					element.pop_back();
					element.pop_back();
					element.pb(combine[element[sz-1]][element[sz-2]]);
				}
			}
			
			int isopposed = 0;
			
			sz = element.size();
			rep(j, element.size()-1) {
				if (opposed[element[sz-1]][element[j]]) {
					isopposed = 1;
					break;
				}
			}
			
			if (isopposed)
				element.clear();
		}
		
		printf("Case #%d: [", T+1);
		if (element.size() >= 1) {
			printf("%c", element[0]);
			fori(i, 1, element.size()-1)
				printf(", %c", element[i]);
		}
		printf("]\n");
	}
	return 0;
}
