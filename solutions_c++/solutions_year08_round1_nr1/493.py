#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v1;
vector<int> v2;

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	int caseCnt = 0;
	while(numCases) {
		--numCases;
		caseCnt++;
		long long int total = 0;
		v1.clear();
		v2.clear();
		int numbers;
		scanf("%d", &numbers);

		int tmpNumber;
		for (int i = 0; i < numbers; i++) {
			scanf("%d", &tmpNumber);
			v1.push_back(tmpNumber);
		}
		for (int i = 0; i < numbers; i++) {
			scanf("%d", &tmpNumber);
			v2.push_back(tmpNumber);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		for (int i = 0; i < numbers; i++) {
			total += (v1[i] * v2[numbers - 1 - i]);
		}

		printf("Case #%d: %lld\n", caseCnt, total);
	}

	return 0;
}
