#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        
        int numGooglers;
        cin >> numGooglers;
        
        int numSurprising;
        cin >> numSurprising;
        
        int p;
        cin >> p;
        
        int numTriples = 0;
        
        for (int i = 0; i < numGooglers; i++) {
            int score;
            cin >> score;
            
            if (score >= 3 * p - 2)
                numTriples++;
            else if (score >= 3 * p - 4 && score >= p && numSurprising) {
                numTriples++;
                numSurprising--;
            }
        }
        cout << numTriples << endl;
    }
    return 0;
}

