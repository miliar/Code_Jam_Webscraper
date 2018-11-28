#include <cstdio>

unsigned int values[1000];
int main()
{
	int T;
	scanf("%d", &T);
	for (int test=1; test<=T; ++test) {
		int N;
		scanf("%d",&N);
		for (int i=0; i<N; ++i) {
			scanf("%u",&values[i]);
		}
		unsigned int totalpossible = (((unsigned int)1 << N) - 1);
		unsigned int answer = 0;
		for (int cursplit = 1; cursplit < totalpossible; ++cursplit) {
			unsigned int SeanActVal = 0;
			unsigned int PatActVal = 0;
			unsigned int SeanPatVal = 0;
			unsigned int PatPatVal = 0;
			
			for (int bit=0; bit<N; ++bit) {
				unsigned int pos = (unsigned int)1 << bit;
				if (cursplit & pos) {
					SeanActVal += values[bit];
					SeanPatVal ^= values[bit];
				}
				else {
					PatActVal += values[bit];
					PatPatVal ^= values[bit];
				}				
			}
			if (SeanPatVal == PatPatVal) {
				if (SeanActVal > answer) {
					answer = SeanActVal;
				}
			}
		}
		if (answer == 0) {
			printf("Case #%d: NO\n", test);
		}
		else {
			printf("Case #%d: %u\n", test, answer);
		}
	}
}