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
#include <windows.h>

#include <numeric>
#include <algorithm> 
#include <functional>

using namespace std;

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

struct Eg {
	int a, b;
	Eg() : a(-1), b(-1) {}
};
struct Pnt {
	vector<int> eg;
	int h;
	char b;
	bool m;
	Pnt() {
		m = false;
	}
};

typedef vector<Pnt> VP;

int h, w;

Pnt p[10000];

//------------------------------------------
int mx = 20000;
int ng[4][2] = {{0, -1}, {-1, 0}, {1,0}, {0, 1}};


Pnt& pnt(int y, int x) {
	return p[y*w + x];
}

int id(int y, int x) {
	return y * w + x;
}

VI bf;
VI bftmp;
bool rec(int id, int c) {

	if (p[id].m) {
		return false;
	}
	
	p[id].m = true;
	p[id].b = c;
	bf.clear();
	bftmp.clear();
	bf.push_back(id);
	
	while(!bf.empty()) {
		int l = bf.size();
		for (int j = 0; j < l;++j) {
			Pnt &pp = p[bf[j]];
			for(int i = 0; i < pp.eg.size(); ++i) {
				int& id = pp.eg[i];
				Pnt& n = p[id];
				if (!n.m){
					bftmp.push_back(id);
					n.m = true;
					n.b = c;
				}
			}
		}
		bf.swap(bftmp);
		bftmp.clear();
	}
	return true;
}

void solve() {
	cin >> h >> w;

	fi(h)
		fj(w) {
			pnt(i,j) = Pnt();
			cin >> pnt(i, j).h;
			
		}

	fi(h)
		fj(w) 
	{
		int x1 = -1;
		int y1 = -1;
		int m = 100000;
		for (int k = 0; k < 4;++k) {
			int x  = j + ng[k][0];
			int y  = i + ng[k][1];
			if (x >= 0 && x < w && y >= 0 && y < h) {
				if (m > pnt(y, x).h) {
					m = pnt(y, x).h;
					x1 = x;
					y1 = y;
				}
			}
		}

		if (m < pnt(i,j).h) {
			pnt(i, j).eg.push_back(id(y1, x1));
			pnt(y1, x1).eg.push_back(id(i, j));
		}
	}
	
	int c = 0;
	fi(h)
		fj(w) 
	{
		if (rec(id(i,j), c)) 
			c++;
	}
	cout << endl;
	fi(h) {
		fj(w) {
			cout << (char)('a' + pnt(i, j).b) << ' ';
		}
		cout<<endl;
	}

}

//------------------------------------------

int main(int argc, char* argv[]) {
	string name = "test.in";
	name = "b-small-attempt0.in";
	name = "b-large.in";
	if (argc > 1) name = argv[1];
	string out = name + ".out";
	freopen(name.c_str(), "r", stdin);
	freopen(out.c_str(), "w", stdout);

	long l = GetTickCount();
	int n;
	cin >> n;
	Rep(i, n) {
		cerr << "Case #" << i + 1 << ": ";
		cout << "Case #" << i + 1 << ": ";
		solve();
		//cout << j << endl;
		//cerr << j;

		long t = GetTickCount() - l;
		cerr << " << " << i << " " << t/1000. << "s, est: " << ( t / double(i + 1)) * n / 1000.  << "s" << endl;
	}
}
