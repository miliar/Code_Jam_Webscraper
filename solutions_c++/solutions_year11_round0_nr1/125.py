// =========================================================
// 
//       Filename:  A.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/06/2011 04:26:51 PM
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
    vector<PII> moves;
    for(int i=0; i<N; ++i)
    {
        int pos; string robot; cin >> robot >> pos;
        int id=(robot[0]=='B');
        moves.PB(PII(id,pos));
    }

    int ans=0;
    int pos[2] = {1,1}; int nmove = moves.size();
    for(int curr=0; curr < nmove; ++curr)
    {
        int id=moves[curr].first, next=moves[curr].second;
        int step = abs(pos[id]-next)+1; ans+=step;
        int other = 1-id, pnext=-1;
        for(int p=curr+1; p<nmove; ++p)
          if (moves[p].first == other) { pnext=moves[p].second; break; }
        if (pnext>0) {
            if (abs(pnext-pos[other])<=step) pos[other]=pnext;
            else {
                if (pnext > pos[other]) pos[other]+=step;
                else pos[other]-=step;
            }
        } 
        pos[id] = next;
    }
    cout << "Case #" << (t+1) << ": " << ans << endl;
}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
