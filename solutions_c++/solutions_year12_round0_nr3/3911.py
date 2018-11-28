#include <iostream>
#include <cstdio>
#include <bitset>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <deque>
#include <vector>
#include <cstdlib>
#include <cassert>
#include <ctime>

#define var(x) #x
#define forn(i, n) for (int i = 0; i < ((int) n); ++i)
#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) (x)*(x)
#define all(x) x.begin(), x.end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'
#define sp ' '
#define elif else if
#define len(x) ((int) (x).size())
#define last(x) ((x)[(len(x))-1])
#define plast(x) ((x)[(len(x))-2])

using namespace std;

typedef long long int64;
typedef unsigned long long lint;
typedef long double ld;

template<typename type>
inline static void _cutedebug(const type &a){
	cerr << a;
}
template<typename type1, typename type2>
inline static void _cutedebug(const pair<type1, type2> &a){
	cerr << "("; _cutedebug(a.fs); cerr << ", "; _cutedebug(a.sc); cerr << ")";
}
template<typename type>
inline static void _cutedebug(const vector<type> &a){
	cerr << "[";
	bool flag = true;
	for (typename vector<type>::const_iterator i = a.begin(); i != a.end(); i++){
		if (flag)
			flag = false;
		else
			cerr << ", ";
		_cutedebug(*i);
	}
	cerr << "]";
}
template<typename type>
inline static void _cutedebug(const set<type> &a){
	cerr << "{";
	bool flag = true;
	for (typename set<type>::const_iterator i = a.begin(); i != a.end(); i++){
		if (flag)
			flag = false;
		else
			cerr << ", ";
		_cutedebug(*i);
	}
	cerr << "}";
}
template<typename type1, typename type2>
inline static void _cutedebug(const map<type1, type2> &a){
	cerr << "{";
	bool flag = true;
	for (typename map<type1, type2>::const_iterator i = a.begin(); i != a.end(); i++){
		if (flag)
			flag = false;
		else
			cerr << ", ";
		cerr << "(";
		_cutedebug((*i).fs);
		cerr << ": ";
		_cutedebug((*i).sc);
		cerr << ")";
	}
	cerr << "}";
}
#ifdef CUTEBMAING
template<typename type>
inline static void _cutedebug_(const type &a, string name, int ln = __LINE__){
	cerr << "Line " << ln << " : " << name << " = "; _cutedebug(a); cerr << ";" << endl;
}
#define debug(x) _cutedebug_(x, var(x), __LINE__)
#endif
#ifndef CUTEBMAING
#define debug(x) {;}
#endif

const char* fin = "input.txt";
const char* fout = "output.txt";

const int inf = (1 << 30);
const int64 linf = (int64(1) << 61);
const int maxn = 3 * (int) 1e+6;

vector<vector<int> > a;

string to_str(int x){
    string res = "";
    while (x > 0){
        res += (char) (x % 10 + '0');
        x /= 10;
    }
    reverse(all(res));
    return res;
}

int to_int(string s){
    int res = 0;
    for (int i = 0; i < len(s); i++)
        res = res * 10 + s[i] - '0';
    return res;
}

void make(int x){
    string s = to_str(x);
    a[x].pb(x);
    for (int i = 0; i < len(s); i++){
        s = s.substr(1, len(s)-1) + s[0];
        if (s[0] != '0')
            a[x].pb(to_int(s));
    }
    sort(all(a[x]));
    vector<int> t;
    for (int i = 0; i < len(a[x]); i++)
        if (i == 0 || a[x][i] != a[x][i-1])
            t.pb(a[x][i]);
    a[x] = t;
}

void run(int t, int aa, int bb){
    int64 res = 0;
    for (int i = aa; i <= bb; i++){
        int l = lower_bound(all(a[i]), aa) - a[i].begin(), r = lower_bound(all(a[i]), bb+1) - a[i].begin();
        res += max(0, r-l-1);
    }
    cout << "Case #" << t << ": " << res / 2 << endl; 
}

int main(){
    a.resize(maxn);
    for (int i = 1; i < maxn; i++)
        make(i);
    debug("Finally!");
    int t; cin >> t;
    for (int i = 0; i < t; i++){
        int a, b; cin >> a >> b;
        run(i+1, a, b);
    }
    return 0;
}
