#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cassert>

using namespace std;

void doCase(int caseNum)
{
    int N;

    cin >> N;

    char games[N][N];
    int winrec[N];
    int lossrec[N];
    memset(games, 0, sizeof(games));
    memset(winrec, 0, sizeof(winrec));
    memset(lossrec, 0, sizeof(lossrec));

    for (int i = 0; i < N; i++) {
        string record;
        cin >> record;
        assert(record.length() == N);
        int wins=0, losses=0;
        for (int j = 0; j < N; j++) {
            const char& g = record[j];
            switch (g) {
                case '0':
                    losses++;
                    break;
                case '1':
                    wins++;
                    break;
                case '.':
                    // ...
                    break;
                default:
                    assert(false);
                    break;
            }
            games[i][j] = g;
        }
        winrec[i] = wins;
        lossrec[i] = losses;
    }

    cout << "Case #" << caseNum << ":" << endl;

    double WPs[N];
    memset(WPs, 0, sizeof(WPs));
    for (int i = 0; i < N; i++) {
        WPs[i] = (double)winrec[i] / (double)(winrec[i] + lossrec[i]);
    }
    double OWPs[N];
    memset(OWPs, 0, sizeof(OWPs));
    for (int i = 0; i < N; i++) {
        int count = 0;
        double currOWP = 0;
        for (int j = 0; j < N; j++) {
            switch (games[j][i]) {
                case '0':
                    currOWP += (double)winrec[j] / (double)(winrec[j] + lossrec[j] - 1);
                    count++;
                    break;
                case '1':
                    currOWP += (double)(winrec[j]-1) / (double)(winrec[j] + lossrec[j] - 1);
                    count++;
                    break;
                case '.':
                    break;
                default:
                    assert(false);
                    break;
            }
        }
        OWPs[i] = currOWP / count;
    }
    double OOWPs[N];
    memset(OOWPs, 0, sizeof(OOWPs));
    for (int i = 0; i < N; i++) {
        int count = 0;
        double currOOWP = 0;
        for (int j = 0; j < N; j++) {
            switch (games[j][i]) {
                case '0':
                case '1':
                    currOOWP += OWPs[j];
                    count++;
                    break;
                case '.':
                    break;
                default:
                    assert(false);
                    break;
            }
        }
        OOWPs[i] = currOOWP / count;
    }

    for (int i = 0; i < N; i++) {
        double RPI = 0.25 * WPs[i] + 0.50 * OWPs[i] + 0.25 * OOWPs[i];
        cout << RPI << endl;
    }

}

int main(int argc, const char *argv[])
{
    int T;

    cin >> T;

    cout.precision(12);

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }

    return 0;
}
