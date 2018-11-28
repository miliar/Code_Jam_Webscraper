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
	/*string fname = "C-small-attempt0";   // for small input file at first attempt*/
	string fname = "C-large";          // for large input file
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
    int T,N,K;
    int long low,XR,sum;
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c){
		scanf("%d",&N);
		sum=XR=0;
		for(int d = 1 ; d <= N ; d++ ){
                scanf("%d ", &K);
                
                sum  += K;
                if(d == 1) low=K; 
                else if(K<low) low=K;
                XR = XR xor K;
            
	}
	if(XR == 0)
	printf("Case #%d: %d\n",c,sum-low);
	else
	printf("Case #%d: NO\n",c);
    }
	return 0;
}
