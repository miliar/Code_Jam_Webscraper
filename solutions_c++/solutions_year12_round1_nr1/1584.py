#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>

using namespace std;

typedef long long ll;

//#define LARGE

int A;
int B;

double probability[99999];

double solve(){

    double ret;

    double p = 1.0;
    for (int i = 0; i < A; i++){
        p *= probability[i];
    }
    ret = p * ((B - A) + 1.0) + (1.0 - p) * ((B - A) + 1.0 + B + 1.0);

    for (int i = 1; i <= A; i++){
        p = 1.0;
        for (int j = 0; j < A - i; j++){
            p *= probability[j];
        }
        double tmp;
        if (i != A){
            tmp = p * ((double)i + B - (A - (double)i) + 1.0) + (1.0 - p) * ((double)i + B - (A - (double)i) + 1.0 + B + 1.0);
        } else {
            tmp = A + B + 1;
        }
        ret = min(ret, tmp);
    }

    double tmp = 1.0 + B + 1.0;
    ret = min(ret, tmp);

    return ret;
}

int main() {
#ifdef LARGE
    FILE *file = fopen("A-large.txt", "w");
#else
    FILE *file = fopen("A-small.txt", "w");
#endif
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> A;
        cin >> B;
        for (int a = 0; a < A; a++){
            cin >> probability[a];
            cout << probability[a] << endl;
        }
        fprintf(file, "Case #%d: %f\n", t + 1, solve());
    }
    fclose(file);
    return 0;
}
