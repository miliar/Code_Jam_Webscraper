#include <cstdio>
#include <cstddef>
#include <cassert>
#include <algorithm>


const size_t NMAX = 64;

char _bins[NMAX][NMAX + 1];

size_t N;
char * bins[NMAX];


void initBins() {
	for(size_t i = 0; i < NMAX; ++i)
		bins[i] = _bins[i];
}


bool isRight(const char * line, size_t n) {
	for(size_t i = n + 1; i < N; ++i)
		if( line[i] != '0' )
			return false;
	return true;
}


size_t processCase() {
	size_t count = 0;

	for(size_t i = 0, j; i < N; ++i) {
		for(j = i; j < N && !isRight(bins[j], i); ++j);

		if( j == N ) {
			assert( j < N );
		}

		for(; j > i; --j) {
			std::swap(bins[j], bins[j - 1]);
			++count;
		}
	}

	return count;
}


int main() {
	//freopen("input.txt", "r", stdin);

	size_t T;
	scanf("%u", &T);

	for(size_t t = 0; t < T; ++t) {
		scanf("%u", &N);

		initBins();
		for(size_t i = 0; i < N; ++i)
			scanf("%s", bins[i]);

		printf("Case #%u: %u\n", t + 1, processCase());
	}

	return 0;
}