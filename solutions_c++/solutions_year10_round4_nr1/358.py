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
int k;
int getS(int a) {
    return a < k ? 2*a+1 : 4*k - 3 - 2*a;
}

int a[120][120];
int get(int x, int y) {
    if (x < 0 || x > 2*k-1 || y < 0 || y > 2*k-1){
        return -1;
    }
    return a[y][x];

}

bool c(int i1, int i2) {
    return (i1 == -1 || i2 == -1 || i1 == i2);
}
bool check(int x, int y) {
    for(int i = 0; i <= k; ++i) {
        for(int x0 = 0; x0 <=i;++x0) {
            for(int y0 = 0; y0 <=i;++y0) {
                int x1 = x - x0; int y1 = y-y0;
                int x2 = x + x0; int y2 = y-y0;
                int x3 = x + x0; int y3 = y+y0;
                int x4 = x - x0; int y4 = y+y0;
                int i1 = get(x1,y1);
                int i2 = get(x2,y2);
                int i3 = get(x3,y3);
                int i4 = get(x4,y4);
                
                if (!c(i1,i2) || !c(i1,i3) || !c(i1,i4) || !c(i2,i4)
                    ||!c(i2,i3) || !c(i3,i4)) {
                    return false;
                }
            }
        }
    }
    return true;
}

//------------------------------------------


int v[100];
int h[100];
int solve() {
    
    memset(a, -1, sizeof(a));
    cin >> k;
    fi(2*k-1) {
        string s = readLine();
        fj(s.size()) {
            if (s.at(j) != ' ')
                a[i][j] = s.at(j)-'0';
        }
    //    cerr << s <<endl;
    }
    
            int xc = k-1;
        int yc = k-1;
    for(int i = 0; i <= k; ++i) {

        for(int x = 0; x <=i;++x) {
            for(int y = 0; y <=i;++y) {
                if (check(xc +x,yc+y)
                    || check(xc -x,yc+y)
                    || check(xc -x,yc-y)
                    || check(xc +x,yc-y)) {
                        //cerr << i;
                        int z = x+y+k;
                        int delta = z * z - k*k;
                        return delta;
                    }
            }
        }
    }
    

	return 1;
}

//------------------------------------------

int main(int argc, char* argv[]) {
	string name = "test.in";
	name = "a-small-attempt0.in";
	name = "a-small-attempt1.in";
	name = "a-large.in";

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
		int j = solve();
		cout << j << endl;
		cerr << j;

		counter.tick(i,n);
	}
}
