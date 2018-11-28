#include<cstdio>
#include<algorithm>
using namespace std;
int d[11111],f[11111],l[11111];
int main(){
	int t,tt,i,j,k,n,dn;
	bool p;
//	freopen("a.in","r",stdin);
//	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++){
		scanf("%d",&n);
		for (i=0;i<n;i++){
			scanf("%d%d",d+i,l+i);
			f[i]=d[i];
		}
		scanf("%d",&k);
		f[0]=0;
		p=false;
		for (i=0;i<n;i++){
			if (d[i]==f[i]) break;
			dn=min(d[i]-f[i],l[i]);
			for (j=upper_bound(d,d+n,dn+d[i])-d-1;f[j]==d[j];j--) f[j]=d[i];
			if (dn+d[i]>=k) {p=true; break;}
		}
		printf("Case #%d: ",tt);
		if (p) puts("YES"); else puts("NO");
	}
}
