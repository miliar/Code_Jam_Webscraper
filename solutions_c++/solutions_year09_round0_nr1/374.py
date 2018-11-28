#include <cstdio>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

char word[5005][16];
char str[100000];

int main()
{
	int L, D, N;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; ++i)
		scanf("%s", word[i]);
	for (int i = 0; i < N; ++i) {
		scanf("%s", str);
		vector<string> v(L);
		int ind = 0;
		int j = 0;
		while (ind < L) {
			if (str[j] == '(') {
				++j;
				while (str[j] != ')') {
					v[ind] += str[j];
					++j;
				}
				++j;
			}
			else
				v[ind] += str[j++];
			++ind;
		}
		int res = 0;
		for (j = 0; j < D; ++j) {
			int flag = 1;
			for (int k = 0; k < L && flag; ++k)
				if (v[k].find(word[j][k]) == string::npos)
					flag = 0;
			if (flag)
				++res;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}