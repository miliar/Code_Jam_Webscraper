#include <stdio.h>
#include <algorithm>

int d[10001],l[10001];
int dis[10001];
int que[1<<20];
int L[10001],R[10001];
int inq[10001];

#define M ((1<<20)-1)

int main(){
    int tt,TT,n,i,j,D,p,q,x,flag,dd;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ){
	scanf("%d",&n);
	for( i=1; i<=n; i++ ){
	    scanf("%d %d",&d[i],&l[i]);
	}
	scanf("%d",&D);
	for( i=1; i<=n; i++ ){
	    dis[i]=0;
	    L[i]=i-1; R[i]=i+1;
	    inq[i]=0;
	}
	dis[1]=d[1];
	p=0; q=-1; que[0]=1;
	inq[0]=1;
	flag=0;
	while(p!=q){
	    q=(q+1)&M;
	    x=que[q];
	    inq[x]=0;
	    if(d[x]+dis[x]>=D){
		flag=1;
		break;
	    }
	    for( i=R[x]; i<=n && (dd=d[i]-d[x])<=dis[x]; i++ ){
		if(dd>l[i]) dd=l[i];
		if(dd>dis[i]){
		    dis[i]=dd;
		    if(!inq[i]){
			inq[i]=1;
			p=(p+1)&M;
			que[p]=i;
		    }
		}
	    }
	    R[x]=i;
	    for( i=L[x]; i>0 && (dd=d[x]-d[i])<=dis[x]; i-- ){
		if(dd>l[i]) dd=l[i];
		if(dd>dis[i]){
		    dis[i]=dd;
		    if(!inq[i]){
			inq[i]=1;
			p=(p+1)&M;
			que[p]=i;
		    }
		}
	    }
	    L[x]=i;
	}
	printf("Case #%d: %s\n",tt+1,flag?"YES":"NO");
    }
    return 0;
}
