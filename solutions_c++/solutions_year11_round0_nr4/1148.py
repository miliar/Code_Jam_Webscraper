#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

int num[1024];
int bit[1024];

int main () {
	
	int T;

	cin >> T;
	for (int t = 1; t <= T; ++t) {
		
		int N, c, p, ans = 0;

		memset(bit, 0, sizeof(int)*1024);

		cin >> N;
		for (int i = 1; i <= N; ++i)
			cin >> num[i];

		for (int i = 1; i <= N; ++i) {
			if (bit[i] == 0) {
			
				p = i;
				c = 0;

				while (bit[p] == 0 && num[p] != p) {
					c++;
					bit[p] = 1;
					p = num[p];
				}

				ans += c;
			
			}
		}

		cout << "Case #" << t << ": " << ans << ".000000" << endl;

	}

	return 0;
}

