#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
	ifstream input("input.txt");
	ofstream output("output.txt");
	
	size_t cases;
	input >> cases;
	for (size_t i = 1; i <= cases; ++i) {
		size_t people, surprising, minScoreRequired;
		input >> people >> surprising >> minScoreRequired;
		
		size_t good = 0, goodIfSurprising = 0;
		for (size_t j = 0; j < people; ++j) {
			size_t totalScore;
			input >> totalScore;

			size_t maxScoreNoSurprising = totalScore / 3 + ((totalScore % 3 > 0) != 0);
			if (maxScoreNoSurprising >= minScoreRequired) {
				++good;
			} else if (totalScore >= 2) {
				size_t maxScoreSurprising;
				switch (totalScore % 3) {
					case 0:
					case 1:
						maxScoreSurprising = totalScore / 3 + 1;
						break;
					case 2:
						maxScoreSurprising = totalScore / 3 + 2;
						break;
				}
				goodIfSurprising += maxScoreSurprising >= minScoreRequired;
			}
		}

		output << "Case #" << i << ": " << good + min(goodIfSurprising, surprising) << endl;
	}
}