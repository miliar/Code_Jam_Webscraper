/**
   File: main.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

long long place(long long L, long long P, long long C, map<pair<long long,long long>, long long>& vMemo) {
    if (L*C >= P) return 0;

    if (vMemo.find(make_pair(L,P)) != vMemo.end()) return vMemo[make_pair(L,P)];

    long long iMin = 1000000;

    long long iVal = sqrtl((long long)L * (long long)P);

    for (long long i = std::max(iVal, L + 1); i <= iVal + 1; i++) {
        long long iNow1 = place(i, P, C, vMemo); // if supported
        long long iNow2 = place(L, i, C, vMemo); // not supported
        long long iNow = 1 + max(iNow1, iNow2);
        iMin = min(iMin, iNow);
    }
    return vMemo[make_pair(L,P)] = iMin;
}


long long calcResult() {
    long long L, P, C;
    cin >> L >> P >> C;

    if (L*C >= P) return 0;

    map<pair<long long,long long>, long long> vMemo;

    long long iMin = 1000000;

    long long iVal = sqrtl((long long)L * (long long)P);

    for (long long i = std::max(iVal, L + 1); i <= iVal + 1; i++) {
        long long iNow1 = place(i, P, C, vMemo); // if supported
        long long iNow2 = place(L, i, C, vMemo); // not supported
        long long iNow = 1 + max(iNow1, iNow2);
        if (iNow < iMin) {
            iMin = iNow;
        }
    }

    return iMin;
}

int main()
{
    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
//        calcResult();
//        break;
        cout << "Case #" << k << ": ";
        cout << calcResult() << endl;
    }
    return 0;
}
