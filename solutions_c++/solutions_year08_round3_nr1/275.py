#include <map>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
long long a[1001];
int main(void){
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,n,t;
	int p,k,l;
	scanf("%d", &t);
	for(int out=1; out<=t; out++){
		scanf("%d %d %d", &p, &k, &l);
		for(i=0; i<l; i++) scanf("%lld" ,&a[i]);
		sort(a, a+l);

		long long sum = 0;
		int back = l-1;
		for(i=1; i<=p; i++){
			for(j=1; j<=k; j++){
				sum += a[back] * i;
				back--;
				if(back < 0) break;
			}
			if(back<0)break;
		}
		printf("Case #%d: %lld\n", out, sum);
	}
}