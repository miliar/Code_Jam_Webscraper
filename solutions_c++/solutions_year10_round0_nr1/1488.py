#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int n, k, task=0, T;
long long ret[50];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	ret[1] = 1;
	for (int i=2; i<=30; i++)
		ret[i] = ret[i-1]*2+1;
	for( scanf("%d", &T); T--; ){
		scanf("%d%d", &n, &k);
		if ( k!=0 && k%(ret[n]+1)==ret[n] )
			printf("Case #%d: ON\n", ++task);else
			printf("Case #%d: OFF\n", ++task);
	}
	return 0;
}
