#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;
long long a[100001],b[100001];
int main(void){
	int i,j,k,l,m,n,t;
	long long v;
	scanf("%d", &t);
	for(int out=1; out<=t; out++){		
		v = 0;
		scanf("%d", &n);
		for(i=0; i<n; i++) scanf("%lld", &a[i]);
		for(i=0; i<n; i++) scanf("%lld", &b[i]);
		sort(a, a+n);
		sort(b, b+n);
		for(i=0; i<n; i++)
			v += a[i] * b[n-i-1];
		printf("Case #%d: ",out);
		cout << v << endl;
	}
}
