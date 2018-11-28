#include <iostream>

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define foreach(c, i) \
    for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

void run(int caseId) {

    bool possible = false;
    int answer = -1;
    int numPlayers, low, high;
    cin >> numPlayers >> low >> high;

    int* freqs = new int[numPlayers];

    REP(i, numPlayers) {
        int freq;
        cin >> freq;
        freqs[i] = freq;
    }

    FOR(freq, low, high + 1) {
        bool good = true;
        REP(i, numPlayers) {
            int other = freqs[i];
            if (other % freq != 0 && freq % other != 0) {
                good = false;
                break;
            }
        }
        if (good) {
            possible = true;
            answer = freq;
            break;
        }
    }

    cout << "Case #" << (caseId + 1) << ": ";
    if (!possible) {
        cout << "NO";
    }
    else {
        cout << answer;
    }
    cout << endl;
}

int main(int argc, char** argv) {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        run(i);
    }
    return 0;
}
