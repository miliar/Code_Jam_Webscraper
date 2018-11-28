#include <cstdio>

#include <vector>

using namespace std;

typedef vector<char> TCharVector;
typedef vector<TCharVector> TCharVectorVector;
typedef vector<double> TDoubleVector;
typedef vector<TDoubleVector> TDoubleVectorVector;

char ReadCh() {
	char ch;
	scanf("%c", &ch);
	while ( (ch != '.') && (ch != '1') && (ch != '0') )
		scanf("%c", &ch);
	return ch;
}

int main() {
	freopen("input.txt", "r", stdin);
	// freopen("");

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int iTest = 0; iTest < t; ++iTest) {
		int n;
		scanf("%d\n", &n);
		TCharVector dummy(n);
		TCharVectorVector table(n, dummy);
		for (size_t i = 0; i < n; ++i)
			for (size_t j = 0; j < n; ++j)
				table[i][j] = ReadCh();
		
		TDoubleVector dDummy(n);
		TDoubleVectorVector owp(n, dDummy);
		for (size_t i = 0; i < n; ++i) {
			for (size_t j = 0; j < n; ++j) {
				int played = 0;
				int won = 0;
				for (size_t k = 0; k < n; ++k) {
					if ( (table[i][k] != '.') && (k != j) ) {
						++played;
						if (table[i][k] == '1')
							++won;
					}
				}
				owp[i][j] = double(won)/played;
			}
		}

		TDoubleVector oowp(n);
		for (size_t i = 0; i < n; ++i) {
			double sum = 0;
			int count = 0;
			for (size_t j = 0; j < n; ++j)
				if (table[i][j] != '.') {
					sum += owp[j][i];
					++count;
				}
			oowp[i] = sum/count;
		}

		printf("Case #%d:\n", iTest + 1);
		for (size_t i = 0; i < n; ++i) {
			double result = 0.25*owp[i][i] + 0.5*oowp[i];
			double sum = 0;
			int count = 0;
			for (size_t j = 0; j < n; ++j)
				if (table[i][j] != '.') {
					sum += oowp[j];
					++count;
				}
			result += 0.25*sum/count;
			printf("%.10lf\n", result);
		}
	}

	return 0;
}