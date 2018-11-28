#include <stdio.h>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

int main(int argc, char* argv[])
{
	FILE* fp = fopen(argv[1], "r");
	if (!fp) return 1;

	int T;
	fscanf(fp, "%d\n", &T);

	vector<pair<int, int>> v;
	for (int line = 1; line <= T; line++) {
		int N;
		fscanf(fp, "%d\n", &N);

		v.clear();
		for (int n = 0; n < N; n++) {
			int a, b;
			fscanf(fp, "%d %d\n", &a, &b);
			v.push_back(make_pair<int, int>(a, b));
		}

		int result = 0;
		for (vector<pair<int, int>>::const_iterator it1 = v.begin(); it1 != v.end(); ++it1) {
			for (vector<pair<int, int>>::const_iterator it2 = it1; ++it2 != v.end();) {
				if (it1->first > it2->first) {
					if (it1->second < it2->second)
						result++;
				} else {
					if (it1->second > it2->second)
						result++;
				}
			}
		}

		printf("Case #%d: %d\n", line, result);
	}

	fclose(fp);
}
