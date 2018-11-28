#include <stdio.h>
#include <string.h>
#include <vector>
using std::vector;
#define D 29
#define C 37
#define N 101
#define maxLen 101
int cnt[N][N];
int main()
{	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);
	int T, n1, n2;
	char str[maxLen], ct[D][3], cb[C][4];
	vector<char> List;
	scanf("%d\t", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &n1);
		for (int i = 0; i < n1; ++i)
			scanf("%s", cb[i]);
		scanf("%d", &n2);
		for (int i = 0; i < n2; ++i)
			scanf("%s", ct[i]);
		int len;
		scanf("%d %s", &len, str);
		List.clear();
		for (int i = 0; i < len; ++i) {
			if (List.empty()) {
				List.push_back(str[i]);
				continue;
			}
			if (n1) {
				int pass1 = 0;
				for (int j = 0; j < n1 && !pass1; ++j)
					if ((str[i] == cb[j][1] && List.back() == cb[j][0])|| (str[i] == cb[j][0] && List.back() == cb[j][1])) {
						List.pop_back();
						List.push_back(cb[j][2]);
						pass1 = 1;
					}
				if (pass1)	continue;
			}
			if (n2) {
				 for (int k = 0; k < n2 && !List.empty(); ++k)
				 	for (int j = 0; j < List.size(); ++j)
						if ((List[j] == ct[k][0] && str[i] == ct[k][1]) || (List[j] == ct[k][1] && str[i] == ct[k][0]))
							List.clear();
				if (List.empty())
					continue;
			}
			List.push_back(str[i]);
		}
		printf("Case #%d: [", t);
		for (int i = 0; i < List.size(); ++i) {
			if (i)	printf(", ");
			printf("%c", List[i]);
		}
		puts("]");
	}
	scanf(" ");
	return 0;
}
