#include <cstdlib>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

int main() 
{
	/*string fname = "D-small-attempt0";   // for small input file at first attempt*/
	string fname = "D-large";          // for large input file
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	const int L=1000;
    int T,N,rnd,perm;
    int A[L];
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c){
		scanf("%d",&N);
		rnd=N;perm=0;
		for(int d = 1 ; d <= N ; d++ ){
                scanf("%d ", &A[d]); 
                if (A[d]==d) rnd--;
                }
		for(int d = 1 ; d <= N-1 ; d++ ){
                for(int e = d+1 ; e <= N ; e++)
                if(A[e]==d && A[d]==e) {rnd-=2; perm++;}
                }
                
	printf("Case #%d: %f\n",c,rnd+perm*2.0);
    }
	return 0;
}
