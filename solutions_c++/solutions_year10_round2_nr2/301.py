#include <string>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>
#include <algorithm>
#include <deque>
#include <utility>
#include <sstream>
#include <vector>
#include <map>
#include <ctime>
#include <set>
using namespace std;
#define sz size()
#define vi vector<int>
#define vs vector<string>
#define dsz size()-1
#define pb push_back
#define maxn(a,b) (a) = ((a) < (b) ? (b) : (a))
#define FUP(ii,ss,ff) for ((ii) = (ss);(ii) <= (ff);(ii)++)
#define FDOWN(ii,ss,ff) for ((ii) = (ss);(ii) >= (ff);(ii)--)
#define FALL(ii, vv) for ((ii) = 0;signed (ii) <= signed ((vv).dsz);(ii)++)
#define ITERATE(__it,__container) for(__it=__container.begin(); __it!=__container.end(); __it++)
#define EPS 1e-12
#define INF 2147483647
#define sgn(x) ((x)>0 ? 1 : (x)==0 ? 0 : -1)
#define sq(x) ((x)*(x))
#define sorta(a) sort(a.begin(), a.end())
#define cleara(a, b) memset(a, b, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define absd(a) ((a)<0?-(a):(a))
#define absm absd
#define mp make_pair
typedef unsigned int uint;
typedef long long ll;

int pos[1000];
int vel[1000];

int main() {
	int t, T, n, k, b, TT, i;
	int done, bad;
	scanf("%d", &TT);
	FUP(T,1,TT) {
		int res = 0;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		FUP(i,0,n-1) {
			scanf("%d", &pos[i]);
		}
		FUP(i,0,n-1) {
			scanf("%d", &vel[i]);
		}
		done = 0, bad = 0;
		FDOWN(i,n-1,0) {
			if ((b-pos[i]) > t*vel[i]) {
				bad++;
			} else {
				done++;
				res += bad;
			}
			if (done == k)break;
		}
		if (i == -1) {
			res = -1;
		}
		if (res == -1) {
			printf("Case #%d: IMPOSSIBLE\n", T);
		} else {
			printf("Case #%d: %d\n", T, res);
		}
	}
	return 0;
}