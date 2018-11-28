#include <fstream>
using namespace std;

ifstream fin("1.in");
#define cin fin

ofstream fout("1_omar.out");
#define cout fout

int main() {
	int number_of_cases, result, number_of_googlers, number_of_surprising_triplets, target, googler, score, q, r;
	cin >> number_of_cases;

	for (int kase = 1; kase <= number_of_cases; ++kase) {
		cin >> number_of_googlers >> number_of_surprising_triplets >> target;
		for (googler = result = 0; googler < number_of_googlers; ++googler) {
			cin >> score;
			q = score / 3;
			r = score % 3;
			if (0 == r) { // if (score == 3 * q), this means that it's either normal (q, q, q) or surprising (q + 1, q, q - 1).
				if (target == q + 1) { // We need to be surprising...
					if (number_of_surprising_triplets && score) // ...so we must have enough credit to increase the result. Note that the score must be positive to be suitable for the surprising form, since 0 is incorrectly described as (1, 0, -1) in the surprising form, so it can never be surprising.
						--number_of_surprising_triplets, ++result;
				} else if (target <= q) {
					++result; // This is a good option to increase the result directly.
				}
			} else if (1 == r && target <= q + 1) { // if (score == 3 * q + 1), this means that it's either normal (q + 1, q, q) or surprising (q + 1, q + 1, q - 1).
				++result; // Let's be greedy and consider it to be normal. Recall that the question asks for the maximum number, so it's better to leave this opportunity to somebody else. Note that the positivity check is useless here, since 1 (the minimum allowed number here) is correctly (1, 0, 0). Although it's incorrectly (1, 1, -1) as well, we always refrain from being surprising here. Thus (1, 0, 0) is enough to get rid of the positivity test.
			} else if (2 == r) { // if (score == 3 * q + 2), this means that it's either normal (q + 1, q + 1, q) or surprising (q + 2, q, q).
				if (target == q + 2) { // We need to be surprising...
					if (number_of_surprising_triplets) // ...so we must have enough credit to increase the result. Note that the positivity check is useless here, since 2 (the minimum allowed number here) is correctly (1, 1, 0) or (2, 0, 0).
						--number_of_surprising_triplets, ++result;
				} else if (target <= q + 1) {
					++result; // This is a good option to increase the result directly.
				}
			}
		}

		cout << "Case #" << kase << ": " << result << "\n";
	}

	return 0;
}
