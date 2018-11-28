/*
 * Author: NomadThanatos
 * Created Time:  2011/5/22 1:10:33
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())

const int MAXINT = -1u>>1;
const int MAXN = 200 + 20;
const double EPS = 1e-13;

template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int sgn(const double &x) {return (int)((x > EPS) - (x < -EPS));}

struct Node {
    int P,V;
    void input() {
        scanf("%d%d",&P,&V);
    }
    bool operator < (const Node &A) const {
        return P < A.P;
    }
}hd[MAXN];

int C,D;

bool check(const double &t) {
    double backpos = -1e10;
    for(int i = 0 ; i < C ; i++) {
        double l = max(backpos + D,hd[i].P - t) ;
        double r = min(l + (hd[i].V - 1) * D,hd[i].P + t);
        //printf("%d %lf %lf\n",i,l,r);
        if (sgn(r - l - (hd[i].V - 1) * D) < 0) {
            //printf("break %lf %lf\n",l - r,(hd[i].V - 1) * D);
            return false;
        }
        backpos = r;
    }
    return true;
}

int main() {
    freopen("B.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        scanf("%d%d",&C,&D);
        for(int i = 0 ; i < C ; i++) {
            hd[i].input();
        }
        sort(hd,hd + C);
        double l = 0.0,r = 1e10,mid;
        for(int cnt = 0 ; cnt < 500 ; cnt++) {
            mid = (l + r) / 2;
            if (check(mid)) {
                r = mid;
            }
            else l = mid;
            //printf("-------\n");
        }
        printf("Case #%d: %0.12lf\n",t + 1,l);
    }
    return 0;
}

