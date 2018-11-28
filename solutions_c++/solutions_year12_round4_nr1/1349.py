#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

int T, N, D;
pair<int, int> v[20000];

map<int, map<int, bool> > cache2;

bool solve(int ipos, int ivine)
{
	int max_dist = v[ivine].first + min(v[ivine].first - v[ipos].first, v[ivine].second);
	if (max_dist >= D) return true;
	map<int, bool>& cache1 = cache2[ipos];
	map<int, bool>::iterator it = cache1.find(ivine);
	if (it != cache1.end()) return it->second;
	for (int i = ivine + 1; i <= N; ++i) {
		if (v[i].first > max_dist) break;
		if (solve(ivine, i)) return (cache1[ivine] = true);
	}
	return (cache1[ivine] = false);
}

int main(int argc, char* argv[])
{
	cin >> T;
	for (int t = 0; t != T; ++t) {
		cache2.clear();
		v[0].first = v[0].second = 0;
		cin >> N;
		for (int n = 0; n != N; ++n)
			cin >> v[n + 1].first >> v[n + 1].second;
		cin >> D;
		bool f = solve(0, 1);
		cout << "Case #" << (t + 1) << ": " << (f ? "YES" : "NO") << endl;
	}
	return 0;
}

