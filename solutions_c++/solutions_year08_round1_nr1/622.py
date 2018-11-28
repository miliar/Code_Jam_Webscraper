
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

    // Files
    ifstream inFile("A-large.in");
    ofstream outFile("A-large.out");

    // Get the number of cases
    long long cases = 0;
    inFile >> cases;

    for (long long i = 0; i < cases; ++i) {

        // Get the size of the vectors
        long long size = 0;
        inFile >> size;

        // Two vectors
        vector<long long> vector1;
        vector<long long> vector2;

        // Grab the info
        for (long long i2 = 0; i2 < size; ++i2) {
            long long temp = 0;
            inFile >> temp;
            vector1.push_back(temp);
        }
        for (long long i2 = 0; i2 < size; ++i2) {
            long long temp = 0;
            inFile >> temp;
            vector2.push_back(temp);
        }

        // Sort the info
        sort(vector1.begin(), vector1.end());
        sort(vector2.begin(), vector2.end());

        // Calculations
        long long result = 0;
        vector<long long>::iterator it1;
        vector<long long>::reverse_iterator it2;
        for (it1 = vector1.begin(), it2 = vector2.rbegin(); it1 != vector1.end(); ++it1, ++it2) {
            result += *it1 * *it2;
        }

        // Output
        outFile << "Case #" << i + 1 << ": " << result << endl;
    }

    // Success
    return 0;
}
