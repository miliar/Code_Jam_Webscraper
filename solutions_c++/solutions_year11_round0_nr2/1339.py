#include <cstdio>
#include <iostream>

using namespace std;

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	for (int t_i = 1; t_i <= t; t_i++) {
		int c, d, n;
		
		cin >> c;
		char combine['Z' - 'A' + 1]['Z' - 'A' + 1] = {0};
		for (int i = 0; i < c; i++) {
			char a, b, c;
			cin >> a >> b >> c;
			combine[a - 'A'][b - 'A'] = combine[b - 'A'][a - 'A'] = c;
		}

		cin >> d;
		bool opposed['Z' - 'A' + 1]['Z' - 'A' + 1] = {0};
		for (int i = 0; i < d; i++) {
			char a, b;
			cin >> a >> b;
			opposed[a - 'A'][b - 'A'] = opposed[b - 'A'][a - 'A'] = true;
		}

		char lst[100];
		int lst_len = 0;
		cin >> n;
		while (n--) {
			cin >> lst[lst_len++];
			if (lst_len > 1) {
				if (combine[lst[lst_len - 1] - 'A'][lst[lst_len - 2] - 'A']) {
					lst[lst_len-- - 2] = combine[lst[lst_len - 1] - 'A'][lst[lst_len - 2] - 'A'];
				}
				for (int i = 0; i < lst_len - 1; i++) {
					if (opposed[lst[i] - 'A'][lst[lst_len - 1] - 'A']) {
						lst_len = 0;
					}
				}
			}
		}

		cout << "Case #" << t_i << ": [";
		for (int i = 0; i < lst_len; i++) {
			cout << lst[i];
			if (i + 1 < lst_len) cout << ", ";
		}
		cout << "]\n";
	}
}
