#include <iostream>
#include <string>

#define DEBUG

using namespace std;

inline unsigned SMIN(unsigned ek, unsigned don) {
    return (ek<don)?ek:don;
}

void doTest(int test) {
    unsigned N = 0U;
    cin >> N;
#ifdef DEBUG
    cerr << "test: " << test << " N = " << N << endl;
#endif

    unsigned num = 0U;
    cin >> num;
    unsigned minNum = num;
    unsigned actSum = num;
    unsigned xorSum = num;

    for (int n=1; n<N; ++n) {
        cin >> num;
        minNum = SMIN(minNum, num);
        actSum += num;
        xorSum ^= num;
    }

    // dump final result
    if (xorSum == 0U) {
        unsigned result = (actSum - minNum);
        cout << "Case #" << test << ": " << result << endl;
    } else {
        cout << "Case #" << test << ": NO" << endl;
    }
}

int main() {
    int T = 0;

    cin >> T;
#ifdef DEBUG
    cerr << "T = " << T << endl;
#endif

    for (int t=1; t<=T; ++t) {
        doTest(t);
    }

    return 0;
}

