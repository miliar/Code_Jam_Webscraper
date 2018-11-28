#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("scores.out", "w", stdout);
	freopen("scores.in", "r", stdin);
	
	int T, N, S, P, g;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> N >> S >> P;
		cout << "Case #" << i << ": ";
		int ans = 0;
		for (int j = 0; j < N; j++) {
			cin >> g;
			if ((g/3 >= P) || (g % 3 == 1 && g/3 + 1 >= P) || (g % 3 == 2 && g/3 + 1 >= P)) ans++;
			else if (S > 0 && ((g % 3 == 0 && g/3 + 1 >= P && g >= 3) || (g % 3 == 2 && g/3 + 2 >= P && g >= 2))) {
				ans++;
				S--;
			}
		}
		cout << ans << endl;
	}
}
