#include <iostream>
#include <string>
using namespace std;

const int maxc = 50;
const int maxn = 110;
int tc, c, d, n, pos;
string cc[maxc];
string dd[maxc];
string str;
char ans[maxn];

int main() {
	cin >> tc;
	for (int tt = 0; tt < tc; tt++) {
		cin >> c;
		for (int i = 0; i < c; i++)
			cin >> cc[i];
		cin >> d;
		for (int i = 0; i < d; i++)
			cin >> dd[i];
		cin >> n >> str;
		
		pos = 0;
		for (int i = 0; i < n; i++) {
			bool cb = false, rm = false;
			// check combine
			if (pos > 0) {
				for (int j = 0; j < c; j++) {
					if ((cc[j][0] == ans[pos - 1] && cc[j][1] == str[i]) || (cc[j][1] == ans[pos - 1] && cc[j][0] == str[i])) {
						ans[pos - 1] = cc[j][2];
						cb = true;
						break;							
					}
				}
			}

			// check rm
			if (!cb) {
				for (int j = 0; j < d; j++) {
					for (int k = 0; k < pos; k++)
						if ((dd[j][0] == ans[k] && dd[j][1] == str[i]) || (dd[j][0] == str[i] && dd[j][1] == ans[k])) {
							rm = true;
							pos = 0;
							break;
						}
					if (rm)
						break;
				}
			}

			if (!rm && !cb)
				ans[pos++] = str[i];
		}
		printf("Case #%d: [", tt + 1);
		if (pos > 0) {
			for (int i = 0; i < pos - 1; i++)
				printf("%c, ", ans[i]);
			printf("%c]\n", ans[pos - 1]);
		} else {
			printf("]\n");
		}
	}
}