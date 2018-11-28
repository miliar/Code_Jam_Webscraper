#include <iostream>
#include <stdint.h>

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define foreach(c, i) \
    for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

int check2(int* dist, uint64_t buildTime, int numStars, int distMod, int first, int second);

void run(int caseId) {

    int numBoosters, numStars, c;
    uint64_t buildTime;
    cin >> numBoosters >> buildTime >> numStars >> c;

    int* dists = new int[c];

    REP(i, c) {
        int dist;
        cin >> dist;
        dists[i] = dist;
    }

    int bestAnswer = 0;

    if (numBoosters == 2) {
        bestAnswer = check2(dists, buildTime, numStars, c, 0, 1);
        REP(i, numStars) {
            FOR(j, i + 1, numStars) {
                int answer = check2(dists, buildTime, numStars, c, i, j);
                if (answer < bestAnswer) {
                    bestAnswer = answer;
                }
            }
        }
    }
    else if (numBoosters == 1) {
        bestAnswer = check2(dists, buildTime, numStars, c, 0, 0);
        REP(i, numStars) {
            int answer = check2(dists, buildTime, numStars, c, i, i);
            if (answer < bestAnswer) {
                bestAnswer = answer;
            }
        }
    }
    else if (numBoosters == 0) {
        bestAnswer = 0;
        REP(i, numStars) {
            bestAnswer += dists[i % c] * 2;
        }
    }
    else {
        cerr << "I can't handle too many boosters!!!" << endl;
        bestAnswer = -1;
    }

    cout << "Case #" << (caseId + 1) << ": ";
    cout << bestAnswer;
    cout << endl;
}

int check2(int* dist, uint64_t buildTime, int numStars, int distMod, int first, int second) {
    unsigned int time = 0;

    REP(pos, numStars) {
        int currentDist = dist[pos % distMod];
        unsigned int travelTime = 2 * currentDist;

        // Are we traveling from a boosted star?
        if (pos == first || pos == second) {
            // Booster finished before I arrived, so get the full speedup.
            if (time >= buildTime) {
                travelTime /= 2;
            }
            // Booster finished midway, apply a partial speedup.
            else if (time + travelTime >= buildTime) {
                unsigned int timeNoSpeed = buildTime - time;
                unsigned int distWithSpeed = currentDist - timeNoSpeed / 2;
                travelTime = timeNoSpeed + distWithSpeed;
            }
        }

        time += travelTime;
    }
    return time;
}

int main(int argc, char** argv) {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        run(i);
    }
    return 0;
}
