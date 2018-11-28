#include <iostream>
#include <vector>
#define SCAN(i) scanf("%d",&i);
#define SCANL(i) scanf("%u",&i);
#define SCANS(i) scanf("%s",&i);
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;
int testcase;
unsigned long int runs, capacity, numberofgroups, groups[1000];
long int run() {
	register unsigned long int ans = 0, currentindex = 0;
	register unsigned long int  tempcapacaity;
	int done = 0;
	for (unsigned long int i = 0; i < runs; ++i) {
		tempcapacaity = capacity;
		for (register unsigned long int i = currentindex; i < numberofgroups; ++i) {
			if (!done) {
				if (groups[i] <= tempcapacaity)
					tempcapacaity -= groups[i];
				else {
					currentindex = i;
					done = 1;
				}
			} else
				break;
		}
		for (register unsigned long int i = 0; i < currentindex; ++i) {
			if (!done) {
				if (groups[i] <= tempcapacaity)
					tempcapacaity -= groups[i];
				else {
					currentindex = i;
					done = 1;
				}
			} else
				break;
		}
		done = 0;
		ans += capacity - tempcapacaity;
	}
	return ans;
}
int main() {
	int i = 0;
	freopen("D:\i.in", "r", stdin);
	freopen("D:\o.in", "w", stdout);
	SCAN(testcase);
	REP(i,testcase) {
		SCANL(runs);
		SCANL(capacity);
		SCANL(numberofgroups);
		for (int var = 0; var < numberofgroups; ++var) {
			SCANL(groups[var]);
		}
		printf("Case #%d: %u\n", i + 1, run());
		fflush(stdout);
	}
	return 0;
}
