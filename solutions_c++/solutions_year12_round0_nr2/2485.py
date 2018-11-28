#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))


int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);
	
	//freopen("B-small-attempt2.in", "r", stdin);
	//freopen("B-small-attempt2.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

	int T; 
	scanf("%d\n", &T); // remember to put \n

	rep(i,T) {
		int N, S, p;
		//int PD, PG;

		// input
		scanf("%d", &N); 
		scanf("%d", &S); 
		scanf("%d", &p); 
    //printf("%d %d %d ", N, S, p);
    int cnt = 0; // counter

		// processing
    int TT1 = (p-1)*3 + 1;
    if (TT1 < 0) TT1 = p;

    int TT2 = (p-1)*3 - 1;
    if (TT2 < 0) TT2 = p;
    rep(j, N) {
      int tp;
		  scanf("%d", &tp); // total points
      //printf("%d ", tp);

      if (tp >= TT1) cnt++; // not surprising cases
      else if ((S > 0) && (tp >= TT2)) { cnt++; S--; } // surprising cases
    }

		// output
    //printf("\n");
		printf("Case #%d: %d\n", i + 1, cnt);
   //printf("\n");
	}

	return 0;
}

