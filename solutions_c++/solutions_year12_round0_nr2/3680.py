#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int numTests;
    cin >> numTests;
    for (int currTest = 0; currTest < numTests; ++currTest)
    {
        int numGooglers, numSurprising, bestNum, numPossible = 0;
        cin >> numGooglers >> numSurprising >> bestNum;
        vector<int> scores;
        for(int i = 0; i < numGooglers; ++i)
        {
            int temp;
            cin >> temp;
            if ((2*(bestNum-1) + bestNum) <= temp) {
                ++numPossible;
            }
            else {
                scores.push_back(temp);
            }
        }

        for(int i = 0; numSurprising > 0 && i < scores.size(); ++i)
        {
            int currScore = scores[i];
            int minScore = bestNum == 1 ? 1 : bestNum + (2 * (bestNum-2));
            if (currScore < minScore) {
                continue;
            }
            --numSurprising;
            ++numPossible;
        }
        cout << "Case #" << currTest+1 << ": " << numPossible << endl;
    }
}
