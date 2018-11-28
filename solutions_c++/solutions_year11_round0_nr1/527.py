#include<stdio.h>
#include<stdlib.h>
#define ABS(x) ((x)>0?(x):-(x))
#define MAX(x,y) ((x)>(y)?(x):(y))
int main(){
	freopen("A-large.in","r",stdin);
	freopen("BansA.out","w",stdout);
	
	int T,t,n,a,b,ta,tb,x,i;
	char c[20];
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		a=1;
		b=1;
		ta=0;
		tb=0;
		for(i=0;i<n;i++){
			scanf("%s%d",c,&x);
			if(c[0]=='O'){
				ta+=ABS(x-a)+1;
				if(ta<=tb)ta=tb+1;
				a=x;
			}
			else{
				tb+=ABS(x-b)+1;
				if(tb<=ta)tb=ta+1;
				b=x;
			}
		}
		printf("Case #%d: %d\n",t,MAX(ta,tb));
	}
}
 
