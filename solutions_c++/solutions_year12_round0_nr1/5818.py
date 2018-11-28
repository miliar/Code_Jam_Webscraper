#include <iostream>
#include <string>

using namespace std;

const char MAPPING[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main (int argc, char** argv) {
    int iterationCount;
    string originString;
    int iterationIndex = 0;

    cin >> iterationCount;


    // for (int i = 0; i < iterationCount; i++) {
    while (iterationIndex < iterationCount) {
        getline (cin, originString);

        if (originString.length() == 0) {
            continue;
        }

        // cout << "string " << iterationIndex + 1 << ": " << originString << endl;
        cout << "Case #" << iterationIndex + 1 << ": ";
        for (int j = 0; j < originString.length(); j++) {
            if (originString[j] >= 'a' && originString[j] <= 'z') {
                cout << MAPPING [originString[j] - 'a'];
            } else {
                cout << originString[j];
            }
        }
        cout << endl;

        iterationIndex += 1;
    }

    return 0;
}