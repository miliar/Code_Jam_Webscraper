#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

int task, T=0, A1, A2, B1, B2;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("a.out","w",stdout);
	for (scanf("%d", &task); task--;){
		scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
		long long ret = 0;
		for (int i = A1; i <= A2; i++){
			int x = (int)ceil(i/((1+sqrt(5.0))*0.5)), 
				y = (int)(i*((1+sqrt(5.0))*0.5));
			if ( B2 < x || y < B1 ) 
				ret += B2-B1+1;else{
				ret += max(0, x-B1);
				ret += max(0, B2-y);
			}
		}
		printf("Case #%d: %I64d\n", ++T, ret);
	}
	return 0;
}
