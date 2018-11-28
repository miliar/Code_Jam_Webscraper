#include <cstdio>
#include <cstring>
#include <sstream>
using namespace std;

char word[5100][20], key[450], ch;
bool used[20][50];
int L, D, n;

int main() {

	scanf("%d %d %d", &L, &D, &n);
	for (int i = 0; i < D; i++) scanf("%s", word[i]);
	for (int i = 0; i < n; i++) {
		memset(used, false, sizeof(used));
		scanf("%s", key);
		istringstream is(key);
		for (int j = 0; j < L; j++) {
			is >> ch;
			if (ch == '(') {
				is >> ch;
				while (ch != ')') {
					used[j][ch - 'a'] = true;
					is >> ch;
				}			
			}
			else {
				used[j][ch - 'a'] = true;
			}	
		}
		int ans = 0;		
		for (int j = 0; j < D; j++) {
			bool yes = true;
			for (int k = 0; k < L; k++)
				if (!used[k][word[j][k] - 'a']) {
					yes = false;
					break;
				}
			if (yes) ans++;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}

	return 0;
}

