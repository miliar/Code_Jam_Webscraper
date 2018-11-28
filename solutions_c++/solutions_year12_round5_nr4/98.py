#include <iostream>
#include <string>
#include <map> 
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>


using namespace std;

#define sqr(x) ((x)*(x))
#define ll long long

int gcd(int a, int b) {
	while (b) b^=a^=b^=a%=b;
	return a;
}

const int maxn=100100;

int k;
string s;
int a[255][255];
int in[255],out[255];


char f(char c) {
	if (c=='o') return '0';
	if (c=='i') return '1';
	if (c=='e') return '3';
	if (c=='a') return '4';
	if (c=='s') return '5';
	if (c=='t') return '7';
	if (c=='b') return '8';
	if (c=='g') return '9';
	return c;
}

void solve(int test) {
	for (int i=0; i<255; i++) for (int j=0; j<255; j++) a[i][j]=0;

	int ans=0,f1=0,f2=0,f3=0;
	cout << "Case #" << test << ": ";
	cin >> k >> s;
	for (int i=0; i<s.length()-1; i++) {
		a[s[i]][s[i+1]]=1;
		a[f(s[i])][s[i+1]]=1;
		a[s[i]][f(s[i+1])]=1;
		a[f(s[i])][f(s[i+1])]=1;
	}
	for (int i=0; i<255; i++) {
		in[i]=out[i]=0;
		for (int j=0; j<255; j++) {
			if (a[i][j]) out[i]++;
			if (a[j][i]) in[i]++;
		}
		ans+=in[i]+out[i]-min(out[i],in[i]);
		if (out[i]>in[i]) f1++;
		if (in[i]>out[i]) f2++;
		if (in[i]==out[i]) f3++;
	}
	if (!f1) ans++;
	if (!f2) ans++;
	if (!f1 && !f2 && f3) ans--;
	cout << ans << endl;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tests;
	cin >> tests;
	for (int test=1; test<=tests; test++) {
		solve(test);
	}


	return 0;
}