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

// End of Function Declarations

// Functions Used

int main() {
    int ret=Solve();
    return 0;
}

int Solve() {
    int i,j,k;
    int t;  
    int L,P,C;
    GI(t);
    REP(k,t) {
        GI(L);GI(P);GI(C);
        int num = L;
        VI v;
        int ans = 1;
        while(num<P) {
            v.pb(num);
            num*=C;
        }    
        v.pb(num);
        int start = 0;
        int end = sz(v)-1;
        bool flag = true;
        while(flag) {
            int mid = (start+end)/2;
            if(v[mid]*C>=P) {
                flag = false;
            }
            else  {
                start=mid;
                ans++;
            }
        }
        if(L*C>=P) ans = 0;
        cout<<"Case #"<<k+1<<": "<<ans<<endl;
    }
    return 0;
}
