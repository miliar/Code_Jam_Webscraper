#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<utility>
#include<iostream>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<ctype.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
int n;
vector<pair<double, int> > vec;
double xx[20], yy[20],L,W;

pair<int, int> check() {
    int i,j;
    for (i=0; i<n; i++) for (j=i+1; j<n; j++) {
        double a = (vec[i].first + vec[j].first);
        a = a * a;
        double b = (xx[vec[i].second] - xx[vec[j].second]); b = b*b;
        double c = (yy[vec[i].second] - yy[vec[j].second]); c = c*c;
        if (a +1e-3 > b + c) return mp(i,j);
    }
    return mp(-1, -1);
}
double getrand(int x) {
    int tem = rand() % (x * 1000);
    return tem/1000.0;
}
void foo(int i, int j) {
    double tem = (vec[i].first + vec[j].first) * (vec[i].first + vec[j].first) /
            ((xx[vec[i].second] - xx[vec[j].second]) * (xx[vec[i].second] - xx[vec[j].second]) +
             (yy[vec[i].second] - yy[vec[j].second]) * (yy[vec[i].second] - yy[vec[j].second]));
    xx[vec[i].second] = (xx[vec[i].second] - xx[vec[j].second]) * tem + xx[vec[j].second] + 1e-5;
    if (xx[vec[i].second] < 1e-6 || xx[vec[i].second] > L - 1e-6) {
        xx[vec[i].second] = getrand(L);
    yy[vec[i].second] = getrand(W);
        return;
    }
    yy[vec[i].second] = (yy[vec[i].second] - yy[vec[j].second]) * tem + yy[vec[j].second] + 1e-5;
    if (yy[vec[i].second] < 1e-6 || yy[vec[i].second] > W - 1e-6) {
        xx[vec[i].second] = getrand(L);
    yy[vec[i].second] = getrand(W);
        return;
    }
    
    
}

int main () {
    int i, j, m, TC=1,ans,k,N;
    double tem;
    scanf("%d", &N);
    while (N--) {
        scanf("%d%lf%lf", &n, &L, &W);
        vec.clear();
        for (i=0; i<n; i++) {
            scanf("%lf", &tem);
            vec.pb(mp(tem, i));
        }
        sort(vec.begin(), vec.end());
        //puts("1111");
        //printf("--%d\n", n);
        xx[vec[n-1].second] = 0; yy[vec[n-1].second] = 0;
        //puts("222");
        if (n>=2) xx[vec[n-2].second] = L, yy[vec[n-2].second] = W;
        //puts("222");
        for (i=0; i<n-2; i++) xx[vec[i].second] = getrand(L), yy[vec[i].second] = getrand(W);
        pair<int, int> tt;
         //puts("222");
        while (1) {
            tt = check();
            if (tt.first == -1) break;
            foo(tt.first, tt.second);
        }
        printf("Case #%d:", TC++);
        for (i=0; i<n; i++) printf(" %lf %lf", xx[i], yy[i]);
        puts("");
    }
    return 0;
}
