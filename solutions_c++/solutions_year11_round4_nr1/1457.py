#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <assert.h>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

struct ww {
    int bi, ei, wi;
};

bool cmp(ww a, ww b)
{
    if(a.wi != b.wi) return a.wi < b.wi;
    return (a.ei - a.bi) < (b.ei - b.bi);
}

ww ws[1111];

int bi[1111];
int ei[1111];
int wi[1111];

int x, s, r, t, n;

long double dt;
long double res;

void move(long double wws, long double dst)
{
    if(dt <= 0){
        res += (long double) dst / (long double)(wws + s);
    } else if( dst / (long double)(r + wws) <= dt){
        res += dst / (long double)(r + wws);
        dt -= dst / (long double)(r + wws);
    } else if(dt >= 0){
        long double run = dt * (long double)(r + wws);
        long double run_time = dt;
        long double walk = dst - run;
        long double walk_time = walk / (long double)(wws + s);

        res += run_time + walk_time;
        dt = -1.0;
    }
}

int main()
{
    int tt;
    scanf("%d", &tt);
    FOR(testcase, 0, tt){
        scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
        FOR(i, 0, n){
            scanf("%d %d %d", &bi[i], &ei[i], &wi[i]);
            ws[i].bi = bi[i];
            ws[i].ei = ei[i];
            ws[i].wi = wi[i];
        }
        assert(n > 0);

        dt = (long double)t;
        res = 0.0;
        FOR(i, 0, n){
            if(i == 0) move(0.0, (long double)bi[i]);
            else move(0.0, (long double)(bi[i] - ei[i - 1]));
        }
        move(0.0, (long double)(x - ei[n - 1]));

        sort(ws, ws + n, cmp);
        FOR(i, 0, n){
            move((long double) ws[i].wi, (long double)(ws[i].ei - ws[i].bi));
        }

        printf("Case #%d: %.14Lf\n", testcase + 1, res);
    }
    return 0;
}

