#include <string>
#include <iostream>
#include <vector>

using namespace std;


int rle(string s) {
	char prev = -1;
	int count = 0;
	for (int i = 0; i < s.size(); ++i) {
		if (prev != s[i]) count++;
		prev = s[i];
	}
	return count;
}

int main() {
	int N;
	cin >> N;
	for (int z = 1; z <= N; ++z) {
		int k;
		string s;
		cin >> k >> s;
		vector<int> v;
		for (int i = 0; i < k; ++i) v.push_back(i);
		int low = INT_MAX/2;
		while (true) {
			string s2 = s;
			for (int i = 0; i < s.size(); i += k) {
				for (int j = 0; j < k; ++j) {
					s2[i+j] = s[i+v[j]];
				}
			}
			low = min(low, rle(s2)); 
			if (!next_permutation(v.begin(), v.end())) break;
		}
		cout << "Case #" << z << ": " << low << endl;
	}
}
