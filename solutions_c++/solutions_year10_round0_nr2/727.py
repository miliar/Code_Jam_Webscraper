#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <set>
#include <list>
#include <map>
#include <complex>
#include <numeric>
#include <algorithm> 
#include <functional>
#include <stdlib.h>
#include <stdio.h>


using namespace std;

#ifdef COUNTER
#include <windows.h>
struct Counter {
	long l;
	Counter() {l = GetTickCount();}
	void tick(int i, int n) {
		long t = GetTickCount() - l;
		cerr << " << " << i << " " << t/1000. << "s, est: " << ( t / double(i + 1)) * n / 1000.  << "s" << endl;
	}
};
#else 
struct Counter {
	Counter() {}
	void tick(int i, int n) {}
};
#endif



#define For(i,a,b) for (int i=a; i < b; ++i)
#define fi(n) For(i, 0, n)
#define fj(n) For(j, 0, n)
#define Ford(i,a,b) for (int i = a; i > b; --i)
#define Rep(i,n) For(i, 0, n)
#define Repd(i,n) Ford(i, n, 0)
#define mp(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))
#define all(v) v.begin(), v.end()
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define VI vector<int>

template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}

//template<class T> inline T gcd(T a,T b)//NOTES:gcd(
//{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,fmod(a,b));}


#undef min
#undef max
const int INF=(1<<30);
char buff[2560];

//debug
template<class T> ostream& operator <<(ostream& o, vector<T>& t) { for (vector<T>::iterator it = t.begin(); it != t.end(); ++it) o << *it << ' '; o << endl; return o;}
template<class T> ostream& operator <<(ostream& o, list<T>& t) { for (list<T>::iterator it = t.begin(); it != t.end(); ++it) o << *it << ' '; o << endl; return o;}
template<class T> ostream& operator <<(ostream& o, set<T>& t) { for (set<T>::iterator it = t.begin(); it != t.end(); ++it) o << *it << ' '; o << endl; return o;}
template<class T, class U> ostream& operator <<(ostream& o, map<T, U>& t) {for(map<T, U>::iterator it = t.begin(); it !=t.end(); ++it) o << it->first << "(" << it->second << ") "; o << endl;return o;}

string readLine() {
	do cin.getline(buff, sizeof(buff)); 
	while(buff[0] == 0);
	return buff;
}

struct StringToNum {
	map<string, int> m;
	int& get(string& str) {
		map<string, int>::iterator it = m.find(str);
		if (m.end() == it) {
			m[str] = m.size();
		} 
		return m[str];
	}

	int size() {
		return m.size();
	}
};

struct rect {
	int l,r,b,t;
	rect(int l, int r, int b, int t) : l(l), r(r), b(b), t(t) {
	}

	bool in(int x, int y) {
		return x >= l && x <= r && y >= b && y <=t;
	}
};

template<class T>
bool inRect(const T& x, const T& y, const T& w, const T& h) {
	return (x>= 0 && y >= 0 && x < w && y < h);
}

template<class T>
bool inRect(complex<T>& v, complex<T>& size) {
	return (v.real()>= 0 && v.imag() >= 0 && v.real() < size.real() && v.imag() < size.imag());
}

struct Pnt {
	int a,b,c;
};

typedef vector<Pnt> VP;

//------------------------------------------
typedef unsigned long long type;
type  solve() {
    int n;
    cin >> n;
    
    type s = 0ULL;
    type l = 0ULL;
    type g = 0ULL;
    type ll;
    fi(n) {
        string st;
       // cin >> st;
      //  ll = atoi64(st.c_str());
        cin >> ll;
        if (!i) {
            s = ll;
            continue;
        } else {
            ll = (s > ll) ? (s - ll) : (ll - s);
            l = (i==1) ? ll : l;
        }

        type g1 = gcd(l, ll);
        if (g == 0) {
            g = g1;
        } else {
            if (g1 > g) {
                swap(g, g1);
            }

            //if (fmod(g,g1) == 0)
              //  g = g1;

            if (!(g%g1))
                g = g1;
        }
            
    }
    //return (floor(s / g) + (fmod(s , g) == 0?0:1))*g - s;
    return (s/g + (s%g == 0 ? 0 : 1))*g - s;

}

//------------------------------------------

int main(int argc, char* argv[]) {
	string name = "test.in";
	name = "b-small-attempt0.in";
	//name = "b-small-attempt1.in";
	//name = "b-large.in";

	if (argc > 1) name = argv[1];
	string out = name + ".out";
	freopen(name.c_str(), "r", stdin);
	freopen(out.c_str(), "w", stdout);

	Counter counter;
	int n;
	cin >> n;
	Rep(i, n) {
		cerr << "Case #" << i + 1 << ": ";
		cout << "Case #" << i + 1 << ": ";
		type  j = solve();
		cout << j << endl;
		cerr << j;

		counter.tick(i,n);
	}
}
