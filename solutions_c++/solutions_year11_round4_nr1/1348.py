// =========================================================
// 
//       Filename:  A.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  06/04/2011 07:13:06 AM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  LI YAN (lyan), lyan@cs.ucr.edu
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 06/04/2011, LI YAN
// 
// =========================================================

#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <string>
#include <vector>
#include <set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define INF (1<<29)
#define fort(i,a) for(typeof a.begin() i=a.begin(); i!=a.end(); ++i)
#define ALL(x) x.begin(), x.end()
#define PB push_back
#define MP make_pair
#define SIZE(x) int(x.size())

struct myseg {
    int B, E, W;
};

bool operator<(myseg s1, myseg s2) {
    return s1.W < s2.W;
}

void solve(int tt)
{
    double ans=0.0;
    int X,S,R,trun,N; cin >> X >> S >> R >> trun >> N; //cout << X << " " << S  << " " << R << " " << t << " " << N << endl;
    double t = trun;
    vector<myseg> vec(N);
    for(int i=0; i<N; ++i) { cin >> vec[i].B >> vec[i].E >> vec[i].W; };
    sort(vec.begin(), vec.end());

    int walk=X; for(int i=0; i<N; ++i) { walk -= (vec[i].E-vec[i].B); }
    if (walk >= R*t) { ans += t; ans += (double)(walk-R*t)/S; t=0; }
    else { double t1 = (double)walk/R; ans += t1; t-=t1; }

    for(int i=0; i<N; ++i) {
            int sp = R+vec[i].W;
            double d = vec[i].E-vec[i].B;
            if (d<= sp*t) { ans += d/sp; t-=d/sp; }
            else { ans += t; ans += (d-sp*t)/(S+vec[i].W); t=0; }
    }

    cout << "Case #" << (tt+1) << ": ";
    cout << fixed << setprecision(10) << ans << endl;
}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
