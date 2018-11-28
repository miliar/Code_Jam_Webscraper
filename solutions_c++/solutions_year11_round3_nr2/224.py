#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>

using namespace std;


int computeProfit(long long t, long long arrival, long long distance) {
	if(arrival > t)
		return distance;
	else
		return max(0LL, distance - (t-arrival)/2);
}

void spike() {
	long long l, t, n, c;
	vector<long long> a, distances, times;

	cin >> l >> t >> n >> c;
	
	for (int i = 0; i < c; i++) {
		int v; cin >> v; a.push_back(v);
	}

	times.push_back(0);
	for (int i = 0; i < n; i++)  {
		distances.push_back(a[i%c]);	
		times.push_back(a[i%c]*2 + times[i]);
	}

	vector<long long> profits;
	for (int i = 0; i < n; i++) {
		profits.push_back(computeProfit(t, times[i], distances[i]));
	}

	sort(profits.begin(), profits.end(), greater<long long>());
	long long sum = 0;
	for (int i = 0; i < l; i++)
		sum += profits[i];

	cout << times[n] - sum << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);


	int z;
	cin >> z;
	for (int i = 0; i < z; i++) {
		cout << "Case #" << i+1 << ": ";
		spike();
	}
}