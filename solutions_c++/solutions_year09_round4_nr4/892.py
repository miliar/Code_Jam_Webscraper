#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MAXR = 350; 
const int MAXC = 20; 
const int MAX = (MAXR + 1) * (MAXC + 1); 
const int INF = 1000000; 
int cid[MAX], rid[MAX], r[MAX], l[MAX], u[MAX], d[MAX]; 
int colct[MAXC + 1]; 
int res[MAXR];  //[\u36873][\u21462][\u30340][\u32467][\u26524] 
int curlim, nextlim; 

inline void rem(const int &col) 
{ 
    l[r[col]] = l[col]; 
    r[l[col]] = r[col]; 
    for (int rr = d[col]; rr != col; rr = d[rr]) { 
        l[r[rr]] = l[rr]; 
        r[l[rr]] = r[rr]; 
    } 
} 

inline void rem2(const int &col) 
{ 
    l[r[col]] = l[col]; 
    r[l[col]] = r[col]; 
} 

inline void rem3(const int &col) 
{ 
    for (int cc = r[col]; cc != col; cc = r[cc]) { 
        for (int rrr = d[cc]; rrr != cc; rrr = d[rrr]) { 
            l[r[rrr]] = l[rrr]; 
            r[l[rrr]] = r[rrr]; 
        } 
    } 
} 

inline void bac(const int &col) 
{ 
    for (int rr = u[col]; rr != col; rr = u[rr]) { 
        l[r[rr]] = rr; 
        r[l[rr]] = rr; 
    } 
    l[r[col]] = col; 
    r[l[col]] = col; 
} 

inline void bac2(const int &col) 
{ 
    l[r[col]] = col; 
    r[l[col]] = col; 
} 

inline void bac3(const int &col) 
{ 
    for (int cc = l[col]; cc != col; cc = l[cc]) { 
        for (int rrr = u[cc]; rrr != cc; rrr = u[rrr]) { 
            l[r[rrr]] = rrr; 
            r[l[rrr]] = rrr; 
        } 
    } 
} 

void findmin(int &minc, int &minn) 
{ 
    minn = INF; 
    for (int cc = r[0]; cc != 0; cc = r[cc]) { 
        if (colct[cc] < minn) { 
            minn = colct[cc]; 
            minc = cc; 
        } 
    } 
} 

int calh() 
{ 
    if (r[0] == 0) { 
        return 0; 
    } 
    int minc, minn, res; 
    findmin(minc, minn); 
    rem2(minc); 
    for (int rr = d[minc]; rr != minc; rr = d[rr]) { 
        rem3(rr); 
    } 
    res = calh(); 
    for (int rr = u[minc]; rr != minc; rr = u[rr]) { 
        bac3(rr); 
    } 
    bac2(minc); 
    return res + 1; 
} 

bool dfs(int round) 
{ 
    if (r[0] == 0) { 
        return true; 
    } 
    int minc, minn; 
    findmin(minc, minn); 
    for (int rr = d[minc]; rr != minc; rr = d[rr]) { 
        rem3(rr); 
        rem(minc); 
        res[round] = rid[rr]; 
        int ex = calh() + round + 1; 
        if (ex > curlim) { 
            if (ex < nextlim) { 
                nextlim = ex; 
            } 
        } 
        else if (dfs(round + 1)) { 
            return true; 
        } 
        bac(minc); 
        bac3(rr); 
    } 
    return false; 
} 

void addlr(const int &lnode, const int &rnode) 
{ 
    l[r[lnode]] = rnode; 
    r[rnode] = r[lnode]; 
    l[rnode] = lnode; 
    r[lnode] = rnode; 
} 

void addud(const int &unode, const int &dnode) 
{ 
    u[d[unode]] = dnode; 
    d[dnode] = d[unode]; 
    u[dnode] = unode; 
    d[unode] = dnode; 
} 

// [\u34892][\u35206][\u30422][\u21015][\u65292][\u20256][\u20837][\u35206][\u30422][\u30697][\u38453][\u12289][\u34892][\u25968][\u21644][\u21015][\u25968][\u65292][\u36820][\u22238][\u26368][\u23569][\u36873][\u21462][\u30340][\u34892][\u35206][\u30422][\u25152][\u26377][\u21015] 
// [\u31572][\u26696][\u23384][\u25918][\u22312]res[\u25968][\u32452][\u20013][\u65292][\u26080][\u35299][\u36820][\u22238]-1 
int MinCover(const bool matr[MAXR][MAXC], int rownum, int colnum) 
{ 
    for (int i = 0; i < colnum; ++i) { 
        int j; 
        for (j = 0; j < rownum; ++j) { 
            if (matr[j][i]) { 
                break; 
            } 
        } 
        if (j == rownum) { 
            return -1; 
        } 
    } 
    int lastr[MAXC + 1]; 
    memset(colct, 0, sizeof(int) * (colnum + 1)); 
    for (int i = 1; i <= colnum; ++i) { 
        addlr(i - 1, i); 
        u[i] = d[i] = i; 
        lastr[i] = i; 
    } 
    int ind = colnum + 1; 
    for (int i = 0; i < rownum; ++i) { 
        bool first = true; 
        for (int j = 0; j < colnum; ++j) { 
            if (matr[i][j]) { 
                cid[ind] = j + 1; 
                rid[ind] = i + 1; 
                ++colct[j + 1]; 
                if (first) { 
                    first = false; 
                    l[ind] = r[ind] = ind; 
                } 
                else { 
                    addlr(ind - 1, ind); 
                } 
                addud(lastr[j + 1], ind); 
                lastr[j + 1] = ind; 
                ++ind; 
            } 
        } 
    } 
    curlim = calh(); 
    while (1) { 
        nextlim = INF; 
        if (dfs(0)) { 
            return curlim; 
        } 
        else { 
            curlim = nextlim; 
        } 
    } 
} 

const double eps = 1e-8;

int dcmp(double x) {
    return (x > +eps) - (x < -eps);
}

struct point {
    double x, y;
    point() {}
    point(double _x, double _y) : x(_x), y(_y) {}
    point operator + (const point& p) const {
        return point(x + p.x, y + p.y);
    }
    point operator - (const point& p) const {
        return point(x - p.x, y - p.y);
    }
    point operator * (double p) const {
        return point(x * p, y * p);
    }
    point operator / (double p) const {
        return point(x / p, y / p);
    }
    point left() {
        return point(-y, x);
    }
    point right() {
        return point(y, -x);
    }
    point trunc(double l) {
        l /= sqrt(x * x + y * y);
        return point(x * l, y * l);
    }
    bool operator < (const point& p) const {
        return dcmp(x - p.x) < 0 || (dcmp(x - p.x) == 0 && dcmp(y - p.y) < 0);
    }
    bool operator ==(const point& p) const {
        return dcmp(x - p.x) == 0 && dcmp(y - p.y) == 0;
    }
    bool operator !=(const point& p) const {
        return dcmp(x - p.x) != 0 || dcmp(y - p.y) != 0;
    }
};

int n, k;
vector<point> dt, cand;
vector<double> rad;
bool ok[MAXR][MAXC];

double dist(const point& a, const point& b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

bool circle_intersection(const point& s, double rs, const point& t, double rt, point& a, point& b) {
    double dd = dist(s, t);
    if (dcmp(dd - (rs + rt)) >= 0) {
        return false;
    }
    double x1 = (dd * dd + rs * rs - rt * rt) / dd / 2;
    double y1 = sqrt(rs * rs - x1 * x1);
    point mid = s + (t - s).trunc(x1);
    a = mid + ((t - s).left()).trunc(y1);
    b = mid + ((t - s).right()).trunc(y1);
    return true;
}

bool check(double r) {
    vector<double> tmpr = rad;
    for (int i = 0; i < tmpr.size(); ++i) {
        tmpr[i] = r - tmpr[i];
    }
    cand.clear();
    vector<bool> flag(n, false);
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            point a, b;
            if (circle_intersection(dt[i], tmpr[i], dt[j], tmpr[j], a, b)) {
                cand.push_back(a);
                cand.push_back(b);
                flag[i] = flag[j] = true;
            }
            /*
            double d = dist(dt[i], dt[j]);
            if (dcmp(d - 2 * r) == 0) {
                cand.push_back((dt[i] + dt[j]) / 2);
                flag[i] = flag[j] = true;
            }
            else if (dcmp(d - 2 * r) < 0) {
                point b = (dt[j] - dt[i]).left().trunc(sqrt(r * r - d * d / 4));
                cand.push_back((dt[i] + dt[j]) / 2 + b);
                cand.push_back((dt[i] + dt[j]) / 2 - b);
                flag[i] = flag[j] = true;
            }
            */
        }
    }
    sort(cand.begin(), cand.end());
    cand.erase(unique(cand.begin(), cand.end()), cand.end());
    int cnt = 0;
    vector<int> num;
    for (int i = 0; i < n; ++i) {
        if (!flag[i]) {
            ++cnt;
            if (cnt > k) return false;
        }
        else {
            num.push_back(i);
        }
    }
    memset(ok, false, sizeof(ok));
    //    printf("%d\n", cand.size());
    for (int i = 0; i < cand.size(); ++i) {
        for (int j = 0; j < n; ++j) {
            if (flag[j]) {
                int jj = lower_bound(num.begin(), num.end(), j) - num.begin();
                if (dcmp(dist(cand[i], dt[j]) - tmpr[j]) <= 0) {
                    ok[i][jj] = true;
                    //                printf("%d %d\n", i, num[j]);
                }
            }
        }
    }
    int ans = MinCover(ok, cand.size(), num.size());
//    if (ans == -1) return false;
    if (ans <= k - cnt) return true;
    return false;
}

double solve() {
    double low = 0;
    for (int i = 0; i < rad.size(); ++i) {
        low = max(low, rad[i]);
    }
    double ans = 100000;
    double high = 100000;
    //    check(2.3);
    //    return 0;
    while (fabs(high - low) > 1e-10) {
        double mid = (low + high) / 2.0;
        if (check(mid)) {
            ans = min(ans, mid);
            high = mid;
        }
        else low = mid;
    }
    return low;
}

int main() {
    freopen("dd.in", "r", stdin);
    freopen("D-small.out", "w", stdout);
    int t, ca = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        k = 2;
        dt.clear();
        rad.clear();
        for (int i = 0; i < n; ++i) {
            double x, y;
            double r;
            scanf("%lf %lf %lf", &x, &y, &r);
            dt.push_back(point(x, y));
            rad.push_back(r);
        }
        printf("Case #%d: %.8lf\n", ca++, solve());
    }
    return 0;
}
