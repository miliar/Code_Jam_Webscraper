#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
struct node{
	int x,y;
}a[10005];
bool cmp(node aa,node bb){
	 return aa.x<bb.x;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int jishu=0;
	int t;
	scanf("%d",&t);
	int n;
	int i,j;
	while(t--){
		jishu++;
		scanf("%d",&n);
		for(i=1;i<=n;i++) scanf("%d%d",&a[i].x,&a[i].y);
		sort(a+1,a+1+n,cmp);
		int ans=0;
		for(i=1;i<=n;i++){
			for(j=i+1;j<=n;j++)
				if(a[i].y>a[j].y) ans++;
		}
		printf("Case #%d: %d\n",jishu,ans);
	}

	return 0;
}