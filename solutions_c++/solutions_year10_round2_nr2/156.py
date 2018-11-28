#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
using namespace std;

int x[50];
int v[50];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tests;
    scanf("%d",&tests);
    for (int ti=1;ti<=tests;ti++) {
		int r=0;
		int n,k,b,t;
		scanf("%d %d %d %d",&n,&k,&b,&t);
		for (int i=0;i<n;i++) scanf("%d",&x[i]);
		for (int i=0;i<n;i++) scanf("%d",&v[i]);

		vector<int> slow,fast;
		for (int i=0;i<n;i++) {
			if (b-x[i] <= t*v[i]) fast.push_back(i);
			else slow.push_back(i);
		}

		if (fast.size()<k) r=-1;
		else {
			vector<int> overs;
			for (int i=0;i<fast.size();i++) {
				int idf=fast[i];
				int over=0;
				for (int j=0;j<slow.size();j++) {
					int ids=slow[j];
					if (x[idf]<x[ids]) over++;
				}
				overs.push_back(over);
			}
			sort(overs.begin(),overs.end());
			for (int i=0;i<k;i++) {
				r+=overs[i];
			}
		}
		printf("Case #%d: ",ti);
		if (r==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",r);
    }
    return 0;
}
