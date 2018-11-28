#pragma warning(disable:4786)
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main()
{
	int N, S, Q, i, k;
	char str[101];
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> N;
	for (k = 1; k <= N; k ++)
	{
		map <string, bool> engines;
		cin >> S;
		cin.get();
		for (i = 0; i < S; i ++) {
			cin.getline(str, 101);
			engines[str] = false;
		}

		map <string, bool> new_egn = engines;
		int used = 0;
		int ans = 0;
		cin >> Q;
		cin.get();
		for (i = 0; i < Q; i ++) {
			cin.getline(str, 101);
			if (new_egn[str] == false) {
				new_egn[str] = true;
				used ++;
			}
			if (used == S) {
				ans ++;
				new_egn = engines;
				new_egn[str] = true;
				used = 1;
			}
		}

		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}