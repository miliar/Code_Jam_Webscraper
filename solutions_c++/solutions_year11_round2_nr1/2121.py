#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <string.h>

using namespace std;

int T,n;
char m[105][105];

double wp (int t, int x) {
	double w=0;
	int g=0;
	for (int i=0; i<n; i++) {
		if (m[t][i]=='.' || i==x) continue;
		g++;
		if (m[t][i]=='1') w+=1;
	}
	return w/g;
}

double owp (int t, int x) {
	double res=0;
	int g=0;
	for (int i=0; i<n; i++) {
		if (m[t][i]=='.' || i==x) continue;
		g++;
		res+=wp(i,t);
	}
	return res/g;
}

double oowp (int t, int x) {
	double res=0;
	int g=0;
	for (int i=0; i<n; i++) {
		if (m[t][i]=='.' || i==x) continue;
		g++;
		res+=owp(i,i);
	}
	return res/g;
}

int main () {
	freopen ("input","r",stdin);
	freopen ("output","w",stdout);
	scanf ("%d",&T);
	for (int z=0; z<T; z++) {
		scanf ("%d",&n);
		for (int i=0; i<n; i++) {
			scanf ("%s",m[i]);
		}
		for (int i=0; i<n; i++) {
			double rpi=(wp(i,i)*0.25)+(owp(i,i)*0.5)+(oowp(i,i)*0.25);
			if (i==0) printf ("Case #%d:\n",z+1);
			printf ("%.10f\n",rpi);
		}
	}
	return 0;
}