#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int casenum = 1; casenum <= cases; casenum++) {
		int k;
		gets(inp); sscanf(inp, "%d", &k);
		char S[50001];
		gets(inp); sscanf(inp, "%s", &S);
		
		vector <int> p;
		for (int i = 0; i < k; i++) {
			p.push_back(i);
		}
		int minnum = 1 << 30;
		do {
			int prev = -1;
			int num = 0;
			for (int i = 0; i < strlen(S); i++) {
				int modu = i % k;
				int base = i - modu;
				if (prev != S[base + p[modu]]) {
					num ++;
				}
				prev = S[base + p[modu]];
			}
			minnum = min(num, minnum);

		} while (next_permutation(p.begin(), p.end()));

		printf("Case #%d: %d\n", casenum, minnum);
	}

	return 0;
}

