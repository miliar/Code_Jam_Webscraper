// =========================================================
// 
//       Filename:  A.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/22/2011 02:06:36 AM
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

int R, C;

bool good(int r, int c)
{
    return 0<=r && r<R && 0<=c && c<C;
}
void solve(int t)
{
    string bad="Impossible";
    cin >> R >> C;

    vector<string> grid(R);
    for(int i=0; i<R; ++i) cin >> grid[i];

    bool ans=true;
    for(int r=0; r<R; ++r)
    for(int c=0; c<C; ++c)
    {
        if (grid[r][c] == '#') {
            grid[r][c] = '/';
            if (good(r,c+1) && grid[r][c+1]=='#') grid[r][c+1] = '\\'; else { ans=false; goto done; }
            if (good(r+1,c) && grid[r+1][c]=='#') grid[r+1][c] = '\\'; else { ans=false; goto done; }
            if (good(r+1,c+1) && grid[r+1][c+1]=='#') grid[r+1][c+1] = '/'; else { ans=false; goto done; }
        }
    }
    done:
    cout << "Case #" << (t+1) << ":\n";
    if (!ans) cout << bad << endl;
    else {
        for(int r=0; r<R; ++r) cout << grid[r] << endl;
    }

}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
