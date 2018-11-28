#include<cstdio>
#include<cmath>
#include<algorithm>
#define maxn (1005)
using namespace std;

struct Tnode{
	int l,r,w;
}a[maxn];
int test,Case,N;
double t,res,R,X,S;

bool cmp(Tnode a,Tnode b){
	if (a.w==b.w) return a.r-a.l<b.r-b.l;
	return a.w>b.w;
}
int main(){
	freopen("i.txt","r",stdin);
	for (scanf("%d",&test);test--;){
		printf("Case #%d: ",++Case);
		scanf("%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
		for (int i=1;i<=N;i++) scanf("%d%d%d",&a[i].l,&a[i].r,&a[i].w);
		sort(a+1,a+N+1,cmp);
		double rem=X;
		res=0;
		for (int i=1;i<=N;i++) rem-=(a[i].r-a[i].l);
		if (R*t<=rem){
				rem-=R*t;
				res+=t;
				for (int i=1;i<=N;i++) res+=(double)(a[i].r-a[i].l)/(a[i].w+S);
				res+=rem/S;
				printf("%.10lf\n",res);
		}
		else{
			res+=rem/R;
			t-=res;
			int i;
			for (i=1;i<=N;i++){
				double len=a[i].r-a[i].l;
				if ((R+a[i].w)*t<=len){
					res+=t;
					len-=(R+a[i].w)*t;
					res+=len/(a[i].w+S);
					break;
				}
				else{
					res+=len/(R+a[i].w);
					t-=len/(R+a[i].w);
				}
			}
			for (i++;i<=N;i++) res+=(double)(a[i].r-a[i].l)/(a[i].w+S);
			printf("%.10lf\n",res);
		}
	}
	return 0;
}
