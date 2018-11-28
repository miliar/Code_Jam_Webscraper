#include <stdio.h>
#include <string.h>
#include <math.h>

const int maxn = 1010;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i = 1 ; i<=t ; i++){
		int n;
		int c[maxn];
		scanf("%d",&n);
		for (int j = 0 ; j<n ; j++){
			scanf("%d",&c[j]);
		}
		int res = 0;
		for (int j = 1 ; j < (1<<n) ; j++){
			int teksum = 0, tekw1 = 0, tekw2 = 0;
			for (int k = 0 ; k<n ; k++){
				if (j & (1<<k)){
					teksum += c[k];
					tekw1 ^= c[k];
				} else{
					tekw2 ^= c[k];
				}
			}
			if (tekw1!=0 && tekw1 == tekw2 && teksum > res){
				res = teksum;
			}
		}
		if (res == 0){
			printf("Case #%d: NO\n",i);	
		} else{
			printf("Case #%d: %d\n", i,res);
		}
	}
	return 0;
}