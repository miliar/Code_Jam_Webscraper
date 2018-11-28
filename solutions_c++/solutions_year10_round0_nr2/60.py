#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <gmp.h>
#ifdef HOME_RUN
# include <debug.hpp>
# include <dump.hpp>
# include <cassert>
#else
# define TR(x) do{}while(0)
# ifdef assert
#  indef assert
# endif
# define assert(x) do{}while(0)
#endif
using namespace std;

#define ALL(C) (C).begin(), (C).end()
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long i64;
typedef unsigned long long u64;

inline istream& skip_endl(istream& in)
{
    string s;
    getline(in, s);
    forIter( i, s ) assert(isspace(*i));
    return in;
}

inline string get_str()
{
    string ret;
    getline(cin, ret);
    return ret;
}

map<string, int> str_index;
int get_index(const string& s)
{
    return str_index.insert(make_pair(s, str_index.size())).first->second;
}
int get_str_index()
{
    return get_index(get_str());
}

#if 1
inline u64 mul64(unsigned a, unsigned b)
{
    u64 ret;
    asm("mul %[b];\n"
        : "=A" (ret)
        : [a] "%a" (a), [b] "r" (b)
        );
    return ret;
}

inline unsigned div64(u64 a, unsigned n)
{
    unsigned div, mod;
    asm("div %[n];\n"
        : "=a" (div), "=d" (mod)
        : "A" (a), [n] "r" (n)
        );
    return div;
}

inline unsigned mod64(u64 a, unsigned n)
{
    unsigned div, mod;
    asm("div %[n];\n"
        : "=a" (div), "=d" (mod)
        : "A" (a), [n] "r" (n)
        );
    return mod;
}

struct NUM {
    vector<unsigned> dd;
    bool operator==(unsigned v) const {
        return dd.empty() && v == 0 || dd.size() == 1 && dd[0] == v;
    }
    bool operator!=(unsigned v) const {
        return !(*this == v);
    }
    void operator*=(unsigned v) {
        unsigned c = 0;
        forIter ( i, dd ) {
            u64 t = mul64(*i, v)+c;
            *i = t;
            c = t >> 32;
        }
        if ( c ) dd.push_back(c);
    }
    unsigned operator/=(unsigned v) {
        unsigned c = 0;
        for ( int i = dd.size(); i--; ) {
            u64 t = (u64(c)<<32)|dd[i];
            c = t%v;
            dd[i] = t/v;
        }
        while ( *this != 0 && dd.back() == 0 ) dd.pop_back();
        return c;
    }
    void operator>>=(unsigned s) {
        unsigned x = s/32;
        s %= 32;
        if ( x ) {
            if ( dd.size() <= x ) {
                dd.clear();
                return;
            }
            dd.erase(dd.begin(), dd.begin()+x);
        }
        unsigned c = 0;
        for ( int i = dd.size(); i--; ) {
            u64 t = (u64(c)<<32)|dd[i];
            c = t;
            dd[i] = t >> s;
        }
        while ( *this != 0 && dd.back() == 0 ) dd.pop_back();
    }
    void operator<<=(unsigned s) {
        unsigned x = s/32;
        s %= 32;
        *this *= 1<<s;
        dd.insert(dd.begin(), x, 0);
    }
    void operator+=(unsigned v) {
        if ( dd.empty() ) {
            if ( v ) dd.push_back(v);
            return;
        }
        unsigned c = v;
        forIter ( i, dd ) {
            u64 t = u64(*i)+c;
            *i = t;
            c = t >> 32;
        }
        if ( c ) dd.push_back(c);
    }
    void operator-=(const NUM& b) {
        if ( dd.size() < b.dd.size() ) abort();
        unsigned c = 0;
        forN ( i, b.dd.size() ) {
            i64 t = i64(dd[i])-b.dd[i]-c;
            dd[i] = t;
            c = t < 0;
        }
        if ( c ) {
            forNF ( i, b.dd.size(), dd.size() ) {
                if ( dd[i]-- ) {
                    c = 0;
                    break;
                }
            }
            if ( c ) abort();
        }
        while ( dd.size() && dd.back() == 0 ) dd.pop_back();
    }
    bool operator>(const NUM& b) const
    {
        if ( dd.size() != b.dd.size() ) return dd.size() > b.dd.size();
        for ( int i = dd.size(); i--; ) {
            if ( dd[i] != b.dd[i] ) return dd[i] > b.dd[i];
        }
        return 0;
    }
    bool operator>=(const NUM& b) const
    {
        if ( dd.size() != b.dd.size() ) return dd.size() > b.dd.size();
        for ( int i = dd.size(); i--; ) {
            if ( dd[i] != b.dd[i] ) return dd[i] > b.dd[i];
        }
        return 1;
    }
    void operator%=(NUM b) {
        unsigned s = 0;
        while ( *this >= b ) {
            ++s;
            b <<= 1;
        }
        while ( s ) {
            --s;
            b >>= 1;
            if ( *this >= b )
                *this -= b;
        }
    }
};
ostream& operator<<(ostream& out, NUM n)
{
    string s;
    while ( n != 0 ) {
        s += char((n /= 10) + '0');
        //cerr << s << " " << n.dd << endl;
    }
    reverse(ALL(s));
    if ( s.empty() ) s = "0";
    out << s;
    return out;
}
istream& operator>>(istream& in, NUM& n)
{
    string s;
    n.dd.clear();
    if ( in >> s ) {
        //cerr << s << endl;
        forIter ( i, s ) {
            n *= 10;
            //cerr << *i << ": " << n.dd << " " << n << endl;
            n += *i-'0';
            //cerr << *i << ": " << n.dd << " " << n << endl;
        }
    }
    //cerr << n.dd << " " << n << endl;
    return in;
}
NUM operator-(const NUM& a, const NUM& b)
{
    NUM r = a;
    r -= b;
    return r;
}
NUM operator<<(const NUM& a, unsigned s)
{
    NUM r = a;
    r <<= s;
    return r;
}
unsigned operator&(const NUM& a, unsigned b)
{
    return a == 0? 0: a.dd[0] & b;
}
unsigned operator&(unsigned b, const NUM& a)
{
    return a == 0? 0: a.dd[0] & b;
}
#else
typedef u64 NUM;
#endif

int N;

vector<NUM> tt;

// binary gcd
template<typename T>
T gcd(T a, T b)
{
    //if ( a < 0 ) a = -a;
    //if ( b < 0 ) b = -b;
    int s = 0;
    while ( a != 0 && b != 0 ) {
        if ( 1&a&b ) {
            if ( a > b )
                a -= b;
            else
                b -= a;
        }
        if ( !((a&1)|(b&1)) ) ++s;
        if ( !(a&1) ) a >>= 1;
        if ( !(b&1) ) b >>= 1;
    }
    return (a != 0? a: b)<<s;
}

NUM diff(const NUM& a, const NUM& b)
{
    return a > b? a-b: b-a;
}

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        // parse input
        cin >> N;
        tt.resize(N);
        forN ( i, N ) {
            cin >> tt[i];
        }
        cin >> skip_endl;

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        NUM g = diff(tt[1], tt[0]);
        forNF ( i, 2, N )
            g = gcd(g, diff(tt[i], tt[0]));
        NUM y = tt[0];
        y %= g;
        if ( y != 0 ) y = g-y;

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << y;
        cout << endl;
    }
}
