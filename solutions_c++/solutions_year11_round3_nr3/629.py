#include<stdio.h>
#include<stdlib.h>

int a[105];

int make(){
	int l,n,r;
	scanf("%d%d%d",&n,&l,&r);
	for(int i = 0; i < n; i++){
		scanf("%d",&a[i]);
	}

	for(int ans = l; ans <= r; ans++){
		int qq = 0;
		for(int i = 0; i < n; i++){
			if ((a[i] % ans == 0) || (ans % a[i] == 0))
				qq++;
		}
		if (qq == n)
			return ans;
	}
	return -1;
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int q = 0; q < t; q++){
		int ans = make();
		if (ans == -1)
			printf("Case #%d: NO\n",q + 1);
		else
			printf("Case #%d: %d\n",q + 1, ans);
	}
	return 0;
}
