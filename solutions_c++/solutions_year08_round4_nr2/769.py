#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pi pair<int, int>

int cross(int x1, int y1, int x2, int y2) { return x1*y2 - x2*y1; }

int main(void)
{
	int i, j, k;
	int n, m ,a;
	int casos;
	scanf("%d", &casos);
	
	for(int h=0; h<casos; h++) {
		scanf("%d %d %d", &n, &m, &a);
		
		int f = 0;
		int off = 0;
		printf("Case #%d: ", h+1);
		for(int x1=0;!f && x1<=n; x1++) {
			for(int y1=m;!f && y1>=-m; y1--) {
				for(int x2=0;!f && x2<=n; x2++) {
					for(int y2=y1;!f && y2>=max(-m, y1-m); y2--) {
// 						printf("%d\n", abs(cross(x1, y1, x2, y2)));
						if(abs(cross(x1, y1, x2, y2)) == a) {
							f = 1;
							if(y2 < 0) off = abs(y2);
							printf("%d %d %d %d %d %d\n", 0, off, x1, y1+off, x2, y2+off);
							
						}
					}
				}
			}
		}
		if(!f) printf("IMPOSSIBLE\n");
	}
	
	
	return 0;
}
