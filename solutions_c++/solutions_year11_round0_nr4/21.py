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

int T, N, trueN;

int main()
{
    ifstream in("D.in");
    ofstream out("D.out");
    
    in >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        in >> N;
        trueN = N;
        for (int i = 1; i <= N; ++i)
        {
            int elem;
            in >> elem;
            if (i == elem)
                trueN--;
        }
        
        out << "Case #" << tc << ": " << trueN << endl;
    }
}
