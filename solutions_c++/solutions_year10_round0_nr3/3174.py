#include <cassert>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <functional>
#include <numeric>

using namespace std;
typedef vector<int> vi_t;
typedef vector<string> vs_t;
typedef long long i64_t;

int main()
{
  int T; cin >> T; cin.ignore();

  for (int t = 1; t <= T; ++t)
  {
	i64_t R, k;
	int N;
	cin >> R >> k >> N;
	vi_t g(N);
	for (int i = 0; i < N; ++i) cin >> g[i];
	i64_t total = accumulate(g.begin(), g.end(), 0);
	if (total <= k) 
	{
		cout << "Case #" << t << ": " <<  total * R << endl;
		continue;
	}
	int first = 0;
	vector<int> visited(N, 0);
	visited[first] = 1;
	i64_t r = 0;
	i64_t income = 0;
	i64_t cycleIncome = -1;
	int cycleLength = 0;
	int firstCycleIndex = -1;
	while (r < R)
	{
		total = 0;
		while (total + g[first] <= k)
		{
			if (cycleIncome >= 0)
			{
				cycleIncome += g[first];
			}
			total += g[first];
			income += g[first];
			first = (first + 1) % N;
		}
		if (cycleIncome >= 0)
		{
			++cycleLength;
		}
		++r;
		if (r == R) break;
		if (visited[first] && cycleIncome < 0)
		{
			cycleIncome = 0;
			firstCycleIndex = first;
			/*std::cout << "First cycle index: " << 
				firstCycleIndex << std::endl;*/
		} else if(visited[first] && first == firstCycleIndex) {
			//cout << "cycle length: " << cycleLength << endl;
			//std::cout << "Cycle income: " << cycleIncome << endl;
			i64_t cycles = (R - r) / cycleLength;
			income += cycles * cycleIncome;
			r += cycles * cycleLength;
		}
		visited[first] = 1;
	}
	cout << "Case #" << t << ": " <<  income << endl;
  }
  return 0;
}
