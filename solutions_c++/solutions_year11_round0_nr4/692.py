#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

vector<long long> readVector(int n) {
	int value;
	vector<long long> result;
	for (size_t i = 0; i < n; i++)	{
		cin >> value;
		result.push_back(value);
	}
	return result;
}

void spike() {
	int n; cin >> n;
	vector<long long> numbers = readVector(n);
	vector<long long> sorted = numbers;
	vector<int> visited(n,0);

	sort(sorted.begin(), sorted.end());

	for (int i = 0; i < n; i++)
		numbers[i] = find(sorted.begin(), sorted.end(), numbers[i]) - sorted.begin();

	double ans = 0;
	for (int i = 0; i < n; i++) {
		int cycle = 0, current = i;
		while (!visited[current]) {
			cycle++;
			visited[current] = true;
			current = numbers[current];
		}
		if (cycle > 1)
			ans += cycle;
	}
	cout << ans << endl;
}

int main() {
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);

	int z;
	cin >> z;
	for (int i = 0; i < z; i++) {
		cout << "Case #" << i+1 << ": ";
		spike();
	}
}