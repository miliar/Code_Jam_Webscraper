#include<cstdlib>
#include<stdio.h>

int main(){
    int T, A, B, pi;
	float p[3], min, ans;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
	    scanf("%d%d", &A,&B);
	    for(int j=0; j<A; j++)  scanf("%f", &p[j]);
	    //for(int j=0; j<A; j++)  printf("%f", p[j]);
	    for(int j=0; j<A; j++){
		    pi=j;
			if(p[j]!=1)  break;
		}
		//case 1
		min=1;
		for(int j=0; j<A; j++)  min*=p[j];
		ans=(B-A+1)*min+(2*B-A+2)*(1-min);
		//case 2
		min=1;
		for(int j=0; j<A-1; j++)  min*=p[j];
		min=(B-A+3)*min+(2*B-A+4)*(1-min);
		if(min<ans)  ans=min;
		//case 3
		min=1;
		for(int j=0; j<A-2; j++)  min*=p[j];
		min=(B-A+5)*min+(2*B-A+6)*(1-min);
		if(min<ans)  ans=min;
		//case 4
		min=B+2;
		if(min<ans)  ans=min;
		printf("Case #%d: %.6f\n", i+1, ans);
	}
    return 0;
}
