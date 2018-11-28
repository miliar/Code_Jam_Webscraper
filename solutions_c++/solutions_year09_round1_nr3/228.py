#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <functional>
#include <cctype>
#include <iomanip>
#include <cmath>
#include <cstdio>

using namespace std;

int c, n;

bool got[1<<10][1001];
double dp[1<<10][1001];

vector<int> mySet[11][11];

double solve(int curSet, int iterations) {
    if (iterations > 1000) return 0;
    if((curSet + 1) == (1 << c)) return 0;
    if(got[curSet][iterations]) return dp[curSet][iterations];
    double ret = 0;
    int possible = 0;
    for(int i=0;i<mySet[c][n].size();i++) {
            ret+= 1 + solve(curSet | mySet[c][n][i], iterations+1);
            possible++;
    }
    got[curSet][iterations]=1;
    return dp[curSet][iterations]=ret/possible;
}

void solve(int cnum) {
    memset(got,0,sizeof(got));
    cin>>c>>n;
    printf("Case #%d: %.06f\n", cnum, solve(0, 0));
    //cout<<"Case #"<<cnum<<": "<<setprecision(8)<<solve(0, 0)<<endl;
}

int main() {
    for(int myc=0;myc<=10;myc++)
        for(int i=0;i<(1<<myc);i++) {
            mySet[myc][__builtin_popcount(i)].push_back(i);
        }
    int cases;
    cin>>cases;
    for(int cnum=1;cnum<=cases;cnum++) {
        solve(cnum);
    }
}

