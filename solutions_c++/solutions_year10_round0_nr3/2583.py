#include <iostream>

using namespace std;

long long next[1001];
long long size[1001];
long long cnt[1001];

int main(){
	int ts;
	long long r, k, n;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&ts);

	for(int t=1;t<=ts;t++){
		long long ans = 0;
		scanf("%lld %lld %lld", &r, &k, &n);
		
		for(int i=0;i<n;i++){
			scanf("%lld",size+i);
		}

		for(int i=0;i<n;i++){
			long long sum = size[i];
			int j;
			for(j=(i+1)%n;j!=i;j=(j+1)%n){
				if(sum + size[j] > k)
					break;
				sum += size[j];
			}
			if(i == j){
				next[i] = (i+n-1)%n;
				cnt[i] = sum;
			}else{
				next[i] = j;
				cnt[i] = sum;
			}
		}
		int cur = 0;
		for(int i=0;i<r;i++){
			ans += cnt[cur];
			cur = next[cur];
		}

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}