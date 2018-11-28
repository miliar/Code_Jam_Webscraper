#include <algorithm>
#include <string>
using namespace std;

int main()
{
	int T;
	char str[100];

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%s", str);
		string res = str;
		if (!next_permutation(res.begin(), res.end())) {
			res += '0';
			sort(res.begin(), res.end());
			int i = 0;
			while (res[i] == '0')
				++i;
			swap(res[0], res[i]);
		}
		printf("Case #%d: %s\n", t, res.c_str());
	}
	return 0;
}
