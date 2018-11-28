#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int candy[16];
int T, n, i, j, k, tmp1, tmp2, cs, res;

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for(cs=1; cs<=T; cs++){
		scanf("%d", &n);
		for(i=0; i<n; i++)
			scanf("%d", &candy[i]);
		sort(candy, candy+n);
		res=-1;
		for(i=1; i<(1<<n); i++){
			tmp1=tmp2=0;
			k=i;
			for(j=0; j<n; j++){
				if(k&1)tmp1^=candy[j];
				else tmp2^=candy[j];
				k>>=1;
			}
			if(tmp1==tmp2){
				tmp1=tmp2=0;
				k=i;
				for(j=0; j<n; j++){
					if(k&1)tmp1+=candy[j];
					else tmp2+=candy[j];
					k>>=1;
				}	
				if(res<max(tmp1, tmp2)){res=max(tmp1, tmp2); break;}
			}
		}
		printf("Case #%d: ", cs);
		if(res==-1)puts("NO");
		else printf("%d\n", res);
	}

	return 0;
}