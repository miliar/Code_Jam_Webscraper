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
    //clock_t start = clock();
    int ret=Solve();
    //clock_t end = clock();
    //cout <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
    return 0;
}

int Solve() {
    int N,k;
    int t,l;
    GI(t);
    REP(l,t) {
        GI(N);GI(k);
        int i,cnt=0;
        cout<<"Case #"<<l+1<<": ";
        for(i=0;i<N;i++) {
            if(k& (1<<i)) cnt++;
        } 
        if(cnt==N) cout<<"ON\n";
        else cout<<"OFF\n";
    }
}
