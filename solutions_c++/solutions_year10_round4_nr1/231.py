/* 
 * File:   Elegant_Diamond.cpp
 * Author: kimi
 *
 * Created on June 5, 2010, 10:15 PM
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <climits>
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

string Filename = "A-large";

int data[200][200], test[200][200];

bool checkH(int size) {
    for (int i = 0; i < size - 1; i++)
        for (int j = 0; j <= i; j++)
            if (test[i][j] != test[2 * size - 2 - i][j]) return false;
    return true;
}

bool checkV(int size) {
    for (int i = 0; i < 2 * size - 1; i++)
        for (int j = 0; j < min(i + 1, 2 * size - 1 - i) / 2; j++)
            if (test[i][j] != test[i][min(i + 1, 2 * size - 1 - i) - j - 1]) return false;
    return true;
}

int main() {
    freopen((Filename + ".in").c_str(), "r", stdin);
    freopen((Filename + ".out").c_str(), "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int k;
        scanf("%d", &k);
        for (int i = 0; i < 2 * k - 1; i++) {
            for (int j = 0; j < min(i + 1, 2 * k - 1 - i); j++)
                scanf("%d", &data[i][j]);
        }

        int H = 0, V = 0;
        for (int L = 1; L <= k; L++) {
            Fill(test, 0);
            for (int i = 0; i < L; i++)
                for (int j = 0; j <= i; j++)
                    test[i][j] = data[i][j];
            int delta = 0;
            for (int i = L; i < 2 * L - 1; i++) {
                delta++;
                if (i >= k) delta--;
                for (int j = 0; j < 2 * L - 1 - i; j++)
                    test[i][j] = data[i][j + delta];
            }
            if (checkH(L)) H = max(H, L);
        }

        for (int L = 1; L <= k; L++) {
            Fill(test, 0);
            for (int i = 0; i < L; i++)
                for (int j = 0; j <= i; j++)
                    test[i][j] = data[2 * k - 2 - i][j];
            int delta = 0;
            for (int i = L; i < 2 * L - 1; i++) {
                delta++;
                if (i >= k) delta--;
                for (int j = 0; j < 2 * L - 1 - i; j++)
                    test[i][j] = data[2 * k - 2 - i][j + delta];
            }
            if (checkH(L)) H = max(H, L);
        }

        for (int L = 1; L <= k; L++) {
            Fill(test, 0);
            for (int i = 0; i < L; i++)
                for (int j = 0; j <= i; j++)
                    test[i][j] = data[i - L + k][j];
            for (int i = L; i < 2 * L - 1; i++)
                for (int j = 0; j < 2 * L - 1 - i; j++)
                    test[i][j] = data[i - L + k][j];
            if (checkV(L)) V = max(V, L);
        }

        for (int L = 1; L <= k; L++) {
            Fill(test, 0);
            for (int i = 0; i < L; i++)
                for (int j = 0; j <= i; j++)
                    test[i][j] = data[i - L + k][j + k - L];
            for (int i = L; i < 2 * L - 1; i++)
                for (int j = 0; j < 2 * L - 1 - i; j++)
                    test[i][j] = data[i - L + k][j + k - L];
            if (checkV(L)) V = max(V, L);
        }
        int s = 3 * k - H - V;
        printf("Case #%d: %d\n", t + 1, s * s - k * k);

    }
    return (EXIT_SUCCESS);
}
