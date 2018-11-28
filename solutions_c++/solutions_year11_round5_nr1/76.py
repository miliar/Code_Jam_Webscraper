//#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <queue>
#include <stack>
#define FOR(i,a,b) for(int i = (a); i <= (b); i++) 
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >= 0; i--)
#define REP(i,a) for(int i = 0; i < (a); i++)
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define For(i,a,b) for(int i = (a); i <= (b); i++)

#define sqr(x) ((x)*(x))
#define dout debug && cout 
#define ll long long
#define sz size()
#define ull unsigned long long
#define pb push_back
#define oo 1000000009
using namespace std;

#define maxn 1000
struct point {
    double x,y;
    point() {x=y=0;}
    point(double x,double y):x(x),y(y) {}
};

point p[maxn];
double totalArea = 0;

double W;
int m,n,G;
vector<point> a,b;
double sum;
double LEFT, RIGHT;

void get(point A,point B, double &a1, double &b1, double &c1) {
    a1 = A.y - B.y;
    b1 = B.x - A.x;
    c1 = - a1 * A.x - b1 *A.y;
}
point getGiao(point A, point B, double D) {
    double a1,b1,c1,a2,b2,c2;
    get(A,B,a1,b1,c1);
    a2 = 1, b2 = 0, c2 = -D;
    double d = a1 * b2 - a2 * b1;
    double dx = b1 * c2 - b2 * c1;
    double dy = c1 * a2 - c2 * a1;
    return point(dx/d,dy/d);
}
double getLine(vector<point> &a, vector<point> &b, double Line) {
    point X,Y;
    FR(i,a.size()-1) 
    if ((a[i].x <= Line && a[i+1].x > Line) || (a[i].x < Line && a[i+1].x >= Line)) {
        X = getGiao(a[i],a[i+1],Line);
        break;
    }
    
    FR(i,b.size()-1)
    if ((b[i].x <= Line && b[i+1].x > Line) || (b[i].x < Line && b[i+1].x >= Line)) {
        Y = getGiao(b[i],b[i+1],Line);
        break;
    }
//    cout << "POINT " << X.x << " " << X.y << " " << Y.x << " " << Y.y << endl;
    double res =  sqrt(sqr (X.x - Y.x) + sqr(X.y-Y.y));
//    cout << res << endl;
    return res;
}
bool LEQ(double x,double y) {
    return abs(x-y) < 1e-8 || x < y;
}
bool GE(double x, double y) {
    return (abs(x-y) != 1e-8 && x > y);
}
void get() {
    
    vector<point> tmp(0);
    FR(i,a.size()-1) {
    if (LEQ(a[i].x,LEFT) && GE(a[i+1].x,LEFT)) {
            tmp.push_back( getGiao(a[i],a[i+1],LEFT));
            FOR(j,i+1,a.size()-1) tmp.push_back( a[j]);
            a = tmp;
            break;
        }
    }
    
    tmp.clear();
    FR(i,b.size()-1) {
        if (LEQ(b[i].x,LEFT) && GE(b[i+1].x,LEFT)) {

            //tinh giao diem
            tmp.push_back( getGiao(b[i],b[i+1],LEFT) );
//            cout << "S" << endl;
//            cout << tmp.size() << endl;
//            cout << i+1 << " " << b.size() - 1 << endl;
            FOR(j,i+1,b.size()-1) tmp.push_back(b[j]);
//            cout << tmp.size() << endl;
            b = tmp;
            break;
        }
    }
    
//    cout << a.size() << " " << b.size() << endl;
//    cout << "CHECK" << endl;
//    cout << a[0].x << endl;
//    cout << b[0].x << endl;
    vector<double> truc(0);
    truc.clear();
    FR(i,a.size()) truc.push_back(a[i].x);
    FR(i,b.size()) truc.push_back(b[i].x);
    sort(truc.begin(),truc.end());
    double total = sum;
//    cout << total << endl;
    FR(i,truc.size()-1) {
        double d1 = getLine(a,b,truc[i]);
        double d2 = getLine(a,b,truc[i+1]);
        double area = (truc[i+1] - truc[i]) * (d1 + d2) / 2;
//        cout << d1 << " " << d2 <<" " << truc[i] << " " << truc[i+1] <<  endl;
        if (total >= area) total -= area;
        else {
            double first = truc[i], last = truc[i+1], mid;
            do {
                mid = (first + last) / 2;
                double d3 = getLine(a,b,mid);
                area = (mid - truc[i]) * (d1 + d3) / 2;
                if (area < total) first = mid;
                else last = mid;
            } while (last - first > 1e-8);
            LEFT = (last + first) / 2;
            printf("%.8lf\n",LEFT);
            return;
        }
    }
//    cout << total << endl;
}
void solve() {
    
    p[m+n+1] = p[1];
    sum = 0;
    FOR(i,1,m+n) sum += (p[i].x - p[i+1].x) * (p[i].y + p[i+1].y);
    sum = abs(sum) / 2;
//    cout << "Area " << sum << endl;
    sum /= G;
//    cout << sum <<e.ndl;
    a.clear();
    b.clear();
    FOR(i,1,m) a.push_back(p[i]);
    DOWN(i,m+n,m+1) b.push_back(p[i]);
    
    
    LEFT = 0; RIGHT = W;
    FOR(i,1,G-1) get();
}
int main() {
    freopen("a.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": " << endl;
        cin >> W >> m >> n >> G;
        FOR(i,1,m) cin >> p[i].x >> p[i].y;
        
        DOWN(i,m+n,m+1) cin >> p[i].x >> p[i].y;
        solve();
    }
    return 0;
}

