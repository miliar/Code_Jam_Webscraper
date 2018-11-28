#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>

using namespace std;

__int64 dd[2005];
__int64 ss[2005];
__int64 cnt[1005],next[1005];

int main(){
	
	int T,cas,n,k,r,i,tmp,J,nn,tim;
	__int64 tt,ans;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++){
		memset(cnt,0,sizeof(cnt));
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%d",&dd[i]);
		nn=n*2;
		for(i=n;i<nn;i++)
			dd[i]=dd[i-n];
			
		for(i=0;i<n;i++){
			tmp=dd[i];
			for(J=i+1;J<i+n;J++){
				if(tmp+dd[J]>k) break;
				tmp+=dd[J];
			}
			if(J==i+n) J++;
			next[i]=J%n;
			ss[i]=tmp;
		}
				
		//for(i=0;i<n;i++)
			//printf("tt; %d %d\n",next[i],ss[i]);
				
		ans=0;
		i=0;
		J=0;
		tim=0;
		while(cnt[i]==0){
			tim++;
			cnt[i]=tim;	
			ans=(__int64)ans+ss[i];
			J=i;			
			i=next[i];	
			//rec[tim]=ans;
			if(tim==r) break;
		}
		if(tim!=r){
			//printf("tt\n");
			//printf("tim: %d, %d ",tim,cnt[i]);
			tt=ans;r-=tim;
			
			if(cnt[i]!=1){
				//printf("kk ");
				//t1=ans;
				memset(cnt,0,sizeof(cnt));
				tim=0;
				tt=0;
				while(cnt[i]==0){
					tim++;
					cnt[i]=tim;	
					tt=(__int64)tt+ss[i];
					J=i;			
					i=next[i];	
					//rec[tim]=tt;
				}
				//ans-=tt;
			}
			tmp=r/tim;
			tt=(__int64)tt*tmp;	
			ans+=tt;
			r-=(tmp*tim);
			
			//ans+=rec[r];
			//i=0;
			//printf("%d ",tim);
			while(r>0){
				
				r--;
				ans=(__int64)ans+ss[i];			
				i=next[i];	
			}
		}
		
		printf("Case #%d: %I64d\n",cas,ans);
	}
}

