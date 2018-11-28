#include<stdio.h>
#include<math.h>

int main(){
	freopen("B-small-attempt0 (1).in","r",stdin);
	freopen("B.out","w",stdout);
	int t,l,p,c,f=1,i,x;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d %d",&l,&p,&c);
		i=(int)(log10((double)(p)/(double)(l))/log10((double)c)); 
	//	printf("i=%d...\n",i);
		if(l*pow(c,i+1)<p) i++;
		//	printf("i=%d...\n",i);
		if(fabs(l*pow(c,i)-p)<1e-10) i--;
		//	printf("i=%d...\n",i);
			i++;
		//	printf("ii=%d\n",i);
		for(x=0;;x++){
			if((1<<x)>=i)  break;
		}
		printf("Case #%d: %d\n",f++,x);
	}
	return 0;
}


