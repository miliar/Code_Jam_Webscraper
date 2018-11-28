#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int t,n;
char g[200][200];

double wp(int x) {
	int all=0,w=0;
	for (int i=0;i<n;i++) if (g[x][i]!='.') {
		all++;
		if (g[x][i]=='1') w++;
	}
	return 1.0*w/all;
}

double owp(int x) {
	double r=0;
	int op=0;
	for (int y=0;y<n;y++) if (g[y][x]!='.') {
		op++;
		int all=0,w=0;
		for (int i=0;i<n;i++) if (i!=x && g[y][i]!='.') {
			all++;
			if (g[y][i]=='1') w++;
		}
		r+=1.0*w/all;
	}
	return r/op;
}

double o[200];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for (int test=1;test<=t;test++) {
    	printf("Case #%d:\n",test);
    	scanf("%d",&n);
    	for (int i=0;i<n;i++) scanf(" %s",g[i]);
    	for (int x=0;x<n;x++) {
    		o[x]=owp(x);
    	}
    	for (int x=0;x<n;x++) {
    		double r=0;
    		r += 0.25 * wp(x);
    		r += 0.50 * o[x];
    		double oowp=0;
    		int p=0;
    		for (int y=0;y<n;y++) if (g[y][x]!='.') {
    			p++;
    			oowp+=o[y];
    		}
    		r += 0.25 * (oowp/p);
    		printf("%.9lf\n",r);
    	}
    }
    return 0;
}
