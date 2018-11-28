#include <iostream>
#include <vector>
#define SCAN(i) scanf("%d",&i);
#define SCANL(i) scanf("%ld",&i);
#define SCANS(i) scanf("%s",&i);
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;

long int testcase, runs, capacity, numberofgroups, groups[1000];
long int run() {
	long int ans = 0, currentindex = 0;
	int done = 0;
	for (long int i = 0; i < runs; ++i) {
		long int tempans = 0,tempcapacaity=capacity;
		for (long int i = currentindex; i < numberofgroups; ++i) {
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
		for (long int i = 0; i < currentindex; ++i) {
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
		done=0;
		ans += capacity-tempcapacaity;
	}
	return ans;
}
int main() {
	int i=0;
	freopen("D:\input.in", "r", stdin);
	freopen("D:\output.in", "w", stdout);
	SCAN(testcase);
	REP(i,testcase) {
		SCANL(runs);
		SCANL(capacity);
		SCANL(numberofgroups);
		for (int var = 0; var < numberofgroups; ++var) {
			SCANL(groups[var]);
		}
		printf("Case %d: %ld\n", i + 1, run());
		fflush(stdout);
	}
	return 0;
}
