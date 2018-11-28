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

typedef long double ll;
struct Node {
	string name;
	ll p;
	Node* c1;
	Node* c2;
	Node* parent;
	Node() {
		c1 = c2 = NULL;
		parent = NULL;
	}
};

string s;
void rec(int start, int end, Node* node) {
	int id1 = s.find('(', start);
	int id2 = s.rfind(')', end);

	int id3 = s.find('(',  id1 + 1);
	string z = s.substr(id1+1, id2 - id1-1);
	if (id3 == -1 || id3 > id2) {
		//leaf;
		istringstream iss(z);
		iss >> node->p;
		return;
	}

	
	istringstream iss(z);
	iss >> node->p >> node->name;
	
	list<int> v;
	int q= 0;
	for(int i = id1+1;i != id2;++i) {
		if (s[i] =='(') {
			v.push_back(i);
		}
		if (s[i] ==')') {
			int k = v.back();
			v.pop_back();
			if (v.empty()) {
				string z = s.substr(k, i-k);
				Node* n = new Node();
				n->parent = node;
				if (0 == q++) {
					node->c1 = n;
				} else {
					node->c2 = n;
				}
				rec(k, i, n);
				
			}
		}
	}
}

vector<string> f;
long double rec2(Node* n) {
	long double p = 1;
	p*= n->p;
	
	if (n->c1 == NULL) {
		return p;
	}
	Node* n1 = n->c1;
	Node* n2 = n->c2;

	if (f.end() != std::find(f.begin(), f.end(), n->name)) {
		p *= rec2(n1);
	} else {
		p*= rec2(n2);
	}
	return p;
}

int solve() {
	
	int n;
	cin >> n;
	
	Node* node = new Node();
	s = "";
	fi(n) {
		s += readLine();
	}

	Node* parent = new Node();
	rec(0, s.size(), parent);
	
	int k = 0;
	cin >> k;
	
	fi(k) {
		string name;
		cin >> name;
		int cn;
		cin >> cn;
		f.clear();
		fj(cn) {
			string q;
			cin >> q;
			f.push_back(q);
		}

		long double d = rec2(parent);
		printf("%.7f", d);
		cout << endl;
		//cerr << d << endl;
	}
	return 1;
}

//------------------------------------------

int main(int argc, char* argv[]) {
	string name = "test.in";
	name = "a-small-attempt0.in";
	//name = "a-large.in";

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
		cout <<endl;
		int j = solve();
		
		
		cerr << j;

		long t = GetTickCount() - l;
		cerr << " << " << i << " " << t/1000. << "s, est: " << ( t / double(i + 1)) * n / 1000.  << "s" << endl;
	}
}
