#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

int pairChar(char c1, char c2) {
	return (((int)c1)&255) | ((((int)c2)&255)<<8);
}

int main() {
	int problemCount;
	scanf("%d", &problemCount);
	for(int problemId=0; problemId<problemCount; ++problemId) {
		int result = 0;
		int N;
		scanf("%d", &N);
		int rP[2] = {1, 1};
		int rT[2] = {0, 0};
		for(int i=0; i<N; ++i) {
			char buf[256];
			int P;
			scanf("%s%d", buf, &P);
			int R = (buf[0]=='O' ? 0 : 1);
			int dP = abs(rP[R] - P);
			result = max(rT[R] + dP + 1, result + 1);
			rT[R] = result;
			rP[R] = P;
		}
		printf("Case #%d: %d\n", problemId + 1, result);
	}
	return 0;
}
