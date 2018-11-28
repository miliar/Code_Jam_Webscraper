#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;

int T,s,r,x,n;
double t;
int b[2000],e[2000],w[2000];
double cu[300],du[300];

int main(){
	int h,i,j,k;
	scanf("%d",&T);
	double ans;
	for(h=1;h<=T;h++){
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		memset(cu,0,sizeof(cu));
		memset(du,0,sizeof(du));
		memset(b,0,sizeof(b));
		memset(e,0,sizeof(e));
		memset(w,0,sizeof(w));
		for(i=0;i<n;i++){
			scanf("%d%d%d",&b[i],&e[i],&w[i]);
		}
		j=0;
		for(i=0;i<x;i++){
			if(e[j]==i)j++;
			if(b[j]<=i && e[j]>i){
				cu[s+w[j]]++;
			}else{
				cu[s]++;
			}
		}
		ans=0;
		for(i=1;i<300;i++){
			if(cu[i]>=t*(i+r-s)){
				cu[i]-=t*(i+r-s);
				du[i+r-s]+=t*(i+r-s);
				t=0;
			}else{
				du[i+r-s]+=cu[i];
				t-=cu[i]/(i+r-s);
				cu[i]=0;
			}
			ans+=(cu[i]+du[i])/(i+0.0);
		}
		printf("Case #%d: %.8lf\n",h,ans);
	}
	return 0;
}
