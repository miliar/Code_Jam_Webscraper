#include <cstdio>
#include <iostream>
using namespace std;

long long d;
int pd,pg,t;

void getout(int i,int k) {
	printf("Case #%d: ",i);
	if (k==0) {
		printf("Broken\n");
	} else {
		printf("Possible\n");
	}
}

int gcd(int a,int b) {
	return (b==0)?(a):(gcd(b,a%b));
}

int main() {
	cin>>t;
	for (int i=1;i<=t;i++) {
		cin>>d>>pd>>pg;
		if (pg==100) {
			if (pd<100) getout(i,0); else getout(i,1);
			continue;
		}
		if (pg==0) {
			if (pd>0) getout(i,0); else getout(i,1);
			continue;
		}
		int a=100/gcd(100,pd);
		if (a>d) getout(i,0); else getout(i,1);
	}
}