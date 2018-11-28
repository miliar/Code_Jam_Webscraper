#include<iostream>
#include<cstdio>
#include<vector>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<string>
#include<algorithm>
int a[120];
int l,h;
int main(void){
	freopen("in.in","r",stdin);
	freopen("out.in","w",stdout);
	int t,k,n,ans;
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		printf("Case #%d: ",k);
		scanf("%d%d%d",&n,&l,&h);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(ans=l;ans<=h;ans++){
			int i;
			for(i=0;i<n;i++){
				if(!(a[i]%ans==0||ans%a[i]==0))
					break;
			}
			if(i==n) break;
		}
		if(ans<=h) printf("%d\n",ans);
		else printf("NO\n");
	}
	return 0;
}