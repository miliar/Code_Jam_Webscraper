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

//------------------------------------------

int a[1001][1001];
int n;
int N = 1000;
bool isB(int i, int j) {
    return i <N && j <N &&(i >0 && j>0 && !a[i][j] && a[i-1][j]&&a[i][j-1]);
}

bool isD(int i, int j) {
     return i <N && j <N &&(a[i][j] && ((i > 0 && !a[i-1][j]) && (j >0 && !a[i][j-1])));
}
int solve() {
	
    cin >> n;
    
    memset(a, 0, sizeof(a));
    int s = 0;
    
    fi(n) {
        int x1, int y1, int x2, int y2;
        cin >> x1>>y1>>x2>>y2;
        for(int x = x1; x <= x2; ++x) {
            for(int y = y1; y <= y2; ++y) {
                s += (a[y][x] == 0);
                a[y][x] = 1;
            }
        }
    }
    
    set<pair<int,int> > d;
    set<pair<int, int> > b;
      //cerr << "--------"<<endl;
    fi(101) {
        fj(101) {
            if (isB(i,j)) {
                b.insert(make_pair(i,j));
            }
            if (isD(i,j)) {
                d.insert(make_pair(i,j));
            }
            //cerr << a[i][j];
        }
        //cerr << endl;
        
    }
    //cerr << b.size() << " " << d.size() << endl;
    
    int c = 0;
    while(s >0) {
        s += b.size() - d.size();
        ++c;
        for(set<pair<int,int> >::iterator it = b.begin(); it != b.end(); ++it) {
            a[it->first][it->second] = 1;
        }

        for(set<pair<int,int> >::iterator it = d.begin(); it != d.end(); ++it) {
            a[it->first][it->second] = 0;
        }

 //cerr << "----" << endl;
 //   fi(10) {
 //       fj(20) {
 //          
 //           cerr << a[i][j];
 //       }
 //       cerr << endl;
 //       
 //   }

        set<pair<int, int> > b2;
        set<pair<int, int> > d2;


        for(set<pair<int,int> >::iterator it = b.begin(); it != b.end(); ++it) {
            int i = it->first + 1;
            int j = it->second;
            if (isB(i,j)) {
                b2.insert(make_pair(i,j));
            }

            i = it->first;
            j = it->second+1;
            if (isB(i,j)) {
                b2.insert(make_pair(i,j));
            }
        }

        for(set<pair<int,int> >::iterator it = d.begin(); it != d.end(); ++it) {
            int i = it->first + 1;
            int j = it->second;
            if (isD(i,j)) {
                d2.insert(make_pair(i,j));
            }

            i = it->first;
            j = it->second+1;
            if (isD(i,j)) {
                d2.insert(make_pair(i,j));
            }
        }

        b.swap(b2);
        d.swap(d2);

    }
    if (s <0) {
        cerr << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
    }
    return c;
}

//------------------------------------------

int main(int argc, char* argv[]) {
	string name = "test.in";
	//name = "c-small-attempt0.in";
	//name = "c-small-attempt1.in";
    name = "c-small-attempt2.in";
    name = "c-small-attempt3.in";
	//name = "c-large.in";

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
