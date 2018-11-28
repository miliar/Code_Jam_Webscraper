#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;


bool valid(int x, int y, int z)
{
	bool valid = true;
	valid &= abs(x - y) <= 2;
	valid &= abs(y - z) <= 2;
	valid &= abs(x - z) <= 2;
	return valid;
}

bool surprising(int x, int y, int z)
{
	bool surprising = false;
	surprising |= abs(x - y) == 2;
	surprising |= abs(y - z) == 2;
	surprising |= abs(x - z) == 2;
	return surprising;
}

int score(int x, int y, int z)
{
	return max(x, max(y, z));
}

pair<int, int> best_results(int sum)
{
	int best_surprising = -1;
	int best = -1;
	for (int i = 0; i <= 10; ++i)
		for (int j = i; j <= 10; ++j)
			for (int k = j; k <= 10; ++k) {
				if (valid(i,j,k) and ( i + j + k == sum)){
					if (surprising(i, j, k)) {
						best_surprising = max(score(i, j, k), best_surprising);
					} else {
						best = max(score(i, j, k), best);
					}
				}
			}
	//assert(best_surprising != -1);
	assert(best != -1);
	return make_pair(best, best_surprising);
}

map<pair<int, int>, int> m;

int solve(const vector<int> &sums, int k, int s, int p)
{
	if (k == sums.size()) return 0;

	if (m.find(make_pair(k, s)) != m.end())
		return m[make_pair(k, s)];

	pair<int, int> br = best_results(sums[k]);
	int best_surprising = br.second;
	int best = br.first;
	
	int sol_surprising = -1;
	if (best_surprising != -1 and s >= 1)
		sol_surprising = (best_surprising >= p ? 1 : 0) + solve(sums, k+1, s-1, p);

	int sol = (best >= p ? 1 : 0) + solve(sums, k+1, s, p);

	int result = max(sol, sol_surprising);
	assert(result != -1);
	m[make_pair(k, s)] = result;
	return result;
}

int main()
{
	int ntc;
	cin >> ntc;
	for (int tc = 1; tc <= ntc; ++tc) {
		int N, S, P;
		cin >> N >> S >> P;
		vector<int> sums(N);
		for (int i = 0; i < N; ++i)
			cin >> sums[i];
		m.clear();
		cout << "Case #" << tc << ": " << solve(sums, 0, S, P) << endl;
	}
}

