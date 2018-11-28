#include<stdio.h>
#include<stdlib.h>

using namespace std;

int a[1005];

void get_ans(int nt){
	int n;
	scanf("%d",&n);
	int sumx = 0;
	long long sum = 0;
	for(int i = 0; i < n; i++){
		scanf("%d",&a[i]);
		sumx = sumx xor a[i];
		sum = sum + a[i];
	}
	if (sumx != 0){
		printf("Case #%d: NO\n",nt);
		return;
	}
	int min = a[0];
	for(int i = 1; i < n; i++){
		if (a[i] < min) min = a[i];
	}
	printf("Case #%d: %d\n",nt,sum - min);
	return;
}

int main(){
      freopen("C-large.in","r",stdin);
      freopen("C-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int k = 1; k <= t; k++){
		get_ans(k);
	}
	return 0;
}            
