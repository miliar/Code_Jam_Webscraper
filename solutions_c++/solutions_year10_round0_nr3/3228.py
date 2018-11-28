/*Theme Park by Oscar Sanchez*/
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <cstring>
#include <fstream>
#include <iostream>
#include <cctype>
#include <string.h>
using namespace std;

int main() {
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int x=1;x<=T;x++) {
		int r,k,n;
		scanf("%d %d %d",&r,&k,&n);
		vector<int>g;
		int t;
		for (int i=0;i<n;i++) {
			scanf("%d",&t);
			g.push_back(t);
		}
		int pos=0;
		long long total=0;
		int tk;
		while(true) {
			if (r<=0) break;
			tk=k;
			int p=pos;
			bool wrap=false;
			for(;;p=((p+1)%g.size())) {
				if (p==pos && wrap) {
					r--;break;
				}
				if (tk<g[p]) {
					r--;
					pos=p;
					break;
				}
				total+=g[p];
				tk-=g[p];
				wrap=true;
			}
		}
		printf("Case #%d: %lld\n",x,total);
	}
	
}
