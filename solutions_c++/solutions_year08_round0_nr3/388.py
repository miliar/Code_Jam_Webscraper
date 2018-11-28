#pragma warning(disable : 4018)
#include <map>
#include <assert.h>
#include <set>
#include <sstream>
#include <iostream>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <numeric>

#ifdef __GNUC__
typedef long long lint;
typedef unsigned long long ulint;
#else
typedef __int64 lint;
typedef unsigned __int64 ulint;
#endif

using namespace std;

#define FOR(iter, bound) for(size_t iter=0; iter < (bound); iter++)
#define SFOR(iter, start, bound) for (int iter = (start); iter<(bound); iter++)
#define ALL(C) C.begin(), C.end()
#define VSORT(vec) sort(ALL(vec))
#define MP(a, b) make_pair((a), (b))

typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<int> VI;
typedef vector<lint> VL;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<double> VD;
typedef vector<vector<double> > VVD;
typedef pair<int, int> PII;
typedef vector<PII> VP;
typedef vector<VP> VVP;

VS Parse(string str, string look_for = " ", bool i_push_empty = false)
{
    VS ans;
    if (look_for.length() == 0)
    {
        ans.push_back(str);
        return ans;
    };
    string last = "";
    int pos = 0;
    while (true)
    {
        if (pos == str.length())
        {
            if (last.length() != 0)
                ans.push_back(last);
            return ans;
        };
        if (look_for.find(str[pos]) == string::npos)
            last.append(1, str[pos]);
        else
        {
            if (i_push_empty || last.length() != 0)
                ans.push_back(last);
            last = "";
        };
        pos++;
    };
    return ans;
};


template<class C>
void PRV(vector<C> vec)
{
    cout << "{";
    FOR(i, vec.size()) {cout << vec[i] << ",";};
    cout << "}";
};


lint GetLint(string ss)
{
    lint ans = 0;
    int pos = 0;
    while (pos < ss.length() && !isdigit(ss[pos]))
        pos++;
    while (pos < ss.length() && isdigit(ss[pos]))
        ans *= lint(10), ans += lint(ss[pos++] - '0');
    return ans;
}

double f, R, t, r, g, S;

double inter(double cat1) {
    return pow(max(0., R * (double)R - cat1 * cat1), 0.5);
}

double PI;

double triArea(double a, double b, double c) {
    assert(a > 0 && b > 0 && c > 0);
    double p = (a + b + c) / 2;
    return pow(p * (p - a) * (p - b) * (p - c), 0.5);
}

double integral(double x1, double x2, double y2) {
    assert(fabs(x2*x2 + y2 * y2 - R * R) < 1e-8 * R);
    if (x1 > x2) {
        double u = x1;
    }
    double an2 = atan2(y2, x2);
    double y1 = inter(x1);
    double an1 = atan2(y1, x1);
    double ans = (R * fabs(an2 - an1) * R) / 2.;
    double dst = hypot(x1, y2);
    return ans - triArea(dst, x2 - x1, R) - triArea(dst, y1 - y2, R);
}

double squareCircle(double x, double y) {
    double y2 = inter(x + g);
    double y1 = inter(x);
    if (y1 <= y)
        return 0;
    if (y2 >= y + g)
        return g * g;
    double x1 = inter(y);
    double x2 = inter(y + g);
    if (x1 < x)
        return 0;
    if (x2 >= x + g) {
        assert(0);
        return g * g;
    }
    if (y2 > y) {
        if (x2 >= x)
            return g * (x2 - x) + integral(x2, x + g, y2) + (x + g - x2) * (y2 - y);
        return integral(x, x + g, y2) + (y2 - y) * g;
    }
    if (y1 <= y + g)
        return integral(x, x1, y);
    return integral(x2, x1, y) + g * (x2 - x);
}

void ff() {
    double total = R * PI * R / 4;
    double good = 0;
    S = 2 * r + g;
    R -= t;
    R -= f;
    if (R <= 0 || g <= 2*f) {
        printf("1.000000");
        return;
    }
    g -= 2 * f;
    r += f;
/*    double y = 0;
    while (true) {
        double x = inter(y + S);
        if (inter(y) < x || x <= 0)
            break;
        int mm = (int)(x / S);
        double sg = good;
        good += g * mm * g;
        x = mm * S;
        while (true) {
            if (inter(y) < x)
                break;
            double delta = squareCircle(x + r, y + r);
            good += delta;
            x += S;
        }
        y += S;
    }*/
    for (double x = 0; x < R; x += S)
        for (double y = 0; y*y + x*x < R* R; y += S)
            good += squareCircle(x + r, y + r);

    double res = good / total;
    printf("%.6f", 1. - res);
}

void main() {
    FILE* in = freopen("d:\\contests\\usaco\\C-small.in", "r", stdin);
    FILE* out = freopen("d:\\contests\\usaco\\C-small.out", "w+", stdout);


    PI = 4 * atan(1.);
    int N1;
    cin >> N1;
    FOR(q, N1) {
        cin >>  f>> R>> t>> r>> g ;
        cout << "Case #" << (q + 1) << ": ";
        ff();
        cout << endl;
    }
    fclose(in);
    fclose(out);

}
