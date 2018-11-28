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

int T, N, Pd, Pg;

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");
    
    in >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        in >> N >> Pd >> Pg;
        bool possible = false;
        
        for (int n = 1; n <= N; ++n)
        {
            int daywins = n*Pd;
            if (daywins % 100 != 0) continue;
            if (Pd > 0 && Pg == 0) continue;
            if (Pd < 100 && Pg == 100) continue;
            possible = true;
        }
        
        if (possible)
            out << "Case #" << tc << ": Possible" << endl;
        else
            out << "Case #" << tc << ": Broken" << endl;
    }
}
