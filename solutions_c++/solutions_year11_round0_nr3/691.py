#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

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
	int n;
	cin >> n;
	vector<long long> pile = readVector(n);
	sort(pile.begin(), pile.end());

	long long sum = 0, xorSum = 0;
	for (size_t i = 0; i < pile.size(); i++) {
		sum += pile[i];
		xorSum ^= pile[i];
	}

	if (xorSum != 0) 
		cout << "NO" << endl;
	else
		cout << sum - pile[0] << endl;
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