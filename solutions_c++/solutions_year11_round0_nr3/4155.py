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
    int i,j,t,n;
	GI(t);
	REP(i,t) {
		GI(n);
		int minimum = INF, sum = 0;
		int Xor = 0;
		int temp;
		REP(j,n) {
			GI(temp);
			Xor = Xor ^ temp;
			sum += temp;
			minimum = min(minimum, temp);
		}
		if(Xor) printf("Case #%d: NO\n",i+1);
		else printf("Case #%d: %d\n",i+1,sum-minimum);
	}
    return 0;
}
	
