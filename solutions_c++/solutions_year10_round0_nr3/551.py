#include<stdio.h>
/*
google code jam 2010
qualification
C Theme Park
*/
typedef long long I;
#define N 1010
#define R "%I64d"
I gi[N*2];
I next[N*2],val[N*2];
I sol(I&start,I cap,I group){
	I lo=start,hi=start+group-1;
	I ret;
	while(hi>=lo){
		I mid=(lo+hi)/2;
		if(gi[mid]-gi[start-1]>cap)hi=mid-1;
		else lo=mid+1;
	}
	if(lo>=start+group||gi[lo]-gi[start-1]>cap)lo--;
	ret=gi[lo]-gi[start-1];
	lo++;
	if(lo>group)lo-=group;
	start=lo;
	return ret;
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large2.out","w",stdout);
	long z,zi=1;
	scanf("%ld",&z);
	while(z--){
		I round,cap,group,group2,last,ans;
		long i;
		scanf(R R R,&round,&cap,&group);
		for(i=0;i<group;i++){
			scanf(R,gi+i);
			gi[i+group]=gi[i];
		}
		group2=group*2;
		for(i=1;i<group2;i++)gi[i]+=gi[i-1];
		for(i=1;i<=group;i++){
			last=i;
			val[i]=sol(last,cap,group);
			next[i]=last;
		}
		last=group;
		ans=0;
		for(i=0;i<round;i++){
			ans+=val[last];
			last=next[last];
		}
		printf("Case #%ld: "R"\n",zi++,ans);
		fflush(stdout);
	}
	return 0;
}
