#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t) {
		int k;
		cin >> k;
		string s;
		cin >> s;
		
		vector<int> p(k);
		for(int i = 0; i < k; ++i)
			p[i] = i;

		int m = 1<<30;
		do {
			string s2 = s;
			for(int i = 0; i*k < (int)s.size(); ++i) {
				for(int j = 0; j < k; ++j) 
					s2[i*k+j] = s[i*k+p[j]];
			}

			int c = 0;
			char last = -1;
			for(int i = 0; i < (int)s.size(); ++i)
				if(s2[i] != last) {
					++c;
					last = s2[i];
				}
			m = min(m,c);
		} while(next_permutation(p.begin(), p.end()));

		cout << "Case #" << t << ": " << m << endl;
	}

	return 0;
}
