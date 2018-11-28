#include <iostream>
#include <stdint.h>
#include <string>
#include <cstring>

using namespace std;

enum Result {
    Win,
    Loss,
    None
};

Result* parseLine(const string &line, int n);

int main(int argc, char** argv) {
    string line;
    int t;
    cin >> t;
    getline(cin, line);
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << (i + 1) << ": " << endl;
        int n;
        cin >> n;
        getline(cin, line);

        Result** results = new Result*[n];
        double* wp = new double[n];
        int** winsNotAgainst = new int*[n];
        int* games = new int[n];
        double* owp = new double[n];
        double* oowp = new double[n];

        for (int j = 0; j < n; ++j) {
            getline(cin, line);
            results[j] = parseLine(line, n);
        }

        // Win % easy to calculate:
        for (int j = 0; j < n; ++j) {
            int numGames = 0;
            int numWins = 0;
            winsNotAgainst[j] = new int[n];

            for (int k = 0; k < n; ++k) {
                if (results[j][k] != None) {
                    ++numGames;
                }
                if (results[j][k] == Win) {
                    ++numWins;
                }
            }
            for (int k = 0; k < n; ++k) {
                if (results[j][k] == Win) {
                    winsNotAgainst[j][k] = numWins - 1;
                }
                else {
                    winsNotAgainst[j][k] = numWins;
                }
            }

            wp[j] = (double) numWins / numGames;
            games[j] = numGames;
        }

        // Fill in OWP table
        for (int j = 0; j < n; ++j) {
            double sum = 0.0;
            int opps = 0;
            for (int k = 0; k < n; ++k) {
                if (results[j][k] == None) {
                    continue;
                }
                int gamesNotAgainst = games[k] - 1;
                sum += (double) winsNotAgainst[k][j] / gamesNotAgainst;
                ++opps;
            }
            owp[j] = sum / opps;
        }

        // OOWP table go go go
        for (int j = 0; j < n; ++j) {
            double sum = 0.0;
            int opps = 0;
            for (int k = 0; k < n; ++k) {
                if (results[j][k] == None) {
                    continue;
                }
                sum += owp[k];
                ++opps;
            }
            oowp[j] = sum / opps;
        }

        for (int j = 0; j < n; ++j) {
            cout << .25 * wp[j] + .5 * owp[j] + .25 * oowp[j] << endl;
        }
    }
    return 0;
}

Result* parseLine(const string &line, int n) {
    Result* row = new Result[n];

    const char* stuff = line.c_str();

    for (int i = 0; i < n; ++i) {
        switch (stuff[i]) {
        case '0':
            row[i] = Loss;
            break;
        case '1':
            row[i] = Win;
            break;
        case '.':
            row[i] = None;
            break;
        default:
            cerr << "What is " << stuff[i] << "???" << endl;
            row[i] = None;
            break;
        }
    }

    return row;
}
