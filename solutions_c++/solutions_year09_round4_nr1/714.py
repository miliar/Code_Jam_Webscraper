#include <cmath>
#include <cstdio>
#include <cstring>

#include <map>
#include <queue>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

#define ALL(x) (x).begin(),(x).end()
#define FOR(_i,n) for(int _i = 0; _i < (n); _i++)
#define FORI(_i,n) for(int _i = (n)-1; _i >= 0; _i--)
#define FORA(_i,a,n) for(int _i = (a); _i < (n); _i++)
#define FORAI(_i,a,n) for(int _i = (n)-1; _i >= (a); _i--)
#define FOREACH(_it,x) for(typeof((x).begin()) it = (x).begin(); _it != (x).end(); _it++)

using namespace std;

char mat[40][50];
int furthest[40];
int order[40];
char tmp[50];

int main() {
	int T, N;
	
	scanf("%d\n", &T);
	
	FOR(ti, T) {
		scanf("%d\n", &N);
		
		FOR(i, N) {
			order[i] = i;
			furthest[i] = 0;
			scanf("%s\n", mat[i]);
			FOR(j, N) {
				if(mat[i][j] == '1') furthest[i] = j;
			}
		}
		
		int cost = 0, tf;
		FOR(i, N) {
			if(furthest[i] > i) {
				FORA(j, i+1, N) {
					// search!
					if(furthest[j] > i) continue;
					
					FORAI(k, i, j) {
						cost++;
						tf = furthest[k];
						furthest[k] = furthest[k+1];
						furthest[k+1] = tf;
					}
					
					break;
				}
			}
		}
		
		printf("Case #%d: %d\n", ti+1, cost);
	}
	
	return 0;
}
