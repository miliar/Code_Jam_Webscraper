#include <cstdio>

int T;
int candy[1000];

int value(int &result, int &resultSum, int ncandies, int split, int onoff) {
	for(int i = 0; i < ncandies; ++i, split>>=1) {
		if ((split & 1) == onoff&1) {
//			printf("%d XOR %d", result, candy[i]);
			result ^= candy[i];
			resultSum += candy[i];
//			printf(" deu %d\n", result);
		}
	}
	return result;
}

int getMaxSplit(int ncandies, int ncandiesBit) {
	int max = 0;
	for(int i = 1; i < ncandies; ++i) {
		int split1 = 0, split1Sum = 0, split2 = 0, split2Sum = 0;
		value(split1, split1Sum, ncandiesBit, i,0);
//		printf("-----\n");
		value(split2, split2Sum, ncandiesBit, i,1);
//		printf("I: %d ", i);
//		printf("VALUE1: %d ", split1);
//		printf("VALUE2: %d\n", split2);
		if (split1 == split2) {
			if (split1Sum >= max) {
				max = split1Sum;
			}
			else if (split2Sum >= max) {
				max = split2Sum;
			}
		}
	}
	return max;
}
	

int main() {
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		int ncandies;
		scanf("%d", &ncandies);
		for(int c = 0; c < ncandies; ++c) {
			scanf("%d", &candy[c]);
		}

		int result = getMaxSplit((2<<(ncandies-2))+1, ncandies);
		if (result != 0)
		{
			printf("Case #%d: %d\n", i, result);
		}
		else {
			printf("Case #%d: NO\n", i);
		}
	}
	return 0;
}