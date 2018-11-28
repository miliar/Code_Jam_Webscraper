/*
Author : SRIRAM S
*/
// Libs 
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,A,n) for(i=A;i<n;i++)
#define sz(c) (signed int) c.size()
#define pb(c) push_back(c)
#define INF (int) 1e9
#define all(c) c.begin(),c.end()
#define GI(t) scanf("%d",&t)
#define VI vector<int>
#define PII pair <int,int>
typedef long long LL;

using namespace std;

// Global Vars 

// End of Global Vars

// Function Declarations

int Solve();
bool cmp(PII a, PII b);

// End of Function Declarations

// Functions Used

int main() {
    int ret=Solve();
    return 0;
}

bool cmp(PII a, PII b) {
    if(a.second<b.second) return true;
    else {
        if(a.second==b.second) {
            if(a.first<=b.first) return true;
            else return false;
        }    
        else return false;
    }
}

int Solve() {
    int i,j,k,l;
    int t,N;
    GI(t);
    REP(l,t) {
        GI(N);
        int x,y;
        vector<PII>v;
        REP(i,N) {
            GI(x);GI(y);
            v.pb(make_pair(x,y));
        }
        sort(all(v),cmp);
        int ans = 0;
        REP(i,N) {
            PII p = v[i];
            for(j=i-1;j>=0;j--) {
                if(v[j].second<p.second && v[j].first>p.first) ans++;
            }
            
        }
        cout<<"Case #"<<l+1<<": "<<ans<<endl;
    }
    return 0;
}
