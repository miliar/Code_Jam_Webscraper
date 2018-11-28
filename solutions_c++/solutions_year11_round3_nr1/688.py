/**
 * Author        : mahbub
 * Problem Name  : GCJ.R1C.Problem_A._Square_Tiles
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

int main() {
	freopen("GCJ.R1C.A.in.txt", "r", stdin);
	freopen("GCJ.R1C.A.out.txt","w", stdout);
	int tcases, r, c;
	char grid[52][52];
	Sf("%d",&tcases);

	For(tcase, 1, tcases) {
		Sf("%d %d",&r, &c);
		gets(grid[0]);
		Rep(i, r) {
			gets(grid[i]);
		}
		bool flg = true;
		Rep(i, r) {
			Rep(j, c) {
				if (grid[i][j]=='#') {
					if (j+1<c && grid[i][j+1]=='#' && i+1<r && grid[i+1][j]=='#' && grid[i+1][j+1]=='#') {
						grid[i][j]='/';
						grid[i][j+1]='\\';
						grid[i+1][j]='\\';
						grid[i+1][j+1]='/';
					} else {
						flg = false;
						break;
					}
				}
			}
			if (!flg) break;
		}
		Pf("Case #%d:\n", tcase);
		if (flg) {
			Rep(i, r) {
				puts(grid[i]);
			}
		} else {
			Pf("Impossible\n");
		}
	}
	Re 0;
}