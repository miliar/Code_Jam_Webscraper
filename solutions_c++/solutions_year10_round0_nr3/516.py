#include <iostream>
#include <map>

using namespace std;

void doCase(int caseNum) {
    long R, k, N;

    cin >> R >> k >> N;

    long g[N];

    for (long i = 0; i < N; ++i) {
        cin >> g[i];
    }

    long start = 0;

    map<long, long> numPeopleStartingAt;
    map<long, long> nextStart;
    long numRuns = 0;
    long totalPeople = 0;

    do {
        long i = start;
        long numPeople = 0;
        bool full = false;
        do {
            if (numPeople + g[i] <= k) {
                numPeople += g[i];
                i = (i + 1) % N;
            } else {
                full = true;
            }

        } while (!full && i != start);

        numPeopleStartingAt[start] = numPeople;
        nextStart[start] = i;
        start = i;
        numRuns++;
        totalPeople += numPeople;
    } while (numRuns < R && numPeopleStartingAt.count(start) == 0);

    if (numRuns < R) {
        // Calculate a cycle
        long peoplePerCycle = 0;
        long runsPerCycle = 0;
        long j = start;
        do {
            peoplePerCycle += numPeopleStartingAt[j];
            runsPerCycle++;
            j = nextStart[j];
        } while (j != start);

        long remaining = R - numRuns;

        long fullCycles = remaining / runsPerCycle;
        long tail = remaining % runsPerCycle;
        totalPeople += fullCycles * peoplePerCycle;

        j = start;
        while (tail > 0) {
            totalPeople += numPeopleStartingAt[j];
            j = nextStart[j];
            tail--;
        }
    }

    cout << "Case #" << caseNum << ": " << totalPeople << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
