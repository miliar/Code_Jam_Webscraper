#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n_cases;
	int p_score, n_googlers, n_surprises;
	cin >> n_cases;
	for (int c = 1; c <= n_cases; ++c) {
		cin >> n_googlers >> n_surprises >> p_score;
		vector<int> total_scores(n_googlers);
		// see how many can be >=p_score
		vector<int> can_be_valid;
		for (int i = 0; i < n_googlers; ++i) {
			cin >> total_scores[i];
		}
		// We have possible valid elements.
		// Now test to see how the surprising can be made.
		//   a     b    c
		int cnt, surprise_to_pas_limit; 
		cnt = 0;
		surprise_to_pas_limit = 0;
		for (int i = 0; i < n_googlers;++i) {
			// 0 and 1 are special
			if (total_scores[i] < 2) {
				if (total_scores[i]>= p_score)
					cnt++;
				continue;
			}
			// the score is greater than 2
			int mod = total_scores[i]%3;
			int div = total_scores[i]/3;
			switch (mod) {
				case 0:	
					if (div + 1 == p_score)
						surprise_to_pas_limit++;
					else if (div+1 > p_score)
						cnt++;
					break;
				case 1:
					if (div+1 >= p_score)
						cnt++;
					break;
				case 2:
					if (div+2 == p_score)
						surprise_to_pas_limit++;
					else if (div+1 >= p_score)
						cnt++;
					break;
				default:
					cout << "err"<< endl;
			}
		}
		if (n_surprises > surprise_to_pas_limit) {
			cnt += surprise_to_pas_limit;
		} else {
			cnt += n_surprises;
		}
		cout << "Case #" << c << ": " << cnt << endl;
	}
}