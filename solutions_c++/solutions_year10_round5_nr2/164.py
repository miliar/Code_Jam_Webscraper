/**
   File: B.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

long long solve(const vector<long long>& v, long long L) {

    if (L == 0) return 0;
    if (L < 0) return -1;

    int iMax = 1000000;

    vector<int> w(L+1, iMax);

    w[0] = 0;

    for (int i = 0; i < int(v.size()); i++) {
        for (int j = 0; j < L; j++) {
            if (w[j] != iMax && j + v[i] <= L) {
                w[j + v[i]] = min(w[j + v[i]], w[j] + 1);
            }
        }
    }

    if (iMax != w[L]) return w[L];
    return -1;
}


void calcResult() {
    long long L;
    int N;
    cin >> L >> N;
    vector<long long> v(N);
    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }

    long long mcd = v[0];
    for (int i = 0; i < N; i++) {
        mcd = gcd(mcd, v[i]);
    }

    if (L % mcd != 0) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        sort(v.begin(), v.end());
        long long R = L / v.back();

        long long lMin = -1;

        for (int i = 0; i < 100 || lMin == -1; i++) {
            long long lRes = solve(v, L - v.back() * (R - i));
            if (lRes != -1) {
                lRes += (R - i);
                if (lMin == -1) lMin = lRes;
                else lMin = std::min(lMin, lRes);
            }
        }

        cout << lMin << endl;
    }
}

int main()
{
    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
        cout << "Case #" << k << ": ";
        calcResult();
    }
    return 0;
}
