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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define MOD 1000000007
#define INF 0x3f3f3f3f

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef complex<ll> pt;

int T, N, W, L;
ld r[100000];
ld x[10], y[10];

int main()
{
    ios::sync_with_stdio(0);
    ifstream in("B.in");
    ofstream out("B.out");
    out << fixed << setprecision(9);
    in >> T;
    srand( time(NULL) );
    for (int z = 1; z <= T; ++z)
    {
       in >> N >> W >> L;
       for (int i = 0; i < N; ++i)
           in >> r[i];
       bool good = false;
       while (!good)
       {
           for (int i = 0; i < N; ++i)
           {
               x[i] = 1e-3+(W-2e-3)*ld(rand())/RAND_MAX;
               y[i] = 1e-3+(L-2e-3)*ld(rand())/RAND_MAX;
           }
           good = true;
           for (int i = 0; i < N && good; ++i)
           for (int j = 0; j < i && good; ++j)
               if ((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]) < (r[i]+r[j])*(r[i]+r[j])*(2))
                   good = false;
       }
       out << "Case #" << z << ":";
       for (int i = 0; i < N; ++i)
           out << ' ' << x[i] << ' ' << y[i];
       out << endl;
    }
}
