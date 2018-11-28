/* 
 * File:   Fair_Warning.cpp
 * Author: kimi
 *
 * Created on May 8, 2010, 4:23 PM
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

const int MAX_N = 1000;

vector<int> number[MAX_N];

vector<int> Convert(string s) {
    vector<int> rst;
    for (int i = s.size() - 1; i >= 0; i--)
        rst.pb(s[i] - '0');
    return rst;
}

int checkNumber(vector<int> vl, vector<int> vr) {
    if (vl.size() > vr.size()) return 1;
    if (vl.size() < vr.size()) return -1;
    int SIZE = vl.size();
    for (int i = SIZE - 1; i >= 0; i--) {
        if (vl[i] > vr[i]) return 1;
        if (vl[i] < vr[i]) return -1;
    }
    return 0;

}

bool judgeIsLargerThan(vector<int> vl, vector<int> vr) {
    return checkNumber(vl, vr) > 0;
}

bool judgeIsNotLessThan(vector<int> vl, vector<int> vr) {
    return checkNumber(vl, vr) >= 0;
}

vector<int> Minus(vector<int> vl, vector<int> vr) {
    vector<int> rst;
    rst.pb(0);
    int SIZE = vl.size();
    for (int i = 0; i < SIZE; i++) {
        rst[i] += vl[i];
        if (i < vr.size()) rst[i] -= vr[i];
        rst.pb(0);
        while (rst[i] < 0) {
            rst[i] += 10;
            rst[i + 1]--;
        }
    }
    while (!rst.empty() && !rst.back()) rst.pop_back();
    return rst;
}

vector<int> getGcd(vector<int> vl, vector<int> vr) {
    while (1) {
        if (judgeIsLargerThan(vr, vl)) {
            vector<int> temp;
            temp = vr;
            vr = vl;
            vl = temp;
        }
        if (!vr.size()) return vl;
        while (judgeIsNotLessThan(vl, vr)) vl = Minus(vl, vr);
    }
}

void printv(vector<int> v) {
    int SIZE = v.size();
    if (!SIZE) printf("0");
    else for (int i = SIZE - 1; i >= 0; i--) printf("%d", v[i]);
}

void printResult(int t, vector<int> v) {
    printf("Case #%d: ", t);
    printv(v);
    printf("\n");
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        for (int i = 0; i < N; i++) {
            string A;
            cin >> A;
            number[i] = Convert(A);
        }
        N--;
        for (int i = 0; i < N; i++)
            if (judgeIsLargerThan(number[i], number[i + 1]))
                number[i] = Minus(number[i], number[i + 1]);
            else number[i] = Minus(number[i + 1], number[i]);
        for (int i = 1; i < N; i++)
            number[0] = getGcd(number[0], number[i]);
        while (judgeIsLargerThan(number[N], number[0]))
            number[N] = Minus(number[N], number[0]);
        printResult(t + 1, Minus(number[0], number[N]));
    }
    return (EXIT_SUCCESS);
}
