#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Ignore the number of test cases
    cin.ignore(100, '\n');

    size_t numGooglers;
    size_t numSurprises;
    size_t caseCount = 1;
    int minScore;

    while (cin >> numGooglers) {
        size_t numGooglersWithMinScore = 0;
        cin >> numSurprises;
        cin >> minScore;

        for (int i = 0; i < numGooglers; ++i) {
            int totalScore;
            cin >> totalScore;
            const int partial = (totalScore % 3 == 0) ? 0 : 1;
            if (totalScore / 3 + partial >= minScore) {
                ++numGooglersWithMinScore;
            } else if (totalScore > 0 && totalScore % 3 == 0 || totalScore % 3 == 2) {
                if (numSurprises > 0 && totalScore / 3 + 2 >= minScore) {
                    ++numGooglersWithMinScore;
                    --numSurprises;
                }
            }
        }
        cout << "Case #" << caseCount << ": " << numGooglersWithMinScore << '\n';
        ++caseCount;
    }

    return 0;
}
