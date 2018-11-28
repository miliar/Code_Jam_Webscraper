#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void)
{
	unsigned int L, D, N;
	unsigned char token;
	int i, j, k, count;
	vector< vector<bool> > pattern(15, (26, 0));

	cin >> L >> D >> N;
	vector<string> words(D, "");
	for (i = 0; i < D; i++) 
		cin >> words[i];
	sort(words.begin(), words.end());
	for (k = 0; k < N; k++) {
		for (i = 0; i < L; i++)
			for (j = 0; j < 26; j++)
				pattern[i][j] = 0;
		i = 0;
		while (i < L) {
			cin >> token;
			if (token == '(') {
				cin >> token;
				while (token != ')') {
					pattern[i][token - 'a'] = 1;
					cin >> token;
				}
				i++;
			}
			else {
				pattern[i][token - 'a'] = 1;
				i++;
			}
		}
		count = 0;
		for (i = 0; i < D; i++) {
			for (j = 0; j < L; j++)
				if (pattern[j][words[i][j] - 'a'] == 0) break;
			if (j == L) count++;
		}
		cout << "Case #" << k+1 << ": " << count << endl;
	}

	return 0;
}

