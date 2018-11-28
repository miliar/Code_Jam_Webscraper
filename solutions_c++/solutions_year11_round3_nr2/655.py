#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int a[1000006];

int make(){
	int l,n,c,t;
	scanf("%d%d%d%d",&l,&t,&n,&c);
	for(int i = 0; i < c; i++){
		scanf("%d",&a[i]);
		a[i] = a[i] * 2;
	}
	for(int i = c; i < n; i++){
		a[i] = a[i % c];
	}
	int ans = 0;
	int j = 0;
	while ((t - ans >= a[j])&&(j < n)){
		ans = ans + a[j];
		j++;
	}
	if ((t - ans > 0) && (j < n)){
		a[j] = a[j] - (t - ans);
		ans = t;
	}
	sort(a + j, a + n);
	for(int i = j; i < n - l; i++){
		
		ans = ans + a[i];
	}
	for(int i = n - l; i < n; i++){
		ans = ans + a[i] / 2;
	}
	return ans;
}


int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int q = 0; q < t; q++){
		printf("Case #%d: %d\n",q + 1,make());
	}
	return 0;
}
