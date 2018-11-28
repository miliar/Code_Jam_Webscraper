#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	int n;
	scanf("%d",&n);
	for(int w = 0; w < n; w++){
		int k;
		scanf("%d",&k);
		int array[k];
		for(int i = 0; i < k; i++){
			scanf("%d",&array[i]);
		}
		int notPossible = 0;
		for(int i = 0; i < k; i++){
			notPossible ^= array[i];
		}
		if(!notPossible){
			int mini = 0x3f3f3f3f;
			long long sum = 0;
			for(int i = 0; i < k; i++){
				sum+= array[i];
				mini = min(mini,array[i]);
			}
			sum -= mini;
			printf("Case #%d: %lld\n",w+1,sum);
		}else{
			printf("Case #%d: NO\n",w+1);
		}
	}
}
