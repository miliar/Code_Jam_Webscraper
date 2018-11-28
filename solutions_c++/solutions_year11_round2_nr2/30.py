#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

typedef pair<int, int> P;
#define x first
#define y second
P a[1111];
int n, d;

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d%d", &n, &d);
	FOR(i,0,n)scanf("%d%d", &a[i].x, &a[i].y);

	double lb = 0.0, ub = 1e30;
	FOR(it,0,1000){
		double md = (lb+ub)*0.5;
		double c = -1e30;
		bool bad = false;
		FOR(i,0,n){
			c = max(c, a[i].x-md)+(a[i].y-1)*d;
			if(c > a[i].x+md){
				bad = true;
				break;
			}
			c+=d;
		}
		if(bad){
			lb = md;
		}else{
			ub = md;
		}
	}
	
	printf("Case #%d: %.12f\n", ++tt, ub);
}
	return 0;
}


