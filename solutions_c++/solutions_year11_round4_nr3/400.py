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
#define NMAX 1000000

using namespace std;
typedef long long ll;

ll T, N;
bool isPrime[NMAX];
vector<ll> primes;

int main()
{
    ifstream in("C.in");
    ofstream out("C.out");
    
    isPrime[0] = isPrime[1] = false;
    isPrime[2] = true;
    primes.push_back(2);
    for (ll i = 3; i < NMAX; ++i)
        isPrime[i] = (i % 2 == 1);
    
    for (ll i = 3; i < NMAX; i += 2)
    {
        if (!isPrime[i])
            continue;
        for (ll j = i*i; j < NMAX; j += 2*i)
            isPrime[j] = false;
        primes.push_back(i);
    }
    
    in >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        in >> N;
        int res = (N > 1)?1:0;
        for (int i = 0; i < primes.size() && primes[i]*primes[i] <= N; ++i)
        {
            ll p = primes[i]*primes[i];
            while (p <= N)
            {
                p *= primes[i];
                res++;
            }
        }
        out << "Case #" << tc << ": " << res << endl;
    }
}
