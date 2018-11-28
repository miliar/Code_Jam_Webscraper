/**
   File: A.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <queue>

using namespace std;

vector<int> pr;

void gen() {
    long long N = 1000000;
    vector<int> v(N);

    pr.push_back(2);

    for (long long i = 3; i < N; i+=2) {
        if (v[i] == 0) {
            pr.push_back(i);
            for (long long j = i*i; j < N; j += 2*i) {
                v[j] = 1;
            }
        }
    }
}

bool checkB(long long A, long long B, long long P, vector<long long>& v) {

    long long S = v[0];

    for (int i = 0; i < int(v.size()); i++) {
        if (v[i] != S) return false;
        S = (S*A + B) % P;
    }
    return true;
}

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}


bool check(long long P, vector<long long>& v) {

    for (int i = 1; i < int(v.size()) - 1; i++) {
        long long a = v[i] - v[i-1];
        a = (a % P + P) % P;
        long long b = v[i+1] - v[i];
        b = (b % P + P) % P;
        if (b % gcd(a, P) != 0) {
            return false;
        }
    }

    for (int i = 1; i < int(v.size()) - 1; i++) {
        long long a = v[i] - v[i-1];
        a = (a % P + P) % P;
        long long b = v[i]*v[i] - v[i+1]*v[i-1];
        b = (b % P + P) % P;
        if (b % gcd(a, P) != 0) {
            return false;
        }
    }


    return true;
}

bool checkA(long long A, long long P, vector<long long>& v) {
    return true;
}




void calcResult() {
    long long D, K;
    cin >> D >> K;
    vector<long long> v(K);
    for (int i = 0; i < K; i++) cin >> v[i];

    if (K == 1) {
        cout << "I don't know." << endl;
        return;
    }

    int iResult = -1;

    int maxP = 1;
    while (D--) maxP *= 10;

    long long iMaxNum = 0;
    for (int i = 0; i < int(v.size()); i++) {
        iMaxNum = std::max(v[i], iMaxNum);
    }

    for (int i = 0; i < int(pr.size()) && pr[i] < maxP; i++) {
        long long P = pr[i];
        if (P > iMaxNum && check(P, v)) {
            for (long long A = 0; A < P; A++) {
                if (checkA(A, P, v)) {
                    long long B = (((v[1] - A * v[0]) % P)  + P) % P;
                    if (checkB(A, B, P, v)) {
                        int iNewResult = (v.back() * A + B) % P;
                        if (iResult == -1) {
                            iResult = iNewResult;
                        }
                        if (iResult != iNewResult) {
//                            cerr << "Here" << endl;
                            cout << "I don't know." << endl;
                            return;
                        }
                    }
                }
            }
        }
    }

    if (iResult == -1) {
        cout << "I don't know." << endl;
    }
    else {
        cout << iResult << endl;
    }
}

int main()
{
    gen();

    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
        cerr << k << " " << N << endl;
        cout << "Case #" << k << ": ";
        calcResult();
    }
    return 0;
}
