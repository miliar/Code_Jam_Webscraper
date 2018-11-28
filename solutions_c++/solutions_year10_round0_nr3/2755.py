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
    int R,N,K;
    int t,l;
    GI(t);
    REP(l,t) {
        GI(R);GI(K);GI(N);
        int A[N],B[N];
        memset(A,0,sizeof(A));
        memset(B,0,sizeof(B));
        REP(i,N) GI(A[i]);
        int sum = 0;
        int amount = 0;
        while(R--) {
            sum = 0;
            REP(i,N) {
                if(sum+A[i]>K) break;
                else sum+=A[i];
            }
            amount+=sum;
            k=0;
            for(j=i;j<N;j++) {
                B[k++] = A[j];
            }
            for(j=0;j<i;j++) {
                B[k++] = A[j];
            }
            REP(i,N) A[i] = B[i];

        }
        cout<<"Case #"<<l+1<<": ";
        cout<<amount<<endl;
    }
}
