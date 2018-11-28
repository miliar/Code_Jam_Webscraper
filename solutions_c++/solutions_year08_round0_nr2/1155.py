#include <stdio.h>
#include <map>
using namespace std;
int main()
{
	int nt;
	scanf("%d", &nt);
	for (int it = 0; it < nt; it++) {
		int na, nb, t, a, b, c, d, ansA, ansB, trA, trB;
		map<int,int> depA, readyB, depB, readyA;
		scanf("%d %d %d", &t, &na, &nb);
		for (int i = 0; i < na; i++) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			depA[a * 60 + b]++;
			readyB[c * 60 + d + t]++;
		}
		for (int i = 0; i < nb; i++) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			depB[a * 60 + b]++;
			readyA[c * 60 + d + t]++;
		}
		ansA = 0;
		ansB = 0;
		trA = 0;
		trB = 0;
		for (int time = 0; time < 24 * 60; time++) {
			trA += readyA[time];
			trB += readyB[time];			
			while (depA[time] > 0) {
				depA[time]--;
				if (trA == 0) {
					ansA++;
				} else {
					trA--;
				}
			}
			while (depB[time] > 0) {
				depB[time]--;
				if (trB == 0) {
					ansB++;
				} else {
					trB--;
				}
			}
		}
		printf("Case #%d: %d %d\n", it + 1, ansA, ansB);
	}
	return 0;
}
