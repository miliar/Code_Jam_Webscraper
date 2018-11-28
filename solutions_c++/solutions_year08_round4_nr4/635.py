#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

#define LL long long

using namespace std;

char str[10000];

int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int t,T;
	scanf("%d", &T);
	int i;
	for (t=1; t<=T; t++) {
		int k;
		int anse=1000000000;
		scanf("%d", &k);
		scanf("%s", str);
		vector<int> ar;
		for (i=0; i<k; i++) {
			ar.push_back(i);
		}
		
		do {
			string g=str;
			int b=0;
			for (i=0; i<g.length(); i++) {
				if (i%k==0) b=i;
				g[i]=str[b+ar[i%k]];
			}
			char last=1;
			int ans=0;
			for (i=0; i<g.length(); i++) {
				if (g[i]==last) continue;
				ans++;
				last=g[i];
			}
			if (ans<anse) 
				anse=ans;
		} while (next_permutation(ar.begin(),ar.end()));
		printf("Case #%d: %d\n",t,anse);
	}
	return 0;
}
