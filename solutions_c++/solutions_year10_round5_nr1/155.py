#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<stdlib.h>

int T;
int d,k,s,a[21111],b[21111],an,pow[21111],f[211111],found,good,p,potans,diff,bb,max;


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	for(int i=2;i<=20000;i++) if(!f[i]){
		a[an++]=i;
		for(int j=i+i;j<=20000;j+=i) f[j]=1;
	}
	pow[0]=1;
	for(int i=1;i<=6;i++) pow[i]=pow[i-1]*10;

	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d",&d,&k);
		if(k==1) found=2;else	found=0;
		max=0;
		for(int i=0;i<k;i++){
			scanf("%d",&b[i]);
			max>?=b[i];
		}
		for(int i=0;i<an && found<2;i++) if(a[i]>max && a[i]<pow[d]){
			p=a[i];
			for(int aa=0;aa<p && found<2;aa++){
				s=b[0];
				good=1;
				for(int j=1;j<k;j++){
					diff=b[j]-((long long)aa*s)%p;
					s=b[j];
					if(diff<0)
						if((-diff)%p==0) diff=0;else
						diff=p-((-diff)%p);
					else
						diff%=p;
					if(j==1) bb=diff;else if(diff!=bb){
						good=0;
						break;
					}
				}
				if(good)
				if(found && potans!=((long long)aa*b[k-1]+bb)%p){
					found=2;
					break;
				}else{
					found=1;
					potans=((long long)aa*b[k-1]+bb)%p;
				}	
			}
			i++;
			i--;
		}
		printf("Case #%d: ",_);
		if(found==1) printf("%d\n",potans);else puts("I don't know.");
		fflush(stdout);
	}
	return 0;
}
