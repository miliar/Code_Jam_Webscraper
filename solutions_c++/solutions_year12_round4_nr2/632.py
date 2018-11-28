#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<vector>
using namespace std;

int r[1024],x[1024],y[1024];
inline int sgn(int x){
	return x>0?1:-1;
}
inline void solve(){
	int n,w,l;
	scanf("%d%d%d",&n,&w,&l);
	for(int i=0;i<n;++i){
		scanf("%d",r+i);
		x[i]=(long long)w*rand()/RAND_MAX;
		y[i]=(long long)l*rand()/RAND_MAX;
	}
	for(int i=0;;++i){
		if(i==n){
			for(i=0;i<n;++i)
				for(int j=0;j<i;++j)
					if(abs(x[i]-x[j])<r[i]+r[j] && abs(y[i]-y[j])<r[i]+r[j])i=j=1000000;
			if(i==n)break;
			i=0;
		}
		for(int j=0;j<n;++j)if(i!=j)
		if(abs(x[i]-x[j])<r[i]+r[j] && abs(y[i]-y[j])<r[i]+r[j]){
			if(rand()&1){
				x[j]+=sgn(x[j]-x[i])*(r[i]+r[j]-abs(x[j]-x[i]));
			}else{
				y[j]+=sgn(y[j]-y[i])*(r[i]+r[j]-abs(y[j]-y[i]));
			}
			if(x[j]>w)x[j]=w;
			if(y[j]>l)y[j]=l;
			if(x[j]<0)x[j]=0;
			if(y[j]<0)y[j]=0;
		}
	}
	for(int i=0;i<n;++i)
		printf(" %d %d",x[i],y[i]);
}
int main(){
	int Tc;
	scanf("%d",&Tc);
	srand(time(NULL));
	for(int ti = 1;	ti<= Tc;++ti){
		printf("Case #%d:",ti);
		solve();
		puts("");
	}
	return 0;
}
