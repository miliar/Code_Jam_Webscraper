#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <ctime>
using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define forit(i, T) for (typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

long long calc(vector<int> v1, vector<int> v2)
{
    long long asw = 0;
    fori(i,v1.sz) asw += v1[i] * v2[i];
    return asw;
}

int main()
{
    int T, N;
    cin >> T;

    fori(count,T)
    {
        int res, n, asw = INT_MAX;
        cin >> n;
        vector<int> v1(n), v2(n);
        fori(i,n) cin >> v1[i];
        fori(i,n) cin >> v2[i];

        _sort(v1);
        _sort(v2);

        do
        {
            res = calc(v1,v2);
            if ( res < asw ) asw = res;
        }   while (next_permutation(all(v1)));

        cout << "Case #" << count+1 << ": " << asw << endl;
    }
    return 0;
}
