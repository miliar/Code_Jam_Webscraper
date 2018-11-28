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

int a[2036], n;

int main() {
	int T;
	scanf("%d", &T);
	FOE(ttt,1,T) {
		scanf("%d", &n);
		int ans=0;
		FOE(i,1,n) scanf("%d", a+i), ans+=a[i]!=i;
		printf("Case #%d: %d\n", ttt, ans);
	}
	return 0;
}
