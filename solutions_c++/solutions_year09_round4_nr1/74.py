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
#include <queue>


#define debug(x) cout << '>' << #x << ':' << x << '\n';
#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define forn(X,Y) for (int X = 0;X < Y;X++)
#define sz(Z) Z.size()
#define all(W) W.begin(), W.end()
#define inf 2123123123LL
#define eps 0.0000001
#define vint vector<int>
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)
#define mp make_pair
#define I(M) (typeof((M).begin()))
#define pb push_back

#define pipii pair< int, pair<int, pair<int, pair<int,int> > > >

typedef long long ll;
typedef long double ld;

using namespace std;

int n;
int righto[60];
int sudah[60];

int main() {

	int zz;
	scanf("%d",&zz);
	forn(z,zz) {
		printf("Case #%d: ",z + 1);
		scanf("%d\n",&n);
		memset(righto,0,sizeof(righto));
		memset(sudah,0,sizeof(sudah));
		forn(i,n) {
			forn(j,n) {
				char hu;
				scanf("%c",&hu);
				if (hu == '1') righto[i] = j;
				}
			scanf("\n");
			}
		
		int ans = 0;
		forn(i,n) {
			int move = 0;
			forn(j,n) {
				if (sudah[j]) continue;
				if (righto[j] <= i) {
					ans += move;
					sudah[j] = 1;
					break;
					}
				move++;
				}
			}
		printf("%d\n",ans);
		}
		
		
		
	
	}

