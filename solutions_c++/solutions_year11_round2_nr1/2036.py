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
int n;
int a[100][100];
double wp[100][3];
double owp[100][100];
double owp2[100];

void calcWP() {
    fi(n) {
        double d = 0;
        int k = 0;
        fj(n) {
            if (a[i][j] != -1) {
                k++;
                d += a[i][j];
            }
        }

         wp[i][2]  = (k==0) ? 0 : d / k;
        wp[i][0]  = d;//(k==0) ? 0 : d / k;
        wp[i][1] = k;
    }
}

void calcOWP() {
    fi(n) fj(n){
        double d = wp[i][0];
        int k = wp[i][1];

        if (a[i][j]!=-1) {
            double d1 = a[i][j];
            d -= d1;
            k--;
            owp[i][j]=k==0?0:d/k;
        }

    }

    fi(n) {
        double d =0;
        int k = 0;
        fj(n) {
            if (a[i][j] != -1) {
                k+= 1;
                d += owp[j][i];
            }
        }
        owp2[i]=k==0?0:d/k;
    }

}

//double getOWP(int k ) {
//    double d=0;
//    fi(n) {
//        d+=owp[i][j];
//    }
//    return 0;
//}

double calcOOWP(int k) {
    double d = 0;
    int s = 0;
    fi(n) {
        if(a[i][k] != -1) {
            d+=owp2[i];
            ++s;
        }
    }
    return s == 0? 0: d/s;
}

double rti(int k) {
    double w1=wp[k][2];
    double w2 = owp2[k];

    //int s = 0;
    //fi(n) {
    //    if(a[i][k] != -1) {
    //        w2+=owp2[i];
    //        ++s;
    //    }
    //}
    //w2 = s == 0 ? 0 : w2/s;
    double w3 = calcOOWP(k);

    return 0.25 * w1 + 0.50 * w2 + 0.25 * w3;

}

int solve() {
    cin >> n;
  
    fi(n)fj(n) {
        char c;
        cin >> c;
        a[i][j] = c == '.' ? -1 : c-'0';
    }

    calcWP();
    calcOWP();

    fi(n) {
        double r = rti(i);
        cerr << r<<endl;
        cout<<setprecision(10) << r<<endl;

    }

	return 1;
}

//------------------------------------------

int main(int argc, char* argv[]) {
	string name = "test.in";
	name = "a-small-attempt0.in";
	//name = "a-small-attempt1.in";
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
		//int j = solve();
      
		cout << endl;
        cerr<<endl;
          solve();
		//cerr << j;

		counter.tick(i,n);
	}
}
