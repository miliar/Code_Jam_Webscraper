#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>

using namespace std;

int gcd(int a,int b){
	int r;
	while(b>0){
		r=a;
		a=b;
		b=r%b;
	}
	return a;		
}
int dd[3];

int main(){
	
	int T,cas,n,i,tt;
	__int64 ans; 
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	/*
	int a,b;
	while(scanf("%d%d",&a,&b)!=EOF){
		printf("%d\n",gcd(a,b));
	}
	*/
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++){

		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&dd[i]);
		sort(dd,dd+n);
		if(n==3){
			tt=gcd(dd[2]-dd[1],dd[1]-dd[0]);
		}
		else
			tt=dd[1]-dd[0];
		
		
		//printf("%d ",tt);	
		if(tt>dd[0])
			ans=tt-dd[0];
		else{
			if(tt==1||tt==dd[0])
				ans=0;
			else{
				__int64 lef=2,rig,mid;
				rig=(__int64)tt*dd[0];
				rig/=(__int64)gcd(tt,dd[0]);
				rig/=tt;
				while(lef<=rig){
					mid=(lef+rig)>>1;
					if(mid*tt>=dd[0]){
						ans=mid;
						rig=mid-1;
					}
					else
						lef=mid+1;
				}
				ans*=tt;
				ans-=dd[0];
			}
		}
		printf("Case #%d: %I64d\n",cas,ans);
	}
}

/*
3
3 26000000 11000000 6000000
3 1 10 11
*/
