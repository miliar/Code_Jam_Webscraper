#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int tests;
int c,d,n;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
    	fprintf(stderr,"%d\n",test);
    	scanf("%d %d",&c,&d);
    	vector<double> y;
    	n=0;
    	for (int i=0;i<c;i++) {
    		int p,v;
    		scanf("%d %d",&p,&v);
    		n+=v;
    		for (int j=0;j<v;j++) y.push_back(p);
    	}
    	double tm=0, tM=1e13;
    	for (int it=0;it<100;it++) {
    		vector<double> x = y;
    		double t=(tm+tM)/2;
    		x[0]-=t;
    		int ok=1;
    		for (int i=1;i<n;i++) {
    			if (x[i-1]+d<=x[i]) { // move left
					x[i]=max(x[i-1]+d, x[i]-t);
    			} else { // move right
    				if (x[i]+t<x[i-1]+d) {
    					ok=0; break;
    				} else {
    					x[i]=x[i-1]+d;
    				}
    			}
    		}
    		if (ok) tM=t;
    		else tm=t;
    	}
    	printf("Case #%d: %.9lf\n",test,tM);
    }
    return 0;
}
