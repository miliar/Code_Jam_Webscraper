#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define FOREACH(it, v) for(typeof(v.begin()) it = v.begin(); it != v.end(); it++)

using namespace std;

bool bacteria[1000][1000];
bool bacteria2[1000][1000];

int main() {
	int T, k, x1, y1, x2, y2;
	int minx, miny, maxx, maxy;
	
	scanf("%d\n", &T);
	
	FOR(nCase, T) {
		scanf("%d\n", &k);
		
		memset(bacteria, 0, sizeof(bacteria));
		
		miny = minx = 1000000;
		maxx = maxy = 0;
		
		FOR(_, k) {
			scanf("%d %d %d %d\n", &x1, &y1, &x2, &y2);
			
			for(int i = y1; i <= y2; i++) {
				for(int j = x1; j <= x2; j++) {
					bacteria[i][j] = true;
				}
			}
			
			minx = min(minx, x1);
			maxx = max(maxx, x2);
			miny = min(miny, y1);
			maxy = max(maxy, y2);
		}
		
		int generation = 0, dead = 0;
		
		while(!dead) {
			generation++;
			
			dead = true;
			
			memset(bacteria2, 0, sizeof(bacteria2));
			
			for(int i = miny; i <= maxy; i++) {
				for(int j = minx; j <= maxx; j++) {
					int cnt = 0;
					
					if(i && bacteria[i-1][j]) cnt++;
					if(j && bacteria[i][j-1]) cnt++;
					
					if(cnt == 0) bacteria2[i][j] = false;
					else if(cnt == 2) bacteria2[i][j] = true;
					else bacteria2[i][j] = bacteria[i][j];
					
					if(bacteria2[i][j]) dead = false;
				}
			}
			
			memcpy(bacteria, bacteria2, sizeof(bacteria));
		}
		
		printf("Case #%d: %d\n", nCase+1, generation);
	}
}
