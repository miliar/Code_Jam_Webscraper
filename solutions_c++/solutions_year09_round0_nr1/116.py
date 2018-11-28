#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);

	char buffer[1024];
	vector<string> words;
	for (int i = 0; i < D; i++) {
		scanf("%s", buffer);
		words.push_back(buffer);
	}

	for (int i = 1; i <= N; i++) {
		scanf("%s", buffer);
		int ans = 0;		
		for (int w = 0; w < D; w++) {
			bool ok = true;
			int cur = 0;
			for (int j = 0; j < L; j++) {
				if (buffer[cur] == '(') {
					ok = false;
					while (buffer[cur++] !=')') {
						if (buffer[cur] == words[w][j]) ok = true;
					}
					if (ok == false) break;
				}
				else {
					if (buffer[cur++] != words[w][j]) {
						ok = false;
						break;
					}
				}
			}
			if (ok) ans++;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
