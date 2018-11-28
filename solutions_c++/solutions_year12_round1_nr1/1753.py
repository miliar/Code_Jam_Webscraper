#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main(){
freopen("A-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);
	int i,j,k,t,a,b;
	double num[1005],ans[1005],y,x;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
        memset(ans , 0 , sizeof(ans));
        scanf("%d%d",&a,&b);
        for(j=0;j<a;j++){
 		    scanf("%lf",&num[j]);
		}
	 	for(j=0;j<a;j++){
		    y = 1;
	        for(k=0;k<=j;k++){
  			    if(k==j)
  			        y *= 1-num[k];
       		    else
       		        y *= num[k];
			}
 		    ans[0] += (2+b)*y;	 	    
 		    ans[1] += (b-a+1+b+1)*y; 		     		  
 		    for(k=1;k<=a;k++){
                if(a-k<=j)
                    ans[k+1] += (k+k+b-a+1)*y;
                else if(k==a)
                    ans[k+1] += (k+b+1)*y;
                else
	  		        ans[k+1] += (b-a+1+b+1+k*2)*y;     		      	  	
	  		}
		}
		y = 1;
	 	for(k=0;k<a;k++){
			 y *= num[k];
		}
		ans[0] += (a==b ? 1 : 2+b)*y;		
		ans[1] += (1+b-a)*y;		
		for(k=1;k<=a;k++){
			ans[k+1] += (k+k+b-a+1)*y;			
		}
		x = 100000;
		for(j=0;j<=a+1;j++){
	 	    x = min(x,ans[j]);
		}
		printf("Case #%d: %.6lf\n",i,x);
	}
} 
