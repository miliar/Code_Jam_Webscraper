#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define D(x) x

using namespace std;

int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int N;
        cin >> N;

        map<char, int> lastpos, lasttime;
        int currentTime = 0;
        lastpos['O'] = lastpos['B'] = 1;
        lasttime['O'] = lasttime['B'] = 0;

        for (int i = 0; i < N; i++) {
            char robot;
            int button;
            cin >> robot >> button;
            currentTime = max(currentTime + 1, 
                    lasttime[robot] + abs(button - lastpos[robot]) + 1);
            lastpos[robot] = button;
            lasttime[robot] = currentTime;
        }

        cout << "Case #" << testCase << ": " << currentTime << endl;
    }
}

