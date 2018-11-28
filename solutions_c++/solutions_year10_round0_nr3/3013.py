#include <iostream>
#include <queue>
using namespace std;

unsigned long long money_made(int R, const int k, queue<int> &g)
{
	unsigned long long acc = 0;
	for (; R > 0; --R) {
		queue<int> in;
		int places_left = k;
		while (!g.empty() && g.front() <= places_left) {
			places_left -= g.front();
			acc += g.front();
			in.push(g.front());
			g.pop();
		}
		while (!in.empty()) {
			g.push(in.front());
			in.pop();
		}
	}
	return acc;
}

int main()
{
	int T; cin >> T;
	for (int x = 1; x <= T; ++x) {
		int R, k, N; cin >> R; cin >> k; cin >> N;
		queue<int> g;
		for (; N > 0; --N) {
			int g_i; cin >> g_i;
			g.push(g_i);
		}
		cout << "Case #" << x << ": " << money_made(R, k, g) << "\n";
	}
}
