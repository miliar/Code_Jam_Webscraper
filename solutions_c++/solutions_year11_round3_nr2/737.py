#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
int c[1005];
int a[1005];
int sum[1005];
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int cas,r=1;scanf("%d",&cas);
	int l,n,m;
	long long t;
	while(cas--){
		//scanf("%d%d%d%d",&l,&t,&n,&m);
		cin>>l>>t>>n>>m;
		for(int i=0; i<m; i++){
			scanf("%d",&a[i]);
		}
		int res=0;
		sum[0]=0;
		for(int i=0; i<n; i++){
			c[i]=a[i%m]*2;
			res+=c[i];
			sum[i+1]=sum[i]+c[i];
		}
		//for(int i=0; i<n; i++) printf("%d ",c[i]);
		printf("Case #%d: ",r++);
		
		if(t>10000000) {printf("%d\n",res); continue;}
		int tt=(int)(t);
		if(l==1){
			int mx=0;
			for(int i=0; i<n; i++){
				if(sum[i+1]<=tt) continue;
				if(sum[i]<=tt && sum[i+1]>tt) {
	                mx=max(mx, (sum[i+1]-tt)/2);
				}else mx=max(mx, c[i]/2);
			}
			res-=mx;
		}else if(l==2){
			int mx=0;
			for(int i=0; i<n; i++){
				for(int j=i+1; j<n; j++){
					int ad;
					if(sum[i+1]<=tt) continue;
					if(sum[i]<=tt && sum[i+1]>tt) {
	                	ad=(sum[i+1]-tt);
					}else ad=c[i];
					
					if(sum[j+1]<=tt) continue;
					if(sum[j]<=tt && sum[j+1]>tt) {
	                	ad+=(sum[j+1]-tt);
					}else ad+=c[j];
					
					ad/=2;
					mx=max(mx, ad);
				}
			}
			res-=mx;
		}
		printf("%d\n",res);
	}
}
