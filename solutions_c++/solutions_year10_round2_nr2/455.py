#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int main()
{
    int T = 20; 
    cin >> T;
    for (int testCase=1; testCase<=T; testCase++) {
        int N, K, B, T;
        cin >> N >> K >> B >> T;
        int *X = new int[N];
        for (int i=0; i<N; i++)
            cin >> X[i];
        int *V = new int[N];
        for (int i=0; i<N; i++)
            cin >> V[i];
        bool *t = new bool[N];
        for (int i=0; i<N; i++)
            if (V[i]*T<B-X[i])
                t[i] = false;
            else
                t[i] = true;
        int res = 0;
        int k = 0;
        for (int i=N-1; i>=0; i--)
            if (t[i]) {
                for (int j=i+1; j<N; j++)
                    if (!t[j])
                        res++;
                k++;
                if (k==K)
                    break;
            }
        if (k==K)
            cout << "Case #" << testCase << ": " << res << endl;
        else
            cout << "Case #" << testCase << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}
