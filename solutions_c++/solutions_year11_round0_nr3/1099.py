#include<cstdio>
#include<algorithm>
using namespace std;

int t, n, minn, sum, ksor,x;

int main(){
	scanf("%d",&t);
	for(int i=1; i<=t; i++){
		scanf("%d",&n);
		minn=1000000007;
		sum=0;
		ksor=0;
		while(n--){
			scanf("%d",&x);
			sum+=x;
			minn=min(minn,x);
			ksor^=x;
		}
		if(ksor) printf("Case #%d: NO\n",i);
		else printf("Case #%d: %d\n",i,sum-minn);

	}
}

