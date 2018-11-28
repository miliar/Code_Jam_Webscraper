#include<stdio.h>
#include<memory.h>
/*
google code jam 2010
B World Cup 2010
*/
#define P 10
#define P2 (((long)1)<<(P))
#define M 0x3fffffff
long dp[P2][P];
//dp[ticket][already get]=min cost
long nomiss[P2],ticket[P2];
long parent[P2],left[P2],right[P2],pleft[P2],pright[P2];
long np,vp;
long solve(long pnow,long got){
	if(dp[pnow][got]!=-1)return dp[pnow][got];
	long i,mx=0;
	long vl=left[pnow],vr=right[pnow];
	for(i=vl;i<=vr;i++){
		if(nomiss[i]>mx)mx=nomiss[i];
	}
	if(mx<=got)return dp[pnow][got]=0;
	if(vl+1==vr){
		if(mx==got+1)return dp[pnow][got]=ticket[pnow];
		else return dp[pnow][got]=M;
	}
	long cost=ticket[pnow],ret1,ret2;
	long cl=solve(pleft[pnow],got),cr=solve(pright[pnow],got);
	if(cl>=M||cr>=M)ret1=M;
	else ret1=cl+cr;
	cl=solve(pleft[pnow],got+1);
	cr=solve(pright[pnow],got+1);
	if(cl>=M||cr>=M)ret2=M;
	else ret2=cl+cr+cost;
	return dp[pnow][got]=(ret1<ret2?ret1:ret2);
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	long z,zi;
	scanf("%ld",&z);
	for(zi=1;zi<=z;zi++){
		scanf("%ld",&np);
		vp=((long)1)<<np;
		long i;
		for(i=0;i<vp;i++){
			long nm;
			scanf("%ld",&nm);
			nomiss[i]=np-nm;
		}
		memset(dp,-1,sizeof(dp));
		memset(pleft,-1,sizeof(pleft));
		memset(pright,-1,sizeof(pright));
		long ip=vp>>1,iv=2,pticket=0;
		while(ip){
			long pstart=pticket;
			for(i=0;i<ip;i++){
				scanf("%ld",ticket+pticket);
				parent[pticket]=pstart+ip+(i>>1);
				if(i&1){
					pright[pstart+ip+(i>>1)]=pticket;
				}else{
					pleft[pstart+ip+(i>>1)]=pticket;
				}
				left[pticket]=i*iv;
				right[pticket]=(i+1)*iv-1;
				pticket++;
			}
			ip>>=1;
			iv<<=1;
		}
		printf("Case #%ld: %ld\n",zi,solve(pticket-1,0));
	}
	return 0;
}
