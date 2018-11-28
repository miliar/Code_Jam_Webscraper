#include <functional>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cmath>
#include <ctime>

#include <numeric>
#include <iomanip>
#include <complex>
#include <float.h>
#include <cfloat>

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <cstdio>

#include <cstring>
#include <string>

#include <iterator>
#include <vector>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

const int MAXN = 100 + 10;
const int MAXS = 100 + 10;
const int INF = 1000000000;

class Triple {
    public:
        Triple(int A, int B, int C, int P) {
            surprising = nice = 0;
            if(abs(A - B) == 2 || abs(A - C) == 2 || abs(B - C) == 2)
                surprising = 1;
            if(abs(A - B) > 2 || abs(A - C) > 2 || abs(B - C) > 2)
                surprising = -1;
            if(max(A, max(B, C)) >= P)
                nice = 1;
            judgeA = A, judgeB = B, judgeC = C;
        }

    public:
        int judgeA, judgeB, judgeC, surprising, nice;
};

int T[MAXN], dp[MAXN][MAXS];
vector< vector<Triple> > googlers;

vector<Triple> genPoints(int T, int P) {
    vector<Triple> resultGooglers;
    resultGooglers.clear();

    for(int A = 0; A <= 10; ++A)
        for(int B = 0; B <= 10; ++B)
            for(int C = 0; C <= 10; ++C)
                if(A + B + C == T) {
                    Triple googler(A, B, C, P);
                    if(googler.surprising >= 0)
                        resultGooglers.push_back(googler);
                }

    return resultGooglers;
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int kOfTest;
    cin >> kOfTest;

    for(int iTest = 1; iTest <= kOfTest; ++iTest) {
        int N;
        cin >> N;

        int S;
        cin >> S;

        int P;
        cin >> P;

        for(int i = 1; i <= N; ++i)
            cin >> T[i];

        googlers.clear();
        for(int i = 1; i <= N; ++i)
            googlers.push_back(genPoints(T[i], P));

        for(int i = 0; i <= N; ++i)
            for(int j = 0; j <= S; ++j)
                dp[i][j] = 0;

        dp[0][0] = 0;
        for(int i = 0; i < N; ++i)
            for(int j = 0; j <= S; ++j)
                if(dp[i][j] > -INF)
                    for(int q = 0; q < googlers[i].size(); ++q) {
                        int su = googlers[i][q].surprising;
                        int ni = googlers[i][q].nice;
                        if(j + su <= S && dp[i][j] + ni > dp[i + 1][j + su])
                            dp[i + 1][j + su] = dp[i][j] + ni;
                    }

         cout << "Case #" << iTest << ": " << dp[N][S];

         if(iTest < kOfTest)
             cout << endl;
    }

    return 0;
}

