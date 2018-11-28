#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x)
{
    return x*x;
}

int gcd(int a, int b)
{
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int main(int argc, char** argv)
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
    for(int ti=1; ti<=T; ++ti) {
		int C, D, N;
		scanf("%d", &C);
		map <char, map<char, char> > mc;
		char str[105];
		for(int i=0; i<C; ++i) {
			scanf("%s", str);
			mc[str[0]][str[1]] = str[2];
			mc[str[1]][str[0]] = str[2];
		}
		scanf("%d", &D);
		map <char, map <char, bool> > md;
		for(int i=0; i<D; ++i) {
			scanf("%s", str);
			md[str[0]][str[1]] = 1;
			md[str[1]][str[0]] = 1;
		}

		scanf("%d", &N);
		scanf("%s", str);
		vector <char> ans;
		for(int i=0; i<N; ++i) {
			ans.PB(str[i]);
			if(ans.size()>=2 && mc[ans[ans.size()-1]][ans[ans.size()-2]] != 0){
				char ch = mc[ans[ans.size()-1]][ans[ans.size()-2]];
				ans.pop_back();
				ans.pop_back();
				ans.PB(ch);
			}
			else {
				for(int j=0; j<ans.size()-1; ++j) {
					if(md[ans[j]][ans[ans.size()-1]] == 1) {
						ans.clear();
						break;
					}
				}
			}
		}
		printf("Case #%d: [", ti);
		for(int i=0; i<ans.size(); ++i) {
			printf("%s%c", i==0?"":", ", ans[i]);
		}
		puts("]");
	}
    return (EXIT_SUCCESS);
}

