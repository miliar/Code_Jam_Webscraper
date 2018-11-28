// =========================================================
// 
//       Filename:  C.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/06/2011 05:59:51 PM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  LI YAN (lyan), lyan@cs.ucr.edu
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 05/06/2011, LI YAN
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
    int N; cin >> N;
    int sum=0, minval=1000000, val, parity=0;
    for(int i=0; i<N; ++i)
    {
        cin >> val; minval = min(minval,val);
        sum += val; parity ^= val;
    }
    cout << "Case #" << (t+1) << ": ";
    if (parity==0) cout << (sum-minval) << endl;
    else cout << "NO" << endl;
}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
