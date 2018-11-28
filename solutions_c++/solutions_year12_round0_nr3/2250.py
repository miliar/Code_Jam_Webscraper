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

const int MAXN = 2000000 + 10;

int used[MAXN];

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int kOfTest;
    cin >> kOfTest;

    memset(used, 0, sizeof(used));

    for(int iTest = 1; iTest <= kOfTest; ++iTest) {
        int A, B;
        cin >> A >> B;
        long long result = 0;
        int pw10 = 1;
        while(A / pw10 > 0) pw10 *= 10;
        for(int i = A; i <= B; ++i)
            if(used[i] != iTest) {
                used[i] = iTest;
                long long k = 0;
                int pw = 10;
                while(pw < pw10) {
                    int x = (i % pw) * (pw10 / pw) + (i / pw);
                    if(x >= A && x <= B && used[x] != iTest) {
                        used[x] = iTest;
                        ++ k;
                        result += k;
                    }
                    pw *= 10;
                }
            }
            cout << "Case #" << iTest << ": " << result;
            if(iTest != kOfTest)
                cout << endl;
    }

    return 0;
}

