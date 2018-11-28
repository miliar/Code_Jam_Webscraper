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

struct Pnt {
	int a,b,c;
};

typedef vector<Pnt> VP;

//------------------------------------------

string s;
int a[30];
int n;
int u[10];
int mn;
void rec(int id) {
	/*For(i, 1, 10) {
		if (u[i] && a[id]<i) {
			a[id] = i;
			return;
		}
	}
	if (id == n) {
		return;
	}

	
	for(int i = id; i >= 0;--i) {
		a[i] = mn;
	}
	rec(id + 1);*/
	bool b = false;
	int i = 0;
	n = n +1;
	for(; i < n && !b; ++i) {
		fj(i) {
			if (a[j] > a[i]) {
				swap(a[j],a[i]);
				b = true;
				break;
			}
		}
	}

	if (i != n) {
		--n;
	}
	//if (!b) {
	//	for(int i = 0; i < n; ++i) {
	//		a[i + 1]= a[i];
	//	}
	//	a[0] = 0;
	//	++n;
	//	//+0
	//	return ;
	//}
	for(i=i-2; i>0; --i) {
		for(int j = i - 1; j >= 0; --j) {
			if(a[i]>a[j]) {
				swap(a[i],a[j]);
			}
		}
	}
	
	return;
}

int solve() {
	//int n;
	
	//cin >> n;
	cin >> s;
	
	
	Fill(a, 0);
	Fill(u,0);
	n = s.size();
	mn = 20;
	fi(s.size()) {
		int k = s.at(i)-48;
		u[k] = 1;
		if (k < mn && k != 0) {
			mn = k;
		}
		a[n - i-1] = k;
	}

	rec(0);

	fi(n) {
		cout << (char)('0' + a[n-i-1]);
	}
	
	return 1;
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
		int j = solve();
		cout << endl;
		

		long t = GetTickCount() - l;
		cerr << " << " << i << " " << t/1000. << "s, est: " << ( t / double(i + 1)) * n / 1000.  << "s" << endl;
	}
}
