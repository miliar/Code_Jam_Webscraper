#include<cstdio>
#include<cstring>

const int N = 2001;
int ret[N];

int data[N];

void find(int left, int right){
	if(left == right) return;
	int pre = left;
	for(int i = left;i < right;i++){
		if(data[i] == right){
			if(data[right] == -1){
				ret[i] = ret[right] - 1;
			}else{
				int temp = ret[data[right]] - ret[right];
				ret[i] = ret[right] - (long long)temp * (right - i) / (data[right] - right) - 2;
			}
			find(pre, i);
			pre = i + 1;
		}
	}
}

int main(){
	freopen("C-small-attempt3.in" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int ii = 0;
	while(t--){
		int n;
		scanf("%d" , &n);
		for(int i = 1;i < n;i++){
			scanf("%d" , &data[i]);
		}
		ret[n] = 1000000000;
		data[n] = -1;
		find(1, n);
		int i, j;
		for(i = 1;i <= n;i++){
			if(data[i] == -1) continue;
			for(j = i + 1;j <= n;j++){
				int x = data[i];
				if(j < x && (long long)(ret[x] - ret[i]) * (j - i) == (long long)(ret[j] - ret[i]) * (x - i)) break;
				if((long long)(ret[x] - ret[i]) * (j - i)  < (long long)(ret[j] - ret[i]) * (x - i)) break;
			}
			if(j <= n) break;
		}
		printf("Case #%d: ", ++ii);
		if(i <= n){
			printf("Impossible");
		}else{
			for(i = 1;i <= n;i++){
				if(i == n) printf("%d" , ret[i]);
				else printf("%d " , ret[i]);
			}
		}
		printf("\n");
	}
	return 0;
}