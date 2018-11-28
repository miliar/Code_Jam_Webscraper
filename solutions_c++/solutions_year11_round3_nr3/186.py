// =========================================================
// 
//       Filename:  Csmall.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/22/2011 02:23:22 AM
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

void solve(int t)
{
    string bad="NO";

    int N, L, H; cin >> N >> L >> H;

    VI other(N);
    for(int i=0; i<N; ++i) cin >> other[i];

    int ans;
    for(ans=L; ans<=H; ++ans)
    {
        bool good = true;
        for(int i=0; i<N; ++i) if (ans%other[i]!=0 && other[i]%ans!=0) { good=false; break; }
        if (good) break;
    }
    cout << "Case #" << (t+1) << ": ";
    if (ans > H) cout << bad << endl;
    else cout << ans << endl;
}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
