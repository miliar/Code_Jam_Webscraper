/**
 * Author        : mahbub
 * Problem Name  : GCJ.R1C.Problem_C._Perfect_Harmony
 * Algorithm     : 
 * Date          : Sunday, May 22, 2011
 */
#pragma warning ( disable : 4786)
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <ctime>
#include <cstring>
#include <climits>
using namespace std;

#define All(X) X.begin(),X.end()
#define For(i, s, n) for(int i=(s); i<=(n); i++)
#define Rep(i, n) for(int i=0; i<(n); i++)
#define Clr(arr) memset(arr, 0, sizeof(arr))
#define Slr(arr) memset(arr, -1, sizeof(arr))
#define Co continue
#define Re return
#define Sf scanf
#define Pf printf
#define Ss stringstream
#define Ox 2147483647
#define Pi (2.0*acos(0.0))
#define Eps (1e-9)

int gcd(int a, int b) {//[^]
    int c = 0;
    while (b > 0) {
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}


int lcm(int a, int b) {//[^]
    return a / gcd(a, b) * b;
}

int vals[10001];

int main() {
	freopen("GCJ.R1C.C.in.txt", "r", stdin);
	freopen("GCJ.R1C.C.out.txt", "w", stdout);
	int tcases, low, hi, n;

	Sf("%d",&tcases);

	For(tcase, 1, tcases) {
		Sf("%d %d %d", &n, &low, &hi);
		Pf("Case #%d: ",tcase);
		
		Rep(i, n) {
			Sf("%d\n",&vals[i]);
		}

		if (low==1) {
			Pf("1\n");
			Co;
		}

		int out=-1, tmp=-1;
		For(i, low, hi) {
			out = i;
			tmp = 1;
			Rep(j, n) {
				if (!(out%vals[j]==0 || vals[j]%out==0)) {
					tmp=-1;
					break;
				}
			}
			if (tmp > 0) {
				break;
			}
		}
		if  (tmp<0) {
			Pf("NO\n");
		} else {
			Pf("%d\n",out);
		}
	}
	Re 0;
}