#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
struct node{
	int r;
	int id;
	bool operator <(const node &nd)const{
		return r>nd.r;
	}
};


int x[2000],y[2000],ref[2000];
node nd[2000];
int main(){
	int i,j,k,m,n,c,r,w,l,rr;
	bool f,ff;
	freopen("B-large.in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&rr);
//	printf("%d\n",r);
	for(c=1;c<=rr;++c){
		scanf("%d%d%d",&n,&w,&l);
		ff=false;
		f=false;
		if(l>w){
			swap(w,l);
			f=true;
		}
		for(i=0;i<n;++i){
			scanf("%d",&nd[i].r);
			nd[i].id=i;
		}
//		sort(a,a+n);
		sort(nd,nd+n);
		for(i=0;i<n;++i)	ref[nd[i].id]=i;
//		w+=a[n-1];
		x[0]=y[0]=0;
		r=nd[0].r;
		for(i=1;i<n;++i){
			if(y[i-1]+nd[i-1].r+nd[i].r<=l){
				y[i]=y[i-1]+nd[i-1].r+nd[i].r;
				x[i]=x[i-1];
			}
			else{
				y[i]=0;
				x[i]=x[i-1]+r+nd[i].r;
				r=nd[i].r;
			}
			if(x[i]>w)	ff=true;
		}
		if(f){
			for(i=0;i<n;++i)	swap(x[i],y[i]);
		}
		printf("Case #%d:",c);
//		if(ff){
//			puts("ERR");
//			continue;
//		}
		for(i=0;i<n;++i)	printf(" %d %d",x[ref[i]],y[ref[i]]);
		printf("\n");
//		printf("%d %d",r,c);
	}
	
}
