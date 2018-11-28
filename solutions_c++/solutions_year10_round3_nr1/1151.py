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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool miordenar (pair <int, int> a, pair <int, int> b)
{
    return a.first < b.first;
}

int main ()
{
    int T, A, B, N, r, l;
    cin >> T;


    for (int k = 1; k <= T; k++)
    {
        cout << "Case #" << k << ": ";
        cin >> N;
        vector <pair <int, int> > A (N);

        for (int i = 0; i < N; i++)
        {
            cin >> r >> l;
            A[i] = pair <int, int> (r, l);
        }

        sort (A.begin(), A.end(), miordenar);

        int contador = 0;
        for (int i = 0; i < N; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                if (A[i].second > A[j].second) contador++;
            }
        }

        cout << contador << endl;
    }
    return 0;
}
