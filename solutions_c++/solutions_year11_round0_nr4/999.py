#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>

using namespace std;

#define DEBUG

double cycleProbabilities[1002];
double ratios[1002];

void initialize() {
    cycleProbabilities[0] = 1.0;
    cycleProbabilities[1] = 0.0;
    ratios[0] = 1.0;
    ratios[1] = 1.0;
    int sign = 1;
    for (unsigned idx = 2U; idx < 1001;  ++idx) {
        ratios[idx] = ratios[idx-1]/idx;
        cycleProbabilities[idx] = cycleProbabilities[idx-1] + sign*ratios[idx];
#ifdef DEBUG
        cerr << "idx = " << idx << " ratio = " << ratios[idx] << ", cycprob " << cycleProbabilities[idx] << endl;
#endif
        sign = -sign;
    }
}

void doTest(unsigned test) {
    unsigned N = 0U;
    cin >> N;
#ifdef DEBUG
    cerr << "Test " << test << " > N = " << N << endl;
#endif

    unsigned numbers[N+1];
    for (unsigned n=1U; n<=N; ++n) {
        cin >> numbers[n];
#ifdef DEBUG
        cerr << " #" << n << " = " << numbers[n] << endl;
#endif
    }

    vector< set<unsigned> > cycles;
    set<unsigned> used;

    unsigned idx = 0U, startIdx = 1U;
    while ((startIdx <= N) && (used.size() < N)) {

        while ((used.find(startIdx) != used.end()) && (startIdx <= N)) {
            ++startIdx;
        }

        if (startIdx <= N) {
            set<unsigned> emptyCycle;
            cycles.push_back(emptyCycle);

#ifdef DEBUG
            cerr << "Curr Cycle " << idx << " -> startIdx = " << startIdx << endl;
#endif
            set<unsigned> &currCycle = cycles[idx];
            unsigned currElem = startIdx;
            while (currCycle.find(currElem) == currCycle.end()) {
                currCycle.insert(currElem);
                used.insert(currElem);
                currElem = numbers[currElem];
#ifdef DEBUG
            cerr << " nextElem = " << currElem << endl;
#endif
            }
            ++idx;
        }
    }
    unsigned sum = 0U, cnt = 0U;
    for (unsigned cyidx = 0U; cyidx < cycles.size(); ++cyidx) {
        unsigned sz = cycles[cyidx].size();
        if (sz > 1U) {
            sum += sz;
            ++cnt;
#ifdef DEBUG
            cerr << " candidate cycle " << cyidx << " with size = " << sz << endl;
            cerr << "   curr sum = " << sum << " cnt = " << cnt << endl;
#endif
        }
    }

    //double result = 2.0*(sum-cnt);
    double result = sum;
    printf("Case #%d: %.6lf\n", test, result);
}

int main() {
    unsigned T=0U;
    cin >> T;
#ifdef DEBUG
    cerr << "T = " << T << endl;
#endif
    for (unsigned t=1U; t<=T; ++t) {
        doTest(t);
    }
    return 0;
}
