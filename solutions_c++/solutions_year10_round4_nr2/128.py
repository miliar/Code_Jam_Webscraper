#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

int T;
int ans,n,m,p,mm,F[6666][22],a[6666],cost[6666];

int rec(int X,int taken){
	if(X>m){
		if(taken>=p-a[X-m-1])  return 0;
		return (int)1e9;
	}
	if(F[X][taken]!=-1) return F[X][taken];
	int x,y;
	x=std::min(rec(X+X,taken),rec(X+X,taken+1)+cost[X+X]);
	if(x>=1e9) return (int)1e9;
	y=std::min(rec(X+X+1,taken),rec(X+X+1,taken+1)+cost[X+X+1]);
	if(y>=1e9) return (int)1e9;
	return F[X][taken]=x+y;
}


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		memset(cost,63,sizeof(cost));
		memset(F,-1,sizeof(F));
		scanf("%d",&p);
		n=1<<p;
		for(int i=n-1;i>=0;i--) scanf("%d",&a[i]);
		m=(1<<p)-1;
		mm=m;
		for(int i=0;i<p;i++)
			for(int j=0;j<(1<<(p-i-1));j++){
				scanf("%d",&cost[mm--]);
			}
		ans=std::min(rec(1,0),rec(1,1)+cost[1]);
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
