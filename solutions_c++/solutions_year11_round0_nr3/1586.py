#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
//	freopen("C-small-attempt2.in","r",stdin);
//	freopen("C-small.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		int n, a[1005], sum=0, ans=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",a+i);
			sum ^= a[i];
			ans += a[i];
		}
		if(sum) puts("NO");
		else {
			int mina = 100000000;
			for(int i=0;i<n;i++)
				mina = min(mina,a[i]);
			printf("%d\n",ans-mina);
		}
	}
}
