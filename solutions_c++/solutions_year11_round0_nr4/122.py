// =========================================================
// 
//       Filename:  Dsmall.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/06/2011 08:22:16 PM
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

double dp[2000];

void init()
{
/* **********
    dp[0]=dp[1]=0; int N=12;
    for(int n=2; n<=N; ++n) {
    VI v(n); for(int i=0; i<n; ++i) v[i]=i;
    int cnt[20]={0};
    do {
        int inpos=0;   
        for(int i=0; i<N; ++i) if (i==v[i]) inpos++;
        cnt[inpos]++;
    } while(next_permutation(v.begin(),v.end()));
    double p[20];
    int fact=1; for(int i=2; i<=n; ++i) fact*=i;
    for(int i=0; i<=n; ++i) p[i]=(double)cnt[i]/fact;

    double num=1.0;
    for(int i=1; i<=n; ++i) num += p[i]*dp[n-i];
    dp[n] = num/(1.0-p[0]);
    }************** */
    dp[0]=dp[1]=0; int N=1050;
    for(int i=2; i<= N; ++i) dp[i]=i;
}

void solve(int t)
{
    int N; cin >> N;
    VI v(N);
    for(int i=0; i<N; ++i) { cin >> v[i]; v[i]--; }
    VI visit(N,0);
    double ans=0.0;
    for(int pos=0; pos<N; ++pos) if (!visit[pos]&&pos!=v[pos])
    {
        int cnt=0, start=pos; visit[pos]=1;
        do { cnt++; pos=v[pos]; visit[pos]=1; } while(pos != start);
        ans += dp[cnt];
    }
    cout << "Case #" << (t+1) << ": ";
    cout << fixed << setprecision(7) << ans << endl;
}

int main()
{
    init();
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
