#include <iostream> 
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

struct Point {
    double x, y;
    Point(double _x = 0.0, double _y = 0.0) : x(_x), y(_y) {}
};

Point upper[110], lower[110];
double answer[110];
int upper_n, lower_n, guests;
double width;

void init() {
    cin >> width >> lower_n >> upper_n >> guests;
    for (int i = 1; i <= lower_n; i ++) cin >> lower[i].x >> lower[i].y;
    for (int i = 1; i <= upper_n; i ++) cin >> upper[i].x >> upper[i].y;
}

double area(Point p1, Point p2) {
    return 0.5 * (p2.x - p1.x) * ((p1.y + 1000.0) + (p2.y + 1000.0));
}

Point get_p(Point a, Point b, double x) {
    return Point(x, (b.y-a.y)/(b.x-a.x)*(x-a.x) + a.y);
}

double cal2(Point p[], int n, double le, double ri) {
    double ans = 0.0;
    for (int i = 1; i < n; i ++) {
        double l = max(le, p[i].x);
        double r = min(ri, p[i+1].x);
        if (l >= r)
            continue;
        ans += area(get_p(p[i], p[i+1], l), get_p(p[i], p[i+1], r));
    }
    //printf("ans = %.9lf\n", ans);
    return ans;
}

double cal(double le, double ri) {
    double ans = cal2(upper, upper_n, le, ri) - cal2(lower, lower_n, le, ri);
    //printf("le=%.9lf ri=%.9lf ans=%.9lf\n", le, ri, ans);
    return ans;
}

void solve(int case_index) {
    double each_size = cal(0, width) / (double)guests;
    answer[1] = 0.0;
    for (int i = 2; i <= guests; i ++) {
        double le = answer[i-1], ri = width, mid;
        for (int times = 0; times < 100; times ++)
            if (cal(answer[i-1], mid = (le+ri)*0.5) < each_size)
                le = mid;
            else
                ri = mid;
        answer[i] = (le+ri) * 0.5;
    }
    printf("Case #%d:\n", case_index);
    for (int i = 2; i <= guests; i ++)
        printf("%.9lf\n", answer[i]);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("a-large.txt", "w", stdout);
    int case_count;
    cin >> case_count;
    for (int i = 1; i <= case_count; i ++) {
        cerr<<i<<endl;
        init();
        solve(i);
    }
    return 0;
}
