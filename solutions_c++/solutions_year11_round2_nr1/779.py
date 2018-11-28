
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <vector>
#define fl(var, start, limit) for(var = (start); var < (limit); ++var)
#define fd(var, start, limit) for(unsigned int var = (start); var < (limit); ++var)
#define flz(var, limit) for(var = 0; var < (limit); ++var)
#define fdz(var, limit) for(unsigned int var = 0; var < (limit); ++var)
#define rl(limitVar) unsigned int limitVar; cin >> limitVar;
#define frl(var, limitVar) rl(limitVar); fdz(var, limitVar)
#define sp << " " <<
using namespace std;
typedef vector<unsigned int> vui;
typedef vector<int> vi;
typedef vector<char> vc;
typedef unsigned int ui;
#define next a; cin >> a; return a;
unsigned int nui() { unsigned int next; }
char nc() { char next; }
int ni() { int next; }
float nf() { float next; }
double nd() { double next; }

void initTestcase() {
}

void cleanTestcase() {
}

void doTestcase() {
    rl(N);

    ui *gamesWon = new ui[N];
    ui *gamesPlayed = new ui[N];
    vui *playedAgainstWon = new vui[N];
    vui *playedAgainstLost = new vui[N];

    fdz(i, N) {
        gamesWon[i] = 0;
        gamesPlayed[i] = 0;

        fdz(j, N) {
            char g = nc();
            while (g != '0' && g != '1' && g != '.') { g = nc(); }
            if ('1' == g) {
                ++gamesWon[i];
                ++gamesPlayed[i];
                playedAgainstWon[i].push_back(j);
            } else if ('0' == g) {
                ++gamesPlayed[i];
                playedAgainstLost[i].push_back(j);
            }
        }
    }

    double *owps = new double[N];
    fdz(i, N) {
        owps[i] = 0;
        fd(j, 0, playedAgainstWon[i].size()) {
            owps[i] += (double) gamesWon[playedAgainstWon[i][j]] / ( gamesPlayed[playedAgainstWon[i][j]] - 1 );
        }
        fd(j, 0, playedAgainstLost[i].size()) {
            owps[i] += (double) (gamesWon[playedAgainstLost[i][j]] - 1) / (gamesPlayed[playedAgainstLost[i][j]] - 1);
        }
        owps[i] /= (playedAgainstLost[i].size() + playedAgainstWon[i].size());
    }

    fdz(i, N) {
        double wp = (double) gamesWon[i] / gamesPlayed[i];
        double oowp = 0;
        fdz(j, playedAgainstWon[i].size()) {
            oowp += owps[playedAgainstWon[i][j]];
        }
        fdz(j, playedAgainstLost[i].size()) {
            oowp += owps[playedAgainstLost[i][j]];
        }
        oowp /= (playedAgainstLost[i].size() + playedAgainstWon[i].size());
        double rpi = 0.25 * wp + 0.50 * owps[i] + 0.25 * oowp;
        cout << rpi << endl;
    }

    delete [] owps;
    delete [] gamesWon;
    delete [] gamesPlayed;
    delete [] playedAgainstWon;
    delete [] playedAgainstLost;
}

int main(int argc, char *argv[]) {
    frl(t, tt) {
        cout << "Case #" << t + 1 << ":" << endl;
        initTestcase();
        doTestcase();
        cleanTestcase();
        cout << endl;
    }
    return EXIT_SUCCESS;
}

