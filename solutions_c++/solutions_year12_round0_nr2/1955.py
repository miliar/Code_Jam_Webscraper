#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

struct Googler {
    int max_with_exception;
    int max_no_exception;
};

bool cmp(Googler const& g1, Googler const& g2) {
    return g1.max_with_exception > g2.max_with_exception;
}
int solve(vector<int>& scores, int exceptions, int target) {
    size_t const sz = scores.size();
    vector<Googler> googlers(sz);
    for (int i = 0; i < sz; ++i) {
        int base = scores[i] / 3;
        int remainder = scores[i] % 3;
        if (scores[i] == 0) {
            googlers[i] = {0, 0};
            continue;
        }
        if (remainder == 0) {
            googlers[i] = {base + 1, base};
        } else if (remainder == 1) {
            googlers[i] = {base + 1, base + 1};
        } else {
            googlers[i] = {base + 2, base + 1};
        }
    }
    sort(googlers.begin(), googlers.end(), cmp);
    int sol = 0;
    for (int i = 0; i < sz; ++i) {
        if (googlers[i].max_no_exception >= target) {
            ++sol;
        } else if (exceptions > 0 && googlers[i].max_with_exception >= target) {
            ++sol;
            --exceptions;
        }
    }
    return sol;
}

int main() {
    int tests = 0;
    scanf("%d", &tests);
    for (int t = 0; t < tests; ++t) {
        int numGooglers = 0;
        int numSurprising = 0;
        int p = 0;
        scanf("%d %d %d", &numGooglers, &numSurprising, &p);
        vector<int> scores(numGooglers);
        for (int i = 0; i < numGooglers; ++i) {
            scanf("%d", &scores[i]);
        }
        printf("Case #%d: %d\n", t + 1, solve(scores, numSurprising, p));
    }
    return 0; } 
