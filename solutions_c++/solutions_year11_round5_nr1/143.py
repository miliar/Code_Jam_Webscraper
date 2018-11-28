#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <utility>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>

using namespace std;

typedef long long LL;

const double eps = 1e-10;

struct Point {
    double x, y;
    Point(const double& x_ = 0, const double& y_ = 0): x(x_), y(y_) {}
};

const int maxn = 230;

int L, U;

Point u[maxn], l[maxn];
vector<double> ans;

double getuy(double x) {
    for (int i = 0; i < U-1; ++i) {
        if (u[i+1].x-u[i].x <= eps) {
            continue;
        }
        if (x >= u[i].x && x <= u[i+1].x) {
            return u[i].y + (u[i+1].y-u[i].y)*(x-u[i].x)/(u[i+1].x-u[i].x);
        }
    }
}

double getly(double x) {
    for (int i = 0; i < L-1; ++i) {
        if (l[i+1].x-l[i].x <= eps) {
            continue;
        }
        if (x >= l[i].x && x <= l[i+1].x) {
            return l[i].y + (l[i+1].y-l[i].y)*(x-l[i].x)/(l[i+1].x-l[i].x);
        }
    }
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int tests_num = 0;
    cin >> tests_num;
    
    for (int cur_test = 1; cur_test <= tests_num; ++cur_test) {
        
        double W, G;
        cin >> W >> L >> U >> G;
        double S = 0;
        for (int i = 0; i < L; ++i) {
            cin >> l[i].x >> l[i].y;
            if (i > 0) {
                S -= (l[i].x - l[i-1].x)*(l[i].y + l[i-1].y)/2.0;
            }
        }
        for (int i = 0; i < U; ++i) {
            cin >> u[i].x >> u[i].y;
            if (i > 0) {
                S += (u[i].x - u[i-1].x)*(u[i].y + u[i-1].y)/2.0;
            }
        }
        
        int cu = 0, cl = 0;
        S /= G;
        double curs = S;
        ans.clear();
        for (int i = 1; i <= G-1; ++i) {
            curs = S;
            while (curs > eps) {
                if (u[cu+1].x < l[cl+1].x && (u[cu+1].x-u[cu].x)*((u[cu+1].y+u[cu].y)/2 - (getly(u[cu+1].x)+l[cl].y)/2) < curs-eps) {
                    curs -= (u[cu+1].x-u[cu].x)*((u[cu+1].y+u[cu].y)/2 - (getly(u[cu+1].x)+l[cl].y)/2);
                    ++cu;
                    l[cl].y = getly(u[cu].x);
                    l[cl].x = u[cu].x;
                } else if (l[cl+1].x <= u[cu+1].x && (l[cl+1].x-l[cl].x)*((getuy(l[cl+1].x)+u[cu].y)/2 - (l[cl+1].y+l[cl].y)/2) < curs-eps) {
                    curs -= (l[cl+1].x-l[cl].x)*((getuy(l[cl+1].x)+u[cu].y)/2 - (l[cl+1].y+l[cl].y)/2);
                    ++cl;
                    u[cu].y = getuy(l[cl].x);
                    u[cu].x = l[cl].x;
                } else {
                    double x1 = u[cu].x, x2 = min(u[cu+1].x, l[cl+1].x), x;
                    while (x2-x1 > eps) {
                        x = (x1+x2)/2;
                        if (curs < (x-u[cu].x)*(2*(u[cu].y-l[cl].y) + (u[cu+1].y-u[cu].y)*(x-u[cu].x)/(u[cu+1].x-u[cu].x) - (l[cl+1].y-l[cl].y)*(x-l[cl].x)/(l[cl+1].x-l[cl].x))/2) {
                            x2 = x;
                        } else {
                            x1 = x;
                        }
                    }
                    x = (x1+x2)/2;
                    u[cu].y = u[cu].y + (u[cu+1].y-u[cu].y)*(x-u[cu].x)/(u[cu+1].x-u[cu].x);
                    l[cl].y = l[cl].y + (l[cl+1].y-l[cl].y)*(x-l[cl].x)/(l[cl+1].x-l[cl].x);
                    u[cu].x = x;
                    l[cl].x = x;
                    ans.push_back(x);
                    curs = 0;
                }
                
            }
        }
        
        printf("Case #%d: ", cur_test);
        cout << endl;
        for (int i = 0; i < ans.size(); ++i) {
            printf("%.10lf\n", ans[i]);
        }
        
    }
    

    return 0;
}