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
	string fname = "A-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
    int T,K,N;
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) 
    {
		scanf("%d %d", &N, &K);
		K=K%(1<<N);
		if(K==((1<<N)-1))
		printf("Case #%d: ON\n", c);
		else
		printf("Case #%d: OFF\n", c);
	}

	return 0;
}
