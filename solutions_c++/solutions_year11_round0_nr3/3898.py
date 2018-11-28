#include <cstdio>

#define MAX_CANDIES 15

int main() {
	int cases;
	scanf("%i", &cases);

	for(int c = 0; c < cases; ++c) {
		int candy_count;
		int candies[MAX_CANDIES];
		
		scanf("%i", &candy_count);
		
		for(int i = 0; i < candy_count; ++i)
			scanf("%i", &candies[i]);

		int sean_max = -1;

		int to = (1 << candy_count) - 1;

		for(int i = 1; i < to; ++i) {
			int sean = 0;
			int patrick = 0;

			for(int n = 0; n < candy_count; ++n) {
				if((i >> n) & 1)
					sean ^= candies[n];
				else
					patrick ^= candies[n];
			}

			if(sean == patrick) {
				sean = 0;
				for(int n = 0; n < candy_count; ++n) {
					if((i >> n) & 1)
						sean += candies[n];
				}
				
				if(sean > sean_max)
					sean_max = sean;
			}
		}

		printf("Case #%i: ", c + 1);
		
		if(sean_max == -1)
			printf("NO\n");
		else
			printf("%i\n", sean_max);
		
	}

	return 0;
}