// =========================================================
// 
//       Filename:  A.cpp
// 
//    Description:  
// 
//        Version:  1.0
//        Created:  05/21/2011 09:04:46 AM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  LI YAN (lyan), lyan@cs.ucr.edu
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 05/21/2011, LI YAN
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
    cout << "Case #" << (t+1) << ":\n";

    int N; cin >> N;
    vector<string> vs(N);
    for(int i=0; i<N; ++i) cin >> vs[i];

    // RPI = 0.25*WP + 0.50*OWP + 0.25*OOWP
    vector<double> winp(N,0.0), owp(N,0.0);
    for(int i=0; i<N; ++i) {
        int win=0, loss=0, sum=0;
        for(int k=0; k<N; ++k) if (vs[i][k]!='.') {
            win += (vs[i][k]=='1');
            loss += (vs[i][k]=='0');
        }
        sum = win+loss;
        winp[i] = (double)win/sum;
        double ototal = 0.0, ocnt=0;
        for(int k=0; k<N; ++k) if (vs[i][k]!='.') {
            int oloss=0, owin=0;
            for(int j=0; j<N; ++j) if (j!=i&&vs[k][j]!='.') {
                owin += (vs[k][j]=='1');
                oloss += (vs[k][j]=='0');
            }
            assert(owin+oloss>0);
            double owp = (double)owin/(owin+oloss);
            ototal += owp; ocnt++;
        }
        assert(ocnt>0);
        owp[i] = ototal / ocnt;
    }
    for(int i=0; i<N; ++i)
    {
        double oowp=0.0, cnt=0;
        for(int k=0; k<N; ++k) if (k!=i && vs[i][k]!='.') 
        { oowp += owp[k]; cnt++; }
        oowp /= cnt;
        double rpi = 0.25*winp[i] + 0.50*owp[i] + 0.25*oowp;
        cout << fixed << setprecision(10) << rpi << endl;
    }

}

int main()
{
    int T; cin >> T;
    for(int t=0; t<T; ++t)
        solve(t);
}
