#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
long long C,D;
double P[222];
long long V[222];
using namespace std;

int okay(double mid) {
    double last = 0;
    long i,j,k;
    for (i = 1; i <= C;i++) {
        for (j = 1; j <= V[i]; j++){
            if (P[i] + mid < last + D) return 0;
            last += D;
            if (P[i] - mid > last ) last = P[i] - mid;
        }        
    }
    return 1;
}

int solve(int x){
    long long i,j;
    double s;
    cin >> C >> D;
    for (i = 1; i <= C; i++) cin >> P[i] >> V[i];
    for (i = 1; i <= C; i++) P[i] = P[i] + 1e13;
    s = 0;
    for (i = 1; i <= C; i++) s += V[i];
    s = (s-1) * D;
    double dau,cuoi,mid;
    dau = 0; cuoi = s;
    while (dau < cuoi - 1e-8) {
        mid = (dau + cuoi)/2;
        if (okay(mid)) cuoi = mid; else dau = mid; 
    }
    cout<<"Case #"<<x<<": "<<mid<<"\n";
}

int main() {
    
    freopen("B-small-0.in", "rt", stdin);
    freopen("b.out", "wt", stdout);
    int t,i,j;
    cin >> t;
    for (i = 1;i <= t; i++) {
        solve(i);
    }
}
