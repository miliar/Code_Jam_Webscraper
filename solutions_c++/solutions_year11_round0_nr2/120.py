// =========================================================
// 
//       Filename:  B.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/06/2011 05:33:58 PM
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
    int C, D, N;
    char combine[300][300]; memset(combine, 0, sizeof combine);
    int oppose[300][300]; memset(oppose, 0, sizeof oppose);
    string s;
    cin >> C;
    for(int i=0; i<C; ++i) { cin >> s; combine[s[0]][s[1]] = combine[s[1]][s[0]]= s[2]; }
    cin >> D;
    for(int i=0; i<D; ++i) { cin >> s; oppose[s[0]][s[1]] = oppose[s[1]][s[0]] = 1; }
    cin >> N; cin >> s;
    string ans; ans+=s[0];
    for(int i=1; i<N; ++i)
    {
        if (ans.empty()) { ans += s[i]; continue; }
        char top = ans[ans.size()-1];
        char rep = combine[top][s[i]];
        if (rep) { ans[ans.size()-1] = rep; continue; }
        bool found = false;
        for(int k=0; k<int(ans.size()); ++k)
            if (oppose[ans[k]][s[i]]) { found = true; break;}

        if (found) ans="";
        else ans += s[i];
    }
    cout << "Case #" << (t+1) << ": ";
    cout << "["; if (!ans.empty()) cout << ans[0];
    for(int i=1; i<int(ans.size()); ++i) cout << ", " << ans[i];
    cout << "]\n";
}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
