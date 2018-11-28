#include <cstdio>
#include <algorithm>

using namespace std;

int arr[1001];

void newprob(int tt){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	sort(arr,arr+n);
	int ans = 0;
	int sum = 0;
	for(int i=0;i<n;i++){
		ans ^= arr[i];
		sum += arr[i];
	}
	int chk = 0;
	for(int i=0;i<n;i++){
		ans ^= arr[i];
		chk ^= arr[i];
		sum -= arr[i];
		if(ans == chk){
			printf("Case #%d: %d\n",tt,sum);
			return;
		}
	}
	printf("Case #%d: NO\n",tt);
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)newprob(i+1);
	return 0;
}
