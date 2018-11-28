/**
 * Author        : mahbub
 * Problem Name  : GCJ.R1B.Problem_A._RPI
 * Algorithm     : 
 * Date          : Saturday, May 21, 2011
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

int matrix[101][101];
double wp[101], owp[101], oowp[101];

int main() {
	freopen("GCJ.R1B.A.in.txt", "r", stdin);
	freopen("GCJ.R1B.A.out.txt", "w", stdout);
	int tcases, n, x;
	char ch;
	Sf("%d", &tcases);
	For (tcase, 1, tcases) {
		Sf ("%d",&n);
		//Clr(matrix);
		Slr(matrix);
		
		Rep(i, n) {
			int p = 0, w = 0;
			Sf("%c", &ch);
			Rep(j, n) {
				Sf("%c", &ch);
				if (ch!='.') {
					p++;
					if (ch=='1') {
						w++;
						matrix[i][j] = 1;
					} else {
						matrix[i][j] = 0;
					}
				}
			}
			wp[i] = w * 1.0 / p;
		}

		Rep(i, n) {
			double cwp = 0;
			int opp = 0;
			Rep(j, n) {
				if (i==j) {Co;}
				if (matrix[i][j]==-1) Co;
				int w=0, p=0;
				Rep(k, n) {
					if (k==i) Co;
					if (matrix[j][k]==1) {
						w++; p++;
					} else if (matrix[j][k]==0) {
						p++;
					}
				}
				cwp += (w*1.0 / p);
				opp++;
			}
			owp[i] = cwp / opp;
		}

		Rep(i, n) {
			double coowp = 0;
			int opp = 0;
			Rep(j, n) {
				if (i==j) Co;
				if (matrix[i][j]!=-1) {
					opp++;
					coowp += owp[j];
				}
			}
			oowp[i] = coowp/ opp;
		}
		Pf("Case #%d:\n", tcase);
		Rep(i, n) {
			double rip = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			Pf("%.7lf\n", rip);
		}
	}
	Re 0;
}