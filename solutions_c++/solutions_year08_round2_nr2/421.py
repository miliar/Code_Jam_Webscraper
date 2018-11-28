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

int gcd(int a, int b) {
	while(b) {
		a%=b;
		swap(a,b);
	}
	return a;
}

vector<int> prime;
bool ff[1001]={false,};

int foo(int n) {
	int i;
	int ret=0;
	for(i=0;i<prime.size();i++) {
		if(n%prime[i]==0) ret=prime[i];
		else if(n<prime[i]) break;
	}

	return ret;
}

int main() {
	int T,t;
	int A,B,P,n;
	int i,j,k,tmp;
	bool flag;

	for(i=2;i<=1000;i++) {
		if(ff[i]==false) {
			prime.push_back(i);
			for(j=i;j<=1000;j+=i) ff[j]=true;
		}
	}

	cin >> t;
	for(T=1;t--;T++) {
		int vv[1001]={0,};
		cin >> A >> B >> P;

		for(i=A;i<=B;i++) vv[i]=i;
		for(i=A;i<=B;i++) {
			for(j=i+1;j<=B;j++) {
				n = foo(gcd(i,j));
/*
				flag=false;
				for(k=0;k<prime.size();k++) if(prime[k]>=P) break;
				for(;k<prime.size() && i>=prime[k] && j>=prime[k];k++)
					if(i%prime[k]==0 && j%prime[k]==0) { flag=true; break; }
				if(flag && vv[i]!=vv[j]) {
*/
				if(n>=P && vv[i]!=vv[j]) {
					tmp=vv[i];
					for(k=A;k<=B;k++) if(vv[k]==tmp) vv[k]=vv[j];
				}
			}
		}
/*
		for(i=A;i<=B;i++) {
			printf("(%d, %d) ", i,vv[i]);
		}puts("");
*/
		set<int> ss;
		for(i=A;i<=B;i++) ss.insert(vv[i]);
		printf("Case #%d: %d\n", T,ss.size());
	}

	return 0;
}