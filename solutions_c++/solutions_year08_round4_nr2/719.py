#include <stdafx.h>
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
#include <windows.h>

using namespace std;

#define For(i,a,b) for (int i=a; i < b; ++i)
#define Ford(i,a,b) for (int i = a; i > b; --i)
#define Rep(i,n) For(i, 0, n)
#define Repd(i,n) For(i, n, 0)
#define mp(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))
#define all(v) v.begin(), v.end()
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define VI vector<int>

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

void solve() {
    long long n, m, a;

    cin >> n >> m >> a;

    for (int x2 = (int)(a / m); x2 <= n; ++x2) {
        for(int y2 = 0; y2 <= m; ++y2) {
            
            int x3max = y2 == 0 ? n : (x2 * m - a) / y2;
            //if (x2 * m >
            for (int x3 = 0; x3 <= x3max; ++x3) {
                if (x2 != 0) /*{
                    if (x3 * y2 == a) {
                        cout << "0 0 " << x2 << " " << y2 << " " << x3 << " " << 0 << endl;
                        return;
                    }
                } else */{
                    long long y3 = (a + ((long long)x3) * y2);
                    if (y3 % x2 == 0 && y3 / x2 <= m) {
                        cout << "0 0 " << x2 << " " << y2 << " " << x3 << " " << y3 / x2 << endl;
                        return;
                    }
/*
                     y3 = (-a + ((long long)x3) * y2);
                    if (y3 % x2 == 0 && y3 / x2 >= 0) {
                        cout << "0 0 " << x2 << " " << y2 << " " << x3 << " " << y3 / x2 << endl;

                        if ((x3 * y2 - x2 * y3 != -a) && (x3 * y2 - y3 != a) ) {
                            cout <<"!!!!!!!!" << endl;
                        }
                        return;
                    }
                    */
                }

            }
        }
    }

        cout << "IMPOSSIBLE" <<endl;

/*
    for (int x = 0; x < n; ++x) {
        for(int y = 0; y <= x; ++y) {
            
            for (int x3 = 0; x3 < n; ++x3) {
                long long y2 = (a + x3 * (long long)y);
                if (x == 0) {

                }
                if (y2 % x == 0) {
                    if (y2 / x < m) {
                        cout << "0 0 " << x << " " << y << " " << x3 << " " << y2 / x << endl;
                    }

                }

            }
        }
    }
    */

}

int main(int argc, char* argv[]) {
    string name = "b-small-attempt5.in";
    //string name = "testb.in";
    if (argc > 1) name = argv[1];
    string out = name + ".out";
    freopen(name.c_str(), "r", stdin);
        freopen(out.c_str(), "w", stdout);

    long l = GetTickCount();
    int n;
    cin >> n;
    Rep(i, n) {
        cout << "Case #" << i + 1 << ": ";
        solve();

        long t = GetTickCount() - l;
        cerr << " << " << i << " " << t/1000. << "s, est: " << ( t / double(i + 1)) * n / 1000.  << "s" << endl;
    }
}

