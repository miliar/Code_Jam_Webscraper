#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int calcGcd(int a, int b) {
    if (b > a) {
	int c = a; a = b; b = c;
    }
    while (b) {
	int c = a % b;
	a = b;
	b = c;
    }
    return a;
}

int main() {
    int C;
    cin >> C;
    for (int c = 1; c <= C; ++c) {
	int N;
	cin >> N;
	vector<int> times(N);
	for (int i = 0; i < N; ++i) {
	    cin >> times[i];
	}
	sort(times.begin(), times.end());
	vector<int> diffs;
	for (int i = 0; i < N; ++i) {
	    for (int j = i+1; j < N; ++j) {
		diffs.push_back(abs(times[i]-times[j]));
	    }
	}
	sort(diffs.begin(), diffs.end());
	int a = diffs[1], b = diffs[0];
	int gcd = calcGcd(a, b);
	bool ng = false;
	for (int i = 2; i < diffs.size(); ++i) {
	    if (diffs[i] % gcd != 0) {
		ng = true;
		break;
	    }
	}
	int T;
	if (ng) T = 1;
	else T = gcd;
	for (int i = 1; ; ++i) {
	    if (T * i >= times[0]) {
		cout << "Case #" << c << ": " << T*i-times[0] << endl;
		break;
	    }
	}
    }

}
