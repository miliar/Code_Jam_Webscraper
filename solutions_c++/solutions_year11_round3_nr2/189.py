// =========================================================
// 
//       Filename:  Bsmall.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/22/2011 02:39:07 AM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  LI YAN (lyan), lyan@cs.ucr.edu
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 05/22/2011, LI YAN
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

LL calc(LL L, LL t, const vector<LL> &stars)
{
//cout << stars[0] << endl;
    int N = stars.size();
    LL sum=0; for(int i=0; i<N; ++i) sum += stars[i];

    //cout << sum << endl;

    t/=2;
    int pos;
    LL pre=t;
    for(pos=0; pos<N; ++pos) { t-=stars[pos]; if (t<=0) break; }
    if (t>=0 && pos>=N) return sum*2LL;
    //cout << t << " " << pos << endl;

    vector<LL> vec; vec.PB(-t);
    for(int i=pos+1; i<N; ++i) vec.PB(stars[i]);

    //for(int i=0; i<int(vec.size()); ++i) cout << vec[i] << " "; cout << endl;
    sort(vec.begin(), vec.end());
    int K=vec.size();
    LL ans=0;
    for(int i=K-1; i>=0; --i) {
        if (L>0) { ans += vec[i]; --L; }
        else ans += 2*vec[i];
    }
    //cout << pre << " " << ans << endl;
    return 2*pre+ans;
}

void solve(int tt)
{
    LL L, t, N, C; cin >> L >> t >> N >> C; //cerr << "Case " << tt << " " << L << " " << t << " " << N << " " << C << endl;
    vector<LL> stars(N);
    for(int i=0; i<C; ++i) cin >> stars[i];
    for(int i=C; i<N; ++i) stars[i] = stars[i%C];


    LL ans = calc(L,t,stars);
    cout << "Case #" << (tt+1) << ": ";
    cout << ans << endl;
    //cerr << ans << endl;
}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
