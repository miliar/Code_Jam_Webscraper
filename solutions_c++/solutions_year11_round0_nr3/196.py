#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
int n,a[1010];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int i,j,k;
	int t,cas;
	int sum,cur;
	int m,ans;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d",&n);
		sum=0;
		m=0;
		for(i=1;i<=n;i++){
			scanf("%d",&a[i]);
			sum^=a[i];
			m=max(m,a[i]);
		}
		printf("Case #%d: ",cas);
		if(sum!=0){
			printf("NO\n");
			continue;
		}
		sort(a+1,a+n+1);
		sum=0;
		for(i=2;i<=n;i++){
			sum+=a[i];
		}
		printf("%d\n",sum);
	}
	return 0;
}
