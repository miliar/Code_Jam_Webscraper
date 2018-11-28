#include<iostream>
#include<cstdio>
#include<string>
#include<map>
#include<cstring>
using namespace std;

int main(void){
	freopen("C:\\a.in","r",stdin);
	freopen("C:\\a.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	int ttt;
	for(ttt=1;ttt<=cs;ttt++){
		int n,k,b,t;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		int i,x[52];
		for(i=1;i<=n;i++){
			scanf("%d",&x[i]);
		}
		int v[52];
		for(i=1;i<=n;i++){
			scanf("%d",v+i);
		}
		int ok=0,ans=0,tt=0;
		for(i=n;i>=1;i--){
			int d=b-x[i];
			if(v[i]*t>=d) {
				ans+=tt;
				++ok;
			}
			else {
				++tt;
			}
			if(ok>=k) break;
		}
		if(ok>=k) {
			printf("Case #%d: %d\n",ttt,ans);
		}
		else printf("Case #%d: IMPOSSIBLE\n",ttt);
	}
	return 0;
}