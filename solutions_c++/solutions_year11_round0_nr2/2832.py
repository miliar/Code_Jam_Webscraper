#include <cstdio>
#include <map>
#include <vector>
#include <bitset>

using namespace std;
typedef long long L;

int main(int argc, char const* argv[])
{
	int test_cases;
	scanf("%d", &test_cases);

	for (int case_id = 0; case_id < test_cases; case_id++) {
		map <int, char> nonbase;
		map <char, bitset<32> > opposed;
		bitset<32> expect_opposed;
		
		vector <char> result;

		int c;
		scanf("%d", &c);
		for (int i = 0; i < c; i++) {
			char b1, b2, b3;
			scanf(" %c%c%c", &b1, &b2, &b3);
			nonbase[b1 + ((int)b2 << 8)] = nonbase[((int)b1 << 8) + b2] = b3;
		}

		int d;
		scanf("%d", &d);
		for (int i = 0; i < d; i++) {
			char b1, b2;
			scanf(" %c%c", &b1, &b2);
			opposed[b2].set(b1-'A');
			opposed[b1].set(b2-'A');
		}

		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char b;
			char t;
			scanf(" %c", &b);

			// check nonbase
			result.push_back(b);
			while (result.size() > 1 && 
				(t = nonbase[result.back() + ((int)result[result.size() - 2] << 8)]) != 0 ) {
				result.pop_back();
				result.pop_back();
				result.push_back(t);
			}

			// stupid recalc expect_opposed
			expect_opposed.reset();
			for (char j : result) { 
				expect_opposed |= opposed[j];
				if (expect_opposed.test(j-'A')) {
					result.clear();
					break;
				}
			}
		}

		printf("Case #%d: [", 1 + case_id);
		int length = result.size();
		for (int i = 0; i < length; i++)
			printf("%c%s", result[i], i == length - 1 ? "" : ", ");
		puts("]");
	}
	return 0;
}
