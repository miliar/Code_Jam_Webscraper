#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int sum, badSum;
vector<int> candies;

bool comp(int a, int b) { return a > b; };

int main() {
	int T;
	cin >> T;
	for (int n = 0; T--; n++) {
		candies.clear();
		int N;
		cin >> N;
		for (int j = 0; N--; j++) {
			int C;
			cin >> C;
			candies.push_back(C);			
		}
		sort(candies.begin(), candies.end(), comp);
		sum = badSum = candies[0];
		for (int j = 1; j < candies.size() - 1; j++) {
			sum += candies[j];
			badSum ^= candies[j];
		}
		cout << "Case #" << (n + 1) << ": ";
		if (badSum ^ candies[candies.size()-1])
			cout << "NO";
		else
			cout << sum;
		cout << endl;
	}
	return 0;
}