#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>
#include <math.h>
using namespace std;

double ans;
struct node{
	double xx,yy,rr;
}dd[10];

double dis(int a,int b){
	return sqrt((dd[a].xx-dd[b].xx)*(dd[a].xx-dd[b].xx)+(dd[a].yy-dd[b].yy)*(dd[a].yy-dd[b].yy));
}

void solve(){
	double tt1,tt2,tt3;
	tt1=(dis(0,1)+dd[0].rr+dd[1].rr)*0.5;
	tt2=(dis(1,2)+dd[2].rr)*0.5;
	tt3=(dis(0,2)+dd[2].rr)*0.5;
	tt2=min(tt2,tt3);
	tt3=dd[2].rr;
	tt2=min(tt2,tt3);
	tt1=max(tt2,tt1);
	ans=min(ans,tt1);
	
	tt1=(dis(0,2)+dd[0].rr+dd[2].rr)*0.5;
	tt2=(dis(2,1)+dd[1].rr)*0.5;
	tt3=(dis(0,1)+dd[1].rr)*0.5;
	tt2=min(tt2,tt3);
	tt3=dd[1].rr;
	tt2=min(tt2,tt3);
	tt1=max(tt2,tt1);
	ans=min(ans,tt1);
	
	tt1=(dis(1,2)+dd[1].rr+dd[2].rr)*0.5;
	tt2=(dis(1,0)+dd[0].rr)*0.5;
	tt3=(dis(2,0)+dd[0].rr)*0.5;
	tt2=min(tt2,tt3);
	tt3=dd[0].rr;
	tt2=min(tt3,tt2);
	tt1=max(tt2,tt1);
	ans=min(ans,tt1);
	
	
}
int main(){
	int i,J,ncase,ii,n;
	double xx,yy,rr;
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	
	scanf("%d",&ncase);
	for(ii=1;ii<=ncase;ii++){
	
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%lf%lf%lf",&dd[i].xx,&dd[i].yy,&dd[i].rr);
			
		}
		ans=99999;
		if(n==1)
			ans=dd[0].rr;
		else
			if(n==2){
				double tt1;
				tt1=max(dd[1].rr,dd[0].rr);
				ans=tt1;
				tt1=(dis(0,1)+dd[0].rr+dd[1].rr)/2;
				ans=min(tt1,ans);
				
			}
		else{
	
			solve();
		}
		
		printf("Case #%d: %lf\n",ii,ans);
		
	}
}
