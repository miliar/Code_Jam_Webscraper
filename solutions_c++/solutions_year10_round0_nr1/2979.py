/* GCJ' 10 Snapper Chain
 * Radar798
 */
#include<stdio.h>
#include<math.h>
	long T;
    long N[10010],K[10010];

void init(){
	scanf("%d",&T);
	for(long i=1;i<=T;i++){
		scanf("%ld %ld",&N[i],&K[i]);
	}
}

void snapper(long m){
    double M,S;
	M=pow(2,N[m]);
    S=fmod((K[m]+1),M);
	if(S==0.0)printf("Case #%d: ON\n",m);
	else printf("Case #%d: OFF\n",m);
}

int main(void){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	init();
	for(long w=1;w<=T;w++)snapper(w);
    return 0;
}	