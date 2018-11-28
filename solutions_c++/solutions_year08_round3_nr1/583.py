
// Headers
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <exception>

// Namespace
using namespace std;

// Main, program entry point
int main(int argc, char* argv[]) {
    try {
        // Files
        ifstream fileIn("A-large.in");
        ofstream fileOut("A-large.out");

        // The number of cases
        int64_t cases;
        fileIn >> cases;

        // For each case
        for (int64_t i = 0; i != cases; ++i) {
            int64_t P = 0, K = 0, L = 0;
            fileIn >> P >> K >> L;
            int64_t count = 0, mult = 1, num = 0;
            vector<int64_t> F;
            for (int64_t c = 0; c < L; ++c) {
                int64_t temp;
                fileIn >> temp;
                F.push_back(temp);
            }
            sort(F.begin(), F.end());
            vector<int64_t>::reverse_iterator it;
            for (it = F.rbegin(); it != F.rend(); ++it) {
                if (count == K) {
                    ++mult;
                    count = 0;
                }
                num += (*it) * mult;
                ++count;
                cout << "C: " << *it << "  N: " << num << "   " << endl;
            }

            cout << "Hello: " << num << endl;
            fileOut << "Case #" << i + 1 << ": " << num << endl;
        }
    } catch (exception &e) {
        cout << "std exception: " << e.what() << endl;
    }
    //Success
    return 0;
}
