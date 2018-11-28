#include <cstdio>
#include <string>
#include <memory.h>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <iomanip>
 
using namespace std;
 
#define forn(i,n) for (int i = 0; i < int(n); i++)
#define pb push_back
#define mp make_pair

typedef long long li;
 
template <typename T> T sqr(const T &x) {
	return x * x;
}
                                    
const int INF = 1e9;                                      
const long double EPS = 1e-9;
const long double PI = acos(-1.0);
const int N = 20002;
		
int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int t;
	scanf("%d\n", &t);
	forn(c, t){
		vector <string> a(4);
		forn(j, 4)
			cin>>a[j];
		int cntx1 = 0, cntx2 = 0, cnty1 = 0, cnty2 = 0;
		bool wonx = false, wono = false;
		int cntp = 0;
		forn(i, 4){
			int cntx_inrow = 0, cntx_incol = 0, cnty_inrow = 0, cnty_incol = 0;
			if(a[i][i] == '.'){				
				cntx1 = -1;
				cnty1 = -1;
			}
			else if(a[i][i] == 'X')
				cntx1++;
			else if(a[i][i] == 'O')
				cnty1++;
			else if(a[i][i] == 'T'){
				cntx1++;
				cnty1++;
			}
			if(a[3 - i][i] == '.'){
				cntx2 = -1;
				cnty2 = -1;
			}
			else if(a[3 - i][i] == 'X')
				cntx2++;
			else if(a[3 - i][i] == 'O')
				cnty2++;
			else if(a[3 - i][i] == 'T'){
				cntx2++;
				cnty2++;
			}
			forn(j, 4){
				if(a[i][j] == 'T'){
					cntx_inrow++;
					cnty_inrow++;
				}
				else if(a[i][j] == 'X'){
					cntx_inrow++;
				}
				else if(a[i][j] == 'O'){
					cnty_inrow++;
				}
				else 
					cntp++;
				if(a[j][i] == 'T'){
					cntx_incol++;
					cnty_incol++;
				}
				else if(a[j][i] == 'X'){
					cntx_incol++;
				}
				else if(a[j][i] == 'O'){
					cnty_incol++;
				}
				else
					cntp++;
			}
			if(cntx_inrow == 4 || cntx_incol == 4)
				wonx = true;
			if(cnty_inrow == 4 || cnty_incol == 4)
				wono = true;
		}
		if(cntx1 == 4 || cntx2 == 4)
			wonx = true;
		if(cnty1 == 4 || cnty2 == 4)
			wono = true;
		if(((wonx && wono) || (!wonx && !wono)) && cntp == 0)
			printf("Case #%d: Draw\n", c + 1);
		else if((!wonx && !wono) && cntp > 0)
			printf("Case #%d: Game has not completed\n", c + 1);
		else if(wonx && !wono)
			printf("Case #%d: X won\n", c + 1);
		else if(!wonx && wono)
			printf("Case #%d: O won\n", c + 1);
	}
   	return 0;
}