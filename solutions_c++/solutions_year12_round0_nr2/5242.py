#include <iostream>

using namespace std;

int main (int argc, char** argv) {
    int iterationCount;
    int googlerNumber;
    int surpriseTripletNumber;
    int scoreThreshold;
    int score;

    int qualificationCount;

    cin >> iterationCount;

    for (int i = 0; i < iterationCount; i++) {
        cin >> googlerNumber;
        cin >> surpriseTripletNumber;
        cin >> scoreThreshold;

        qualificationCount = 0;

        for (int j = 0; j < googlerNumber; j++) {
            cin >> score;
            
            // if (score < 2) {
            //     continue;
            // }

            if (score == 0 && scoreThreshold > 0) {
                continue;
            }

            if ((score - scoreThreshold == 2 * scoreThreshold - 4 ||
                 score - scoreThreshold == 2 * scoreThreshold - 3) &&
                surpriseTripletNumber > 0) {
                // if qualified
                qualificationCount += 1;
                surpriseTripletNumber -= 1;
            } else if (score - scoreThreshold > 2 * scoreThreshold - 3) {
                qualificationCount += 1;
            }
        }

        cout << "Case #" << i + 1 << ": " << qualificationCount << endl;
    }
    
    return 0;
}