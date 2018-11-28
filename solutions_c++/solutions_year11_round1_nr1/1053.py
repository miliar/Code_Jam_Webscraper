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

int see(int N, int D, int G){
	int re = 0;
	if (G==100 && D != 100)
		return 0;
	if (D !=0 && G == 0)
		return 0;
	for(int tI=1; tI <= N; tI++) {
		for(int tJ=tI; tJ >= 0; tJ--) {
			if ((tJ*100)%tI == 0 && (tJ*100)/tI == D) {
				//printf("@@@DW=%d,D=%d\n",tJ,tI);								
				return 1;									
			}
		}
	}
	return 0;
}

int main(){
	freopen("A-large.in","rt",stdin);
	freopen("t3.out","wt",stdout);
	int cases = 0;
	scanf("%d",&cases);
	
	for (int iii = 1; iii <= cases; iii++) {		
                int N,D,G;
		scanf("%d%d%d",&N,&D,&G);
		int re = see(N,D,G);
		if (re == 0)
			printf("Case #%d: Broken\n",iii);
		else
			printf("Case #%d: Possible\n",iii);
	}
	return 0;
}
