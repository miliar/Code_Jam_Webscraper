#include <climits>
#include <iostream>
#include <set>
#include <algorithm>
#include <queue>
#include <vector>
#include <bitset>
#include <map>

using namespace std;

void
solve()
{
	int P, K, L;
	
	cin >>P >>K >>L;
	vector<int> freq(L);
	for (int i = 0; i < L; i++) {
		cin >>freq[i];
		freq[i] = -freq[i];
	}

	if (P * K < L) {
		cout <<"Impossible";
		return;
	}

	sort(freq.begin(), freq.end());
	int result = 0;
	for (int i = 0; i < L; i++) {
		result += -freq[i] * (1 + i / K);
	}

	cout << result;
}

int
main(int argc, char **argv)
{
	int N, n;
	cin >> N;
	for (n = 1; n <= N; n++) {
		cout << "Case #" << n << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
