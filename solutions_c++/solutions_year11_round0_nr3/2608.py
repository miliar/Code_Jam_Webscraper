#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;


#define DEBUGGING true

#define doubt if (DEBUGGING) cerr

#define foo(x) doubt << #x << ": " << x << endl;
#define loopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) \
                          doubt << #x << "[" << i2 << "]: " << x[i2] << endl;
#define looploopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) { \
                           for (int j2 = 0; j2 < x[i2].size(); j2++) \
                               doubt << '\t' << #x << "[" << i2 << "][" \
                                     << j2 << "]: " << x[i2][j2]; \
                           doubt << endl; }


int main(int argc, char** argv)
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        int N;
        cin >> N;

        vector<int> vals(N);

        for (int i = 0; i < N; i++)
            cin >> vals[i];

        int res = 0;
        for (int i = 0; i < N; i++)
            res ^= vals[i];

        int ans = 0;

        if (res == 0)
        {
            sort(vals.begin(), vals.end());
            for (int i = 1; i < vals.size(); i++)
                ans += vals[i];
        }

        cout << "Case #" << caseNum << ": ";
        if (res != 0)
            cout << "NO";
        else
            cout << ans;
        cout << endl;
    }

    return 0;
}
