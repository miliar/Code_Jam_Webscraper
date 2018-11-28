#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#define maxn (25)
#define eps (1e-10)
using namespace std;

struct Tnode{
	int p,v;
}a[maxn];

int D,m,N,test,Case;

int calcdist(int t){
	int i;
	for (i=1;a[i].v<t;t-=a[i++].v);
	return a[i].p;
}
bool can(double t){
	double now=a[1].p-t;
	for (int i=1;i<=m;i++){
		int p=calcdist(i);
		double l=p-t,r=p+t;
		if (r<now) return false;
		if (now<l) now=l;
		now+=D;
	}
	return true;
}
int main(){
	freopen("i.txt","r",stdin);
	for (scanf("%d",&test);test--;){
		printf("Case #%d: ",++Case);
		scanf("%d%d",&N,&D);
		for (int i=1;i<=N;i++) scanf("%d%d",&a[i].p,&a[i].v);
		m=0;
		for (int i=1;i<=N;i++) m+=a[i].v;
		double l=0,r=1000000000;
		for (;r-l>eps;){
			double m=(l+r)/2;
			if (can(m)) r=m;
				else l=m;
		}
		printf("%.10lf\n",l);
	}
	return 0;
}
