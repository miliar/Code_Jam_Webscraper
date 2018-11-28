#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;

typedef long long i64;

bool solve() {
	i64 N; int PD,PG;
	cin>>N>>PD>>PG;
	if(PD!=0&&PD!=100) {
		int gcd=__gcd(100,PD);
		if(100/gcd>N)return false;
	}
	if(PG==0) {
		if(PD!=0)return false;
	} else if(PG==100) {
		if(PD!=100)return false;
	}
	return true;
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		printf("Case #%d: %s\n",S,(solve()?"Possible":"Broken"));
	}
	return 0;
}
