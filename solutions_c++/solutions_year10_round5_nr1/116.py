#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 

vector<int> getPrime(int n) {
    vector<int> ret;
    FORE(i, 2, n) {
        bool ok = true;
        int k = (int)floor(sqrt((double)i)+EPS);
        for (unsigned int j = 0; j < ret.size() && ret[j] <= k; ++j) {
            if (i % ret[j] == 0) {
                ok = false;
                break;
            }
        }
        if (ok)
            ret.push_back(i);
    }
    return ret;
}

#define MAX_10D 10000
vector<int> primes;

int get10D(int d) {
    int ret = 1;
    REP(i, d)
        ret *= 10;
    return ret;
}

vector<int> getBCand(int A, int P, int S0, int S1) {
    vector<int> ret;
    int B0 = S1-(A*S0)%P;
    if (0 <= B0 && B0 < P && (A*S0)%P+B0 < P)
        ret.push_back(B0);
    int B1 = S1-(A*S0)%P+P;
    if (0 <= B1 && B1 < P && (A*S0)%P+B1 >= P)
        ret.push_back(B1);
    return ret;
}

int main(void) {
    primes = getPrime(MAX_10D);
    int T;
    cin >> T;
    REP(_t, T) {
        int D, K;
        cin >> D >> K;
        int d10 = get10D(D);
        vector<int> input(K);
        REP(i, K) {
            cin >> input[i];
            assert(input[i] < d10);
        }
        int next = -1;
        int S0 = input[0];
        int minP = *max_element(input.begin(), input.end());
        if (K >= 2) {
            REPV(primes, i) if (minP < primes[i] && primes[i] <= d10) {
                int P = primes[i];
                REP(A, P) {
                    vector<int> bcand = getBCand(A, P, input[0], input[1]);
                    REPV(bcand, _b) {
                        int B = bcand[_b];
                        bool ok = true;
                        int S = S0;
                        REP(k, K) {
                            if (input[k] != S) {
                                ok = false;
                                break;
                            }
                            S = (A*S+B)%P;
                        }
                        if (ok) {
                            if (next != -1 && next != S) {
                                next = -1;
                                goto end;
                            }
                            next = S;
                        }
                    }
                }
            }
        }
      end:
        cerr << _t+1 << endl;
        if (next == -1)
            cout << "Case #" << _t+1 << ": I don't know." << endl;
        else
            cout << "Case #" << _t+1 << ": " << next << endl;
    }
    return 0;
}

