// =========================================================
// 
//       Filename:  A.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/20/2011 05:59:13 PM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  LI YAN (lyan), lyan@cs.ucr.edu
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 05/20/2011, LI YAN
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

LL gcd(LL a, LL b)
{
    if (b==0) return a;
    return gcd(b,a%b);
}
void solve(int t)
{
    LL N, D, G;
    cin >> N >> D >> G;
    string good="Possible", bad="Broken";
    string ans;

    if (D==0) {
        if (G==0) ans=good;
        else if (G==100) ans=bad;
        else ans = good;
    }
    else if (G==0) ans=bad;
    else if (G==100 && D<100) ans=bad;
    else {
        LL g = gcd(D,100LL);
        LL p = D/g, q=100/g;
        if (q<=N) {  ans = good; }
        else ans = bad;
    }
    cout << "Case #" << (t+1) << ": ";
    cout << ans << endl;
}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
