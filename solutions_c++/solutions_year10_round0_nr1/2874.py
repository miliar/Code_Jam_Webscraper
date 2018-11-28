#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
	int T, N, K;
	scanf("%d", &T);

	for(int i=1; i<=T; i++) {
		scanf("%d", &N);
		scanf("%d", &K);
		K = K + 1;
		N = (int)pow(2.0, (double)N);
		if(K >= N && K%N == 0) {
			printf("Case #%d: ON\n", i);
		} else {
			printf("Case #%d: OFF\n", i);
		}
	}
	return 0;
}