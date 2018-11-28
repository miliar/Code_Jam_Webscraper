#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
int n,a[1010];
int t,cas;
struct Nodes{
	int id,val;
}p[1010];
bool cmp(Nodes aa,Nodes bb)
{
	return aa.val<bb.val;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D.out","w",stdout);
	int i,j,k;
	int ans;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf("%d",&p[i].val);
			p[i].id=i;
		}
		sort(p+1,p+n+1,cmp);
		ans=0;
		for(i=1;i<=n;i++){
			if(i!=p[i].id)ans++;
		}
		printf("Case #%d: ",cas);
		printf("%d.000000\n",ans);
	}
	return 0;
}
