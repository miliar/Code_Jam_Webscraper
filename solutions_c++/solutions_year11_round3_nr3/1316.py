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
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
	int cases = 0;
	int player[10001];
	scanf("%d",&cases);
	
	for (int iii = 1; iii <= cases; iii++) {		
		int N,L,H;
		scanf("%d%d%d",&N,&L,&H);
		for(int i = 0; i < N; i++) {
			scanf("%d",&player[i]);
		}
		int re = -1;
		for(int i = L; i <= H; i++) {
			int j = 0;
			for ( ; j < N; j++) {
				if (i%player[j] == 0) 
					continue;
				else {
					if (player[j]%i == 0) {
						continue;		
					} 
					break;
				}
			}
			if (j >= N) {
				re = i;
				break;
			}
		}
		if (re == -1) 
			printf("Case #%d: NO\n",iii);
		else 
			printf("Case #%d: %d\n",iii,re);
	}
	return 0;
}
