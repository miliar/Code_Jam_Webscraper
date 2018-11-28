#include <iostream>
#include <cassert>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int inf = (int)1E+9;

typedef long long int64;
typedef pair<int,int> pii;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define last(a) (int)a.size() - 1
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

const int nmax = 5000;
const int lmax = 500;

bool can[lmax][256];
string s[nmax];

int l, d, n;


int main(){
	freopen ("a.in", "rt", stdin);
	freopen ("a.out", "wt", stdout);

	scanf("%d %d %d", &l, &d, &n);

	forn(i,d)
		cin >> s[i];
	forn(tst,n){
		memset(can,0,sizeof can);
		string now;
		cin >> now;
		int pos = 0;
		memset(can,0,sizeof can);
		forn(i,now.size()){
			if (now[i] == '('){
				int j = i;
				while (now[j] !=')') j++;
				for (int k = i+1; k < j; k++)
					can[pos][now[k]] = 1;
				i = j;
			}else can[pos][now[i]] = 1;
			pos++;
		}	
		int res = 0;
		forn(i,d){
			bool good = 1;
			forn(j,l)
				if (!can[j][s[i][j]]) good = 0;
			if (good) res++;
		}
		printf("Case #%d: %d\n", tst+1, res);
	}
			

	return 0;
}
