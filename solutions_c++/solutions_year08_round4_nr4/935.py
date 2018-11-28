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

#define fori(i, n) for ( typeof(n) i = 0; i < (n); ++i )
#define forr(i, a, b) for ( typeof(a) i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( typeof(a) i = (a); i >= (b); --i )
#define tr(T, i) for ( typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

const double EPS = 1e-9;

int cmp( double x, double y = 0, double tol = EPS )
{
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int count (string s)
{
    int asw = 0;
    char c = '.';
    fori(i,s.sz)
    {
        if ( s[i] == c ) { continue; }
        c = s[i];
        asw++;
    }
    return asw;
}

string change(string s, vector<int> v)
{
    int N = v.sz;
    int C = (int) s.sz;
    int c = 0;
    string asw;
    while ( c < C )
    {
        string sub = s.substr(c, N);
        string aux = "";
        fori(i,N)
        {
            aux += sub[v[i]-1];
        }
        asw += aux;
        c += N;
    }
    return asw;
}

int main()
{
    int N;
    cin >> N;

    fori(cas, N)
    {
        int m, k;
        string s;
        cin >> k >> s;

        vector<int> v(k);
        fori(i,k) v[i] = i+1;

        int asw = INT_MAX;
        string aux = s;
        do
        {
            aux = change(s, v);
            m = count(aux);
            if ( m < asw ) asw = m;
        }   while (next_permutation(all(v)));


        cout << "Case #" << cas+1 << ": ";
        cout << asw << endl;
    }

    return 0;
}
