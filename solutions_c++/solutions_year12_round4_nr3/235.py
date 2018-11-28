#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// Google CodeJam 2012 Round 2
// Author: Fdg

int h[11]={0};
int arr[11]={0};

int check(int n) {
	for(int i=0;i<n-1;++i) {
		int what=arr[i]-1;
		for(int j=i+1;j<what;++j) {
			double y=h[i]+1.0*(h[what]-h[i])*(j-i)/(what-i);
			if (y<=h[j]) return what;
		}
		for(int j=what+1;j<n;++j) {
			double y=h[i]+1.0*(h[what]-h[i])*(j-i)/(what-i);
			if (y<h[j]) return what;
		}
	}
	return -1;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;++test) {
		printf("Case #%d:",test);
		int n;
		scanf("%d",&n);
		for(int i=0;i<n-1;++i) {
			h[i]=1;
			scanf("%d",&arr[i]);
		}
		h[n-1]=1;
		for(int it=0;it<10000000;++it) {
			int r=check(n);
			if (r==-1) break;
			h[r]++;
		}
		if (check(n)!=-1) puts(" Impossible");
		else {
			for(int i=0;i<n;++i)
				printf(" %d",h[i]);
			printf("\n");
		}
	}
	return 0;
}
