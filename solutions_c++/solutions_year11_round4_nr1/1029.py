// BEGIN CUT HERE

// END CUT HERE
// Mini Template
#include <cstdio>
#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define TR(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define REP(i, n) for(int i = 0; i<(n); i++)
#define REPSE(i, s, e) for(int i = s; i <(e); i++)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define FILL(x, c) memset(x, c, sizeof(x))
#define ALL(x) x.begin(), x.end()
#define FIN(x, c) (x.find(c)!=x.end())
#define IN(x, c) (find(x.begin(), x.end(), c)!=x.end())
// Template Ends
//hihihihihihi

int x, s, r, t, n;
struct node {
    int b, e, w;
    node(int b, int e, int w) {
        this->b = b;
        this->e = e;
        this->w = w;
    }

    bool operator<(const node &other) const {
        double twalk1 = (double)(e-b)/(s+w);
        double trun1 = (double)(e-b)/(r+w);

        double twalk2 =(double)(other.e-other.b)/(s+other.w);
        double trun = (double)(other.e-other.b)/(r+other.w);
        return w < other.w;
        //return (trun1-twalk1)<(trun-twalk2);
    }
};

vector<node> vn;

int segment[1111111];
const double EPS = 1e-9;
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int ts;
    scanf("%d", &ts);

    for(int testcase = 1; testcase <= ts; testcase++) {

        scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
        //printf("x = %d s = %d r = %d t = %d n = %d\n", x, s, r, t, n);
        vn.clear();
        FILL(segment, 0);
        REP(i, n) {
            int b, e, w;
            scanf("%d%d%d", &b, &e, &w);
            vn.PB(node(b , e, w));
            segment[b]++;
            segment[e]--;
        }

        int ddist = 0;
        int cum = segment[0];
        for(int i = 1; i <= x; i++) {
            if(cum==0) ddist++;
            cum += segment[i];
        }
        //printf("ddist = %d\n", ddist);
        //
        vn.PB(node(0, ddist, 0));
        sort(ALL(vn));


        double total = 0;
        double left = t;
        double _time;
        TR(vn, it) {
            int l = it->e-it->b;
            int w = it->w;
            //printf("Checking %d %d %d\n", it->b, it->e, it->w);
            if(left>0+EPS) {
                //printf("Left > 0\n");
                _time = (double)l/(r+w);
                //printf("_time = %lf\n", _time);
                if(_time < left+EPS) {
                    //printf("_time < left\n");
                    left -= _time;
                    total += _time;
                    //printf("left = %lf total = %lf\n", left, total);
                }
                else {
                    //printf("_time !< left\n");
                    double dist1, dist2;
                    dist1 = left*(r+w);
                    dist2 = l - dist1;
                    total += left + (double)dist2/(s+w);
                    //printf("dist1 = %lf dist2 = %lf left = %lf total = %lf\n\n", dist1, dist2, left, total);
                    left = 0;
                }
            }
            else {
                //printf("Left = 0\n");
                _time = (double)l/(s+w);
                total += _time;
                //printf("time = %lf total = %lf\n", _time, total);
            }
            //printf("\n\n");
        }

        printf("Case #%d: %0.12f\n", testcase, total);
    }
}
