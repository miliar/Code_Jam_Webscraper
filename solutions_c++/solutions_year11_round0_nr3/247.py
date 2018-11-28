#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n,m,test,cur = 1,minnum,xorsum,sum;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		scanf("%d",&n);
		sum = xorsum = 0;
		minnum = 1000000000;
		for ( int i = 0 ; i < n ; i++ ){
			scanf("%d",&m);
			sum += m;
			xorsum ^= m;
			minnum = min(minnum,m);
		}
		printf("Case #%d: ",cur);
		if (xorsum!=0) printf("NO\n"); else printf("%d\n",sum-minnum);
	}
}
