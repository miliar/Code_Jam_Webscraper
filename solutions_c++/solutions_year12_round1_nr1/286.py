#include <stdio.h>

int a,b;
double prob[1000005];
double min;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    int zz,xx;
    scanf("%d",&xx);
    double temp,now;
    for(zz=1;zz<=xx;zz++){
    	scanf("%d%d",&a,&b);
    	int x=b-a,bx=b+x+2;
    	now=1;
    	for(i=1;i<=a;i++){
    	    scanf("%lf",&temp);
            prob[i]=now*(1-temp);
    	    now*=temp;
    	}
    	prob[a+1]=now;
    	for(i=1;i<=a+1;i++){
    		prob[i]+=prob[i-1];
    	}
    	min=b+2;
    	for(i=0;i<=a;i++){
            temp=(x+1+2*i)*(prob[a+1]-prob[a-i]) + (bx+2*i)*(1-prob[a+1]+prob[a-i]);
            if(min>temp){
            	min=temp;
            }
    	}
    	printf("Case #%d: ",zz);
    	printf("%.10lf\n",min);
    }
	return 0;
}
/*
3
2 5
0.6 0.6
1 20
1
3 4
1 0.9 0.1
*/
