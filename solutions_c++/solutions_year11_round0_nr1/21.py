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
#include <fstream>

using namespace std;
typedef long long ll;

int T, N, P;
char R;

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");
    
    in >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        in >> N;
        int bPos = 1, oPos = 1, bTime = 0, oTime = 0, totalTime = 0;
        
        for (int i = 0; i < N; ++i)
        {
            in >> R >> P;
            if (R == 'B')
            {
                bTime = min(0, bTime - abs(bPos - P)) - 1;
                bPos = P;
                if (bTime < 0)
                {
                    totalTime -= bTime;
                    oTime -= bTime;
                }
                bTime = 0;
            }
            else
            {
                oTime = min(0, oTime - abs(oPos - P)) - 1;
                oPos = P;
                if (oTime < 0)
                {
                    totalTime -= oTime;
                    bTime -= oTime;
                }
                oTime = 0;
            }
        }
        out << "Case #" << tc << ": " << totalTime << endl;
    }
}
