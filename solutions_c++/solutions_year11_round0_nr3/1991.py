#include <iostream>
#include <vector>

using namespace std;

int min(int a, int b) {
    return a < b ? a : b;
}

int main() {

    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
	int N;
	cin >> N;
	vector<int> candies(N,0);
	int minElement = (1<<30);
	int candysum = 0;
	for (int i = 0; i < N; ++i) {
	    cin >> candies[i];
	    minElement = min(candies[i],minElement);
	    candysum += candies[i];
	}

	bool flag = false;
	for (int i = 0; i < 14; ++i) {
	    int sum = 0;
	    for (int j = 0; j < candies.size(); ++j) {
		int temp = (candies[j] & (1<<i));
		temp = (temp >> i);
		sum += temp;
	    }
	    if (sum % 2 != 0) {
		flag = true;
	    }
	}
	cout << "Case #" << testcase << ": ";
	if (flag) {
	    cout << "NO" << endl;
	} else {
	    int res = candysum - minElement;
	    cout << res << endl;
	}
    }

}
