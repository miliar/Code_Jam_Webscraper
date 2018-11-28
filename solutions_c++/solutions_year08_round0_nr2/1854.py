#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#define REP(i,n) for (int i=0;i<(n);i++) 
using namespace std;

int train[2][3600][100];
int top[2][3600];
int ans[2];
int na, nb;
int turnaround;
int Count[2][3600];

int
main()
{
	int T, t;
	for ( scanf("%d", &T), t = 0; t < T; t++ ) {
		printf("Case #%d:", t + 1);
		scanf("%d", &turnaround);
		scanf("%d %d", &na, &nb);
		memset(top, 0, sizeof top);
		REP(i,na) {
			int m1, s1, m2, s2;	
			scanf("%d:%d %d:%d", &m1, &s1, &m2, &s2);
			train[0][m1 * 60 + s1][top[0][m1 * 60 + s1]++] = m2 * 60 + s2;
		}
		REP(i,nb) {
			int m1, s1, m2, s2;	
			scanf("%d:%d %d:%d", &m1, &s1, &m2, &s2);
			train[1][m1 * 60 + s1][top[1][m1 * 60 + s1]++] = m2 * 60 + s2;
		}
		ans[0] = ans[1] = 0;
		memset(Count, 0, sizeof Count);
		REP(k,3600) {
			REP(q,2) {
				REP(i,top[q][k]) {
					if ( Count[q][k] > 0 ) --Count[q][k];
					else ++ans[q];
					int e = train[q][k][i] + turnaround;
					if ( e < 3600 ) {
						++Count[1 - q][e];
						//printf("%d %d: %d\n", 1 - q, e, Count[1 - q][e]);
					}
				}
				if ( k + 1 < 3600 ) Count[q][k + 1] += Count[q][k];
			}
		}
		printf(" %d %d\n", ans[0], ans[1]);
	}
}
