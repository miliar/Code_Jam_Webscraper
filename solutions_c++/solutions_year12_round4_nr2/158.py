


#include <iostream>
#include <iomanip>
#include <fstream>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#include <sstream>
#include <string>

#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>

#include <algorithm>

#include <utility>

using namespace std;



const int inf = 2000000000;
const long long linf = 9000000000000000000LL;
const double finf = 1.0e18;
const double eps = 1.0e-8;

struct node {
	int i;
	int r;
	int x, y;
}a[1005];


bool fr(node i, node j) {
	return i.r>j.r;
}

bool fi(node i, node j) {
	return i.i<j.i;
}




int T, n, w, l, r[1005];


long long dis(int x, int y, int X, int Y) {
	return ((X-x)*(long long)(X-x) +(Y-y)*(long long)(Y-y));
}

bool put(int I, int X, int Y) {
if ((0<=X)&&(X<=w)&&(0<=Y)&&(Y<=l)) {
	for (int i=1; i<I; i++) {
		if (dis(a[i].x, a[i].y, X, Y)<(a[I].r+a[i].r)*(long long)(a[I].r+a[i].r)) return false;
	}
	return true;
}
else return false;
}


int main() {

	scanf("%d",&T);
	for (int tt=1; tt<=T; tt++) {
		scanf("%d%d%d",&n, &w, &l);
		for (int i=1; i<=n; i++) {
			scanf("%d",&a[i].r);
			a[i].i = i;
			a[i].x = a[i].y = -1;
		}
		
		
		
		sort(a+1, a+1+n, fr);
		for (int i=1; i<=n; i++) {
			if (i==1) {
				a[i].x = a[i].y = 0;
			}
			else {
				for (int j=1; j<i; j++) {
					if (put(i, a[j].x+a[j].r+a[i].r, a[j].y)) {
						a[i].x = a[j].x+a[j].r+a[i].r;
						a[i].y = a[j].y;
					}
					else 
					if (put(i, a[j].x, a[j].y+a[j].r+a[i].r)) {
						a[i].x = a[j].x;
						a[i].y = a[j].y+a[j].r+a[i].r;
					}
					
				}
			}
			
			
		}
		sort(a+1, a+1+n, fi);
		
			printf("Case #%d:",tt);
			for (int i=1; i<=n; i++) {
				printf(" %d %d", a[i].x, a[i].y);
			}
			printf("\n");
		
		
		
		
	
	}
	
	return 0;
}


