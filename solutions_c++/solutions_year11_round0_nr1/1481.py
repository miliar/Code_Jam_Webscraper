#include <iostream>
#include <string>
#include <cmath>

using namespace std;

void doCase(int caseNum) {
    int N;

    cin >> N;

    int oloc = 1, bloc = 1;
    int otime = 0, btime = 0;
    int totaltime = 0;
    for (int i = 0; i < N; i++) {
        string bot;
        int space;
        cin >> bot >> space;

        int& loc = bot == "O" ? oloc : bloc;
        int& mytime = bot == "O" ? otime : btime;
        int& othertime = bot == "O" ? btime : otime;
        int thistime = abs(space - loc) + 1;
        //cout << bot << " " << space << endl;
        //cout << "thistime: " << thistime << endl;
        int remainder = max(1, thistime - mytime);
        //cout << "remainder: " << remainder << endl;
        totaltime += remainder;
        //cout << "totaltime: " << totaltime << endl;
        othertime += remainder;
        mytime = 0;

        loc = space;
    }

    cout << "Case #" << caseNum << ": " << totaltime << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
