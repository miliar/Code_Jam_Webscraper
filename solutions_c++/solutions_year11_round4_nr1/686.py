#include<cstdio>
#include<algorithm>
using namespace std;
struct node {
	int l,r,w;
}a[2010];

bool cmp(node a,node b){
	return a.w<b.w;
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++){
		int m,x,y,n,len=0;
		double t;
		double ans=0;
		scanf("%d%d%d%lf%d",&m,&x,&y,&t,&n);
		int last=0;
		for (int i=1;i<=n;i++){
			int l,r,w;
			scanf("%d%d%d",&l,&r,&w);
			len++;
			a[len].l=last;a[len].r=l;a[len].w=0;
			len++;
			a[len].l=l;a[len].r=r;a[len].w=w;
			last=r;
		}
		len++;
		a[len].l=last;a[len].r=m;a[len].w=0;
		sort(a+1,a+len+1,cmp);
		for (int i=1;i<=len;i++){
			int l=a[i].l,r=a[i].r,w=a[i].w;
			if (double(r-l)/(w+y)<=t){
				t-=double(r-l)/(w+y);
				ans+=double(r-l)/(w+y);
			}else {
				ans+=t+(r-l-t*(w+y))/(w+x);
				t=0;
			}
		}
		printf("Case #%d: %lf\n",TT,ans);
	}
	return 0;
}
