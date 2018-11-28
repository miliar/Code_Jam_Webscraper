#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *inf=fopen("C-small.in","r"),*ouf=fopen("C-small.out","w");
int t,r,k,n,g[1005],nxt[1005],j,now,zn=0,jj,l;
long long ms[1005],ans,mans;

main(){
	int i;
	fscanf(inf,"%d",&t);
	while(t--){
		fscanf(inf,"%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			fscanf(inf,"%d",g+i);
		now=ans=0;
		memset(nxt,-1,sizeof(long long)*n);
		for(i=0;i<r;i++){
			jj=(now+n-1)%n;
			for(j=now,l=mans=0;mans+g[j]<=k&&l<n;j=(j+1)%n,l++)mans+=g[j];
			now=j;
			ans+=mans;
		}
		fprintf(ouf,"Case #%d: %d\n",++zn,ans);
	}
}
