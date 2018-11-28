#include <vector>
#include <list>
#include <map>
#include <set>
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


#define debug(x) cout << '>' << #x << ':' << x << '\n';
#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define forn(X,Y) for (int X = 0;X < Y;X++)
#define sz(Z) Z.size()
#define all(W) W.begin(), W.end()
#define inf 2123123123
#define eps 0.0000001
#define vint vector<int>
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)
#define mp make_pair
#define I(M) (typeof((M).begin()))
#define pb push_back

typedef long long ll;
typedef long double ld;

using namespace std;

int n;

int main() {
	string welcome = "welcome to code jam";
	int banyak[50];
	
	scanf("%d\n",&n);
	forn(i,n) {
		memset(banyak,0,sizeof(banyak));
		banyak[0] = 1;
		char kata[1000];
		scanf("%[^\n]\n",kata);
		int length = strlen(kata);
		forn(j,length) {
			for (int k = sz(welcome) - 1;k >= 0;k--) {
				if (kata[j] == welcome[k]) {
					banyak[k + 1] += banyak[k];
					banyak[k + 1] %= 10000;
					}
				}
			}
		printf("Case #%d: %.4d\n",i + 1,banyak[sz(welcome)]);
		}
	
	return 0;
	}

