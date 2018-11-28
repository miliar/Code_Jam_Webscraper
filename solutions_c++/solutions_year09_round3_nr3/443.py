#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <bitset>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
#include <stack>
#include <deque>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

int solve(int P, vector <int> tbr)
{
    int bestBribe = -1;
    vector <int> tbr2(tbr);
    for (; tbr != tbr2 || bestBribe == -1;
        next_permutation(tbr2.begin(), tbr2.end()))
    {
        int bribe = 0;
        vector <int> cells(P, 0);
        for (int i = 0; i < tbr2.size(); ++i)
        {
            cells[tbr2[i] - 1] = -1;
            for (int j = tbr2[i] - 2; j >= 0; --j)
            {
                if (cells[j] == -1)
                    break;
                ++bribe;
            }
            for (int j = tbr2[i]; j < cells.size(); ++j)
            {
                if (cells[j] == -1)
                    break;
                ++bribe;
            }
        }
        
        if (bestBribe == -1 || bribe < bestBribe)
            bestBribe = bribe;
    }
    
    return bestBribe;
}

int main()
{
    int N;
    cin >> N;
    
    for (int i = 0; i < N; ++i)
    {
        int P, Q;
        cin >> P >> Q;
        vector <int> toBeReleased(Q);
        for (int j = 0; j < Q; cin >> toBeReleased[j++]);
        cout << "Case #" << (i + 1) << ": " << solve(P, toBeReleased) << endl;
    }
    
    return 0;
}
