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
	
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);

	int T; 
	scanf("%d\n", &T); // remember to put \n

	rep(i,T) {
		int A, B;

    // input
		scanf("%d", &A); 
		scanf("%d", &B); 
    //printf("%d %d %d ", N, S, p);
    int cnt = 0; // counter
    
		// processing
    char lenB[10];
    sprintf(lenB, "%d", B);
    int len = strlen(lenB);
    if (len < 2) { printf("Case #%d: %d\n", i + 1, cnt); continue; }

    char lenJ[10];
    char lenk[10];
    lenk[0] = 0;

    int intk[10];
    int cntk = 0;
    rep(kk, 10) intk[0] = -1;

    fo(j,A,B) {
      lenJ[0] = 0;
      sprintf(lenJ, "%d", j);

      int cntk = 0;
      rep(kk, 10) intk[0] = -1;

      lenk[0] = 0;
      sprintf(lenk, "%d", j); 
      rep (k, len) {
        char tt = lenk[len - 1];
        for (int m = len - 1; m > 0; m--) lenk[m] = lenk[m-1];
        lenk[0] = tt;
        if (tt != '0') {
          int ii = atoi(lenk);
          if ((j < ii) && (ii <= B)) {
            bool found = false;
            rep(kk, cntk) {
              if (intk[kk] == ii) { found = true; break; }
            }
            if (!found) {
              cnt++;
              intk[cntk] = ii;
              cntk++;
            }
          }
        }
      }
    }
 
		// output
    //printf("\n");
		printf("Case #%d: %d\n", i + 1, cnt);
   //printf("\n");
	}

	return 0;
}

