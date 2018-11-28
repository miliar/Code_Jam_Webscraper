/*
TASK: A
LANG: C++
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())


int main(){
	freopen("A-large.in","rt",stdin);
	freopen("large.out","wt",stdout);
	int N;
	scanf("%d",&N);
	
	for (int iii = 1; iii <= N; iii++) {		
                int NN;
                scanf("%d",&NN);
                int step = 0;
		int button[200];
		char St[200];
                for(int jj = 0; jj < NN; jj++){
			char c;
			scanf("%c", &c);
			scanf("%c", &St[jj]);
			scanf("%d", &button[jj]);
		}          
		int pc=1,pn=1;
		int ii = 1;
		for(; ii < NN; ii++) {
			if (St[ii] != St[0]){
				break;
			}
		}
		for(int jj = 0; jj < NN; ) {
			step++;
			if (ii>=NN)
				;
			else if (button[ii] == pn)
				;
			else if (button[ii] > pn){
				pn++;
			}
			else if (button[ii] < pn) {
				pn--;
			}
			if (button[jj] == pc) {						
				if (jj+1 < NN){
					if (St[jj] != St[jj+1]){
						int temp = pc;
						pc = pn;
						pn = temp;	
						ii = jj + 2;	
						for(; ii < NN; ii++) {
							if (St[ii] == St[jj])
							break;
						}		
					}	
				}
				jj++;	// press button				
			} else if (button[jj] > pc) {
				pc++;			
			} else if (button[jj] < pc) {
				pc--;			
			} 	        	
		}
		printf("Case #%d: %d\n",iii,step);
	}
	return 0;
}
