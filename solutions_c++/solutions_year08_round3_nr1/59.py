#include <cstdio>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int casenum = 1; casenum <= cases; casenum++) {
		int P, K, L;
		gets(inp); sscanf(inp, "%d%d%d", &P, &K, &L);

		vector <int> freq;
		gets(inp);
		stringstream ss(inp);
		for (int i = 0; i < L; i++) {
			int f;
			ss >> f;
			freq.push_back(f);
		}

		sort(freq.begin(), freq.end(), greater<int>());
		int num = 0;
		for (int i = 0; i < L; i++) {
			num += freq[i] * (i / K + 1);
		}

		printf("Case #%d: %d\n", casenum, num);
	}

	return 0;
}

