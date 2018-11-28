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

int len,jmldic,jmlword;

vector<string> kata;

int main() {
	
	scanf("%d%d%d",&len,&jmldic,&jmlword);
	
	forn(i,jmldic) {
		char dumi[100];
		string hehe;
		scanf("%s",dumi);
		hehe = dumi;
		kata.pb(hehe);
		}
	
	forn(i,jmlword) {
		//debug(i);
		char dumi[1000];
		string hehe;
		//debug(i);
		vector<char> tuing[20];
		//debug(i);
		scanf("%s",dumi);
		//debug(i);
		//printf("%s",dumi);
		//debug(i);
		int pos = 0;
		forn(j,len) {
			vector<char> tambah;
			if (dumi[pos] != '(') {
				tambah.pb(dumi[pos]);
				tuing[j] = tambah;
				pos++;
				continue;
				}
			pos++;
			while (dumi[pos] != ')') {
				tambah.pb(dumi[pos]);
				pos++;
				}
			pos++;
			tuing[j] = tambah;
			}
		
		int answer = 0;
		forn(k,sz(kata)) {
			int iya = 1;
			forn(j,len) {
				if (find(all(tuing[j]),kata[k][j]) == tuing[j].end()) {
					iya = 0;
					break;
					}
				}
			if (iya) answer++;
			}
		//debug(i);
		printf("Case #%d: %d\n",i + 1,answer);
		}
	
		
	
	return 0;
	}

