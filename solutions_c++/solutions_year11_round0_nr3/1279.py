#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define x first
#define y second

int main() {
	int T;
	scanf("%d", &T);
	FOE(ttt,1,T) {
		int x=0,y=0,s=0,mn=1000001;
		int n;
		scanf("%d", &n);
		FOR(i,0,n) {
			scanf("%d", &y);
			x ^= y;
			s += y;
			if (y < mn) mn = y;
		}
		printf("Case #%d: ", ttt);
		if (x!=0) puts("NO");
		else printf("%d\n", s-mn);
	}
	return 0;
}
