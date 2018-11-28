#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <utility>

using namespace std;
//using namespace __gnu_cxx;

typedef long long ll;
typedef double db;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef istringstream is;
typedef ostringstream os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);--(i))
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();++(i))
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define PRINT(v) for(int (i)=0;(i)<(int)(v).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;

string tab[200];
int wins[200];
int sums[200];
double wp[200];
double owp[200];
double oowp[200];

void run(int cnum){
    int n;
    cin >> n;
    REP(i,n){
        wins[i] = 0;
        sums[i] = 0;
        wp[i] = 0.0;
        owp[i] = 0.0;
        oowp[i] = 0.0;
    }

    REP(i,n){
        cin >> tab[i];
        REP(j,n){
            if(tab[i][j] != '.')
                ++sums[i];
            if(tab[i][j] == '1')
                ++wins[i];
        }
        wp[i] = (double)wins[i] / sums[i];
    }
    REP(i,n){
        REP(j,n){
            if(tab[i][j] == '.') continue;
            owp[i] += (double)(wins[j] - (tab[i][j] == '0' ? 1 : 0)) / (sums[j] - 1);
        }
        owp[i] /= sums[i];
    }
    REP(i,n){
        REP(j,n){
            if(tab[i][j] == '.') continue;
            oowp[i] += owp[j];
        }
        oowp[i] /= sums[i];
    }
    cout.precision(12);
    cout << "Case #" << cnum << ":\n";
    REP(i,n)
        cout << wp[i] / 4 + owp[i] / 2 + oowp[i] / 4 << "\n";
}

int main(){
    ios::sync_with_stdio(0);
    int C;
    cin >> C;
    REP(i,C) run(i+1);
    return 0;
}

