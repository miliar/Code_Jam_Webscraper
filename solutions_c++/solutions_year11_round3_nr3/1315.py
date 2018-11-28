#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int a[10010];
int ch(int a,int b){
	while(1){
		if(a > b)
			a -=b;
		else if(a < b)
			b -= a;
		else
			return a;
	}
}
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int i,j;
	int T;
	int n,l,h;
	scanf("%d",&T);
	int ans;
	int tmp;
	int tn,tk;
	int cas = 1;
	while(T --){
		scanf("%d%d%d",&n,&l,&h);
		for(i = 0; i<n; i ++){
			scanf("%d",&a[i]);
		}
		for(ans = l; ans <= h; ans++){
			for(j = 0; j < n; j ++){
				if(ans % a[j] == 0 || a[j] % ans == 0)
					continue;
				else
					break;
			}
			if(j >= n){
				break;
			}		
		}
		printf("Case #%d: ",cas++);
		if(ans > h){
			printf("NO\n");
		}else{
			printf("%d\n",ans);
		}
	}
	return 0;
}