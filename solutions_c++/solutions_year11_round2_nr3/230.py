#include <fstream>
#include <string>
#include <vector>

using namespace std;

#define FILENAME	"C-small-0"

int walls[2048][2048];
int lists[2048][2048];
int l[2048], u[2048], v[2048];
int visited[2048];
int colors[2048];
int ans[2048];
int used[2048];

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		int N, M;
		in >> N >> M;
		for (int i = 0; i < M; ++i)
			in >> u[i];
		for (int i = 0; i < M; ++i)
			in >> v[i];

		memset(walls, 0, sizeof(walls));
		for (int i = 1; i <= N; ++i)
			walls[i][i+1] = 1;
		walls[N][1] = 1;
		for (int i = 0; i < M; ++i) {
			walls[u[i]][v[i]] = 1;
			walls[v[i]][u[i]] = 1;
		}

		int k = 0;
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				if (walls[i][j]) {
					--walls[i][j];
					int prev = i, cur = j;
					l[k] = 0;
					lists[k][l[k]++] = prev;
					while (cur != i) {
						lists[k][l[k]++] = cur;
						int next;
						for (next = prev - 1; true; --next) {
							if (next == 0)
								next = N;
							if (walls[cur][next])
								break;
						}
						prev = cur;
						cur = next;
						--walls[prev][cur];
					}
					++k;
				}
		int lists_n = k;

		int MAX = 1;
		for (int i = 0; i < lists_n; ++i)
			if (l[i] > MAX)
				MAX = l[i];

		int best = 1;
		for (int i = 1; i <= N; ++i) {
			ans[i] = 1;
			colors[i] = 1;
		}
		while (true) {
			bool ok = false;
			for (int i = N; i > 0; --i)
				if (colors[i] < MAX) {
					++colors[i];
					ok = true;
					break;
				} else
					colors[i] = 1;
			if (!ok) break;

			int max = 1;
			for (int i = 1; i <= N; ++i)
				used[i] = 0;
			for (int i = 1; i <= N; ++i) {
				used[colors[i]] = 1;
				if (colors[i] > max)
					max = colors[i];
			}
			for (int i = 1; i <= max; ++i)
				if (used[i] == 0) {
					ok = false;
					break;
				}
			if (!ok || max < best)
				continue;

			for (int i = 0; i < lists_n; ++i) {
				for (int j = 1; j <= max; ++j)
					used[j] = 0;
				for (int j = 0; j < l[i]; ++j)
					used[colors[lists[i][j]]] = 1;
				for (int j = 1; j <= max; ++j)
					if (used[j] == 0) {
						ok = false;
						break;
					}
			}
			if (!ok) continue;

			best = max;
			for (int i = 1; i <= N; ++i)
				ans[i] = colors[i];
		}

		out << "Case #" << test << ": " << best << endl;
		for (int i = 1; i < N; ++i)
			out << ans[i] << " ";
		out << ans[N] << endl;
	}

	return 0;
}