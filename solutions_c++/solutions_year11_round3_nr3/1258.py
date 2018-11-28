#include<iostream>
#include<vector>

using namespace std;

int N, L, H;
vector<int> freqs;

int main() {
	int T;
	cin >> T;
	for (int testCase = 0; T--; testCase++) {
		cin >> N >> L >> H;
		int curr = L;
		freqs.clear();
		for (int i = 0; i < N; i++) {
			int freq; cin >> freq;
			while (curr <= H && curr % freq != 0 && freq % curr != 0) curr++;
			freqs.push_back(freq);			
		}
		bool possible = false;
		int num = -1, i = curr;
		for (; !possible && i <= H; i++) {
			possible = true;
			for (int j = 0; possible && j < N; j++)
				if (i % freqs[j] != 0 && freqs[j] % i != 0) possible = false;
		}
		if (possible) num = --i;
		cout << "Case #" << (testCase + 1) << ": ";
		if (num != -1)
			cout << num;
		else
			cout << "NO";
		cout << endl;
	}
	return 0;
}