#include <stdio.h>

int main() {
	int N;
	scanf("%d",&N);
	for(int N__=1;N__<=N;N__++) {
		int n;
		scanf("%d",&n);
		int a[1000];
		int sum=0;
		for(int i=0;i<n;i++) {
			scanf("%d",a+i);
			sum+=a[i];
		}

		int result;
		int temp=0;
		for(int i=0;i<n;i++)
			temp^=a[i];
		if(temp) {
			printf("Case #%d: NO\n",N__);
		}
		else {
			result=2e9;
			for(int i=0;i<n;i++)
				result=a[i]<result?a[i]:result;
			printf("Case #%d: %d\n",N__,sum-result);
		}
	}
	return 0;
}
