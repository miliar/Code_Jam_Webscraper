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

int T, N;
int d[10002], l[10002];
int maxl[10002];

int main()
{
    ios::sync_with_stdio(0);
    ifstream in("A.in");
    ofstream out("A.out");
    //out << fixed << setprecision(12);
    in >> T;
    for (int z = 1; z <= T; ++z)
    {
       in >> N;
       for (int i = 0; i < N; ++i)
           in >> d[i] >> l[i];
       in >> d[N]; l[N] = 0;
       maxl[0] = d[0];
       for (int i = 1; i <= N; ++i)
       {
           maxl[i] = -1;
           for (int j = 0; j < i; ++j)
           if (maxl[j] >= d[i] - d[j])
               maxl[i] = max(maxl[i], min(l[i], d[i] - d[j]));
       }
       if (maxl[N] >= 0)
           out << "Case #" << z << ": YES" << endl;
       else
           out << "Case #" << z << ": NO" << endl;
    }
}
