#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>

#define FOR(i, a, b) for(int i = int(a); i < int(b); i++)
#define INF 2000000000
#define EPS 1e-9
#define PB push_back
#define MP make_pair
#define F first
#define S second
using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

int main() {
//	freopen("bot.in", "r", stdin);
//	freopen("bot.out", "w", stdout);
	
	int T, tc = 0;
	scanf("%d", &T);
	
	while(T--) {
		int n;
		scanf("%d", &n);
		
		int po = 1, pb = 1, ans = 0, last = 0;
		char lid = 'z';
		for(int i = 0; i < n; ++i) {
			char id; int pos;
			getchar();
			scanf("%c %d", &id, &pos);
			
			if(id == 'O') {
				int dist = abs(pos - po);
				if(lid == 'E') dist -= last;
				
				if(dist > 0) ans += dist;
				
				if(lid == 'E') last = max(dist, 0);
				else last += dist;
				
				lid = 'O';
				
				ans++; // push tombol;				
				last++;
				po = pos;
//				printf("dist=%d id=%c last=%d ans=%d po=%d pb=%d pos=%d\n", dist, lid, last, ans, po, pb, pos);
			} else {
				int dist = abs(pos - pb);
				if(lid == 'O') dist -= last;
				
				if(dist > 0) ans += dist;
				
				if(lid == 'O') { last = max(dist, 0); lid = 'E'; }
				else last += dist;
				
				lid = 'E';
				
				ans++; // push tombol;	
				last++;			
				pb = pos;
//				printf("dist=%d id=%c last=%d ans=%d po=%d pb=%d pos=%d\n", dist, lid, last, ans, po, pb, pos);
			}
		}

		
		printf("Case #%d: %d\n", ++tc, ans);
	}
	
	return 0;
	}
