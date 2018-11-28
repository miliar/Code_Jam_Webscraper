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

#define For(i,a,b) for (int i=a; i <= b; ++i)
#define Ford(i,a,b) for (int i = a; i >= b; --i)
#define Rep(i,n) For(i, 0, n -1)
#define Repd(i,n) For(i, n - 1, 0)
#define mp(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))
#define all(v) v.begin(), v.end()
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
const int INF=(1<<30);

using namespace std;

char buff[256];

bool useDelim = false;


struct Pt {
    long x;
    long y;
    Pt(long _x, long _y) : x(_x), y(_y){};
    Pt() {
        Pt(0, 0);
    }
};
struct sc  {    
    bool operator()(Pt&x, Pt& y) {
        return x.x < y.x;
    }
};


ostream& operator <<(ostream& o, Pt& pt) {
    return o << "(" << pt.x << "," << pt.y << ")";
}

template<class T> ostream& operator <<(ostream& o, vector<T>& t) {
    for (vector<T>::iterator it = t.begin(); it != t.end(); ++it) {
        o << *it << ' ';
    }
    o << endl;
    return o;
}


int main(int argc, char* argv[]) {
    string name = "a-small-attempt2.in";//argv[1];
    string outName = name + ".out";
    ifstream in(name.c_str());
    ofstream out(outName.c_str());

    
    int N;
    in >> N;
    Rep(i, N) {
        out << "Case #" << i + 1 << ": ";

        long long n, A, B, C, D, M, x0, y0;

        in >> n >> A >> B >> C >> D >> x0 >> y0 >> M;


        vector<Pt> vp;
        vp.reserve(n);
        long x = x0; long y = y0;
        vp.push_back(Pt(x,y));
        for (int j = 0; j < n - 1; ++j) {
            
            x = (A * x + B) % M;
            y = (C * y + D) % M;
            vp.push_back(Pt(x,y));
            
        }

        // sort(all(vp), sc());

       //  cout << vp;
        long s = 0;
        for (int a = 0; a < n; ++a)
        for (int b = a + 1; b < n; ++b)
        for (int c = b + 1; c < n; ++c) {
            long l1 = (vp[a].x + vp[b].x + vp[c].x);
            long l2 = (vp[a].y + vp[b].y + vp[c].y);
            if ( l1 % 3==0 && l2 % 3 ==0) {
                ++s;
            }
            
            /*
            long xc = l1 /3;
            long yc = l2 / 3;
            for (int d = a; d <= c; ++d) {
                if (vp[d].x == xc && vp[d].y == yc) {
                    ++s;
                }
            }
            */
        }
        out << s << endl;            
        //cout << vp ;
    }
}

