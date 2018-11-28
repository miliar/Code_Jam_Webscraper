#include <cstdio>
#include <algorithm>
using namespace std;
int TC,ok,AC,cnt[30],n,a[1005];
int main(){
	scanf("%d",&TC);
	for (int T=1;T<=TC;T++){
		
		scanf("%d",&n);
		memset(cnt,0,sizeof(cnt));
		ok=1;
		AC=0;
		
		for (int i=1;i<=n;i++){
			scanf("%d",&a[i]);
			for (int j=0;j<25;j++)
				if (a[i] & (1<<j)) cnt[j]++;
			AC+=a[i];
		}
		sort(a+1,a+1+n);
		for (int i=0;i<25;i++)
			if (cnt[i]%2==1) ok=0;
		
		if (!ok) printf("Case #%d: NO\n",T);
		else printf("Case #%d: %d\n",T,AC-a[1]);
	}
	//scanf("\n");
	return 0;
}
