#include<iostream>
#include<string>
#include<cmath>
#include<map>
using namespace std;
#define eps 1e-15



struct Point {
    double x, y, z;

    void in() {
        scanf("%lf %lf %lf", &x, &y, &z);
    }

    void out(){
        printf("%.3lf %.3lf %.3lf\n",x, y, z);
    }


    Point operator+(const Point & p)const {
        Point ans;
        ans.x = x + p.x;
        ans.y = y + p.y;
        ans.z = z + p.z;
        return ans;
    }

    Point operator-(const Point & p)const {
        Point ans;
        ans.x = x - p.x;
        ans.y = y - p.y;
        ans.z = z - p.z;
        return ans;
    }

    Point operator/(double N) const {
        Point ans;
        ans.x = x / N;
        ans.y = y / N;
        ans.z = z / N;
        return ans;
    }

    Point operator*(double N) const {
        Point ans;
        ans.x = x * N;
        ans.y = y * N;
        ans.z = z * N;
        return ans;
    }
};

Point p, v, zero;

int dcmp(double x){return x < -eps ? -1 : x > eps; }

double dis(Point a, Point b){
    return sqrt((a.x - b.x)*(a.x - b.x)+(a.y - b.y)*(a.y - b.y) + (a.z - b.z)*(a.z - b.z) );
}

double find(double t){
    Point now  = p + v*t;
    return dis(now, zero);
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    int cas, T, i, n;
    cin >> T;
    for (cas = 1; cas <= T; cas++) {
        zero.x = zero.y = zero.z = 0;
        printf("Case #%d: ", cas);
        scanf("%d", &n);
        Point tp, tv;
        p.x = p.y = p.z = v.x = v.y = v.z = 0;

        for (i = 0; i < n; i++) {
            tp.in();
            tv.in();
            p = p + tp;
            v = v + tv;
        }
        p = p / n;
        v = v / n;

        if(dcmp(v.x)==0 && dcmp(v.y)==0 && dcmp(v.z)==0 )
        {
            printf("%.10lf %.10lf\n",find(0), 0.0);
            continue;
        }
        
        double l = 0, r = 1e100, mid1, mid2, t1, t2;
        while (r - l > eps) {
            mid1 = l + 1.0 / 3 * (r - l);
            mid2 = l + 2.0 / 3 * (r - l);
            t1 = find(mid1);
            t2 = find(mid2);
            if (dcmp(t1 - t2) > 0) {
                l = mid1;
            } else
                if (dcmp(t1 - t2) < 0) {
                r = mid2;
            } else {
                l = mid1;
                r = mid2;
            }
        }
        printf("%.10lf %.10lf\n",find(r), r);
    }

}

/*
10 
3
2553 1147 2313 793 -1570 -1367
-738 -2237 -2093 -355 -2319 -458
1785 -2510 1580 -438 3889 1825
 */