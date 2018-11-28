
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

#define PROB_ID "A"
#define INPUT_SIZE "small" //"large" //  

int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);
		
	freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
  freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

  const char in[27] = "abcdefghijklmnopqrstuvwxyz";
  const char gg[27] = "ynficwlbkuomxsevzpdrjgthaq";


	int T; 
	scanf("%d\n", &T); // remember to put \n

	char L[128];
	char out[128];

	rep(i, T) {
		// inputs
		gets(L); // read input
		int len = strlen(L);
    strcpy(out, L);

    rep (j, len) {
      if ((out[j] >= 'a') && (out[j] <= 'z')) {
        int idx = 0;
        while (idx < 27) {
          if (gg[idx] == out[j]) { out[j] = in[idx]; idx = 28; }
          idx++;
        }
      }
    }
		printf("Case #%d: %s\n", i+1, out);
	}

	return 0;
}
