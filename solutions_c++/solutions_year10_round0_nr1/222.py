#include<stdio.h>
#include<memory.h>

int n,k;

int judge(int a,int b){
    int ans = 1;
    for(int i=0;i<b;i++){
	    if((a&(1<<i))==0){
	        ans = 0;
	       break;
		}
	}
	return ans;
}
int main(){
    int t;
    int ccount = 0;
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
	    scanf("%d %d",&n,&k);
	    int test = judge(k,n);
	    if(test==1)
	       printf("Case #%d: ON\n",++ccount);
	    else
	       printf("Case #%d: OFF\n",++ccount);
	}
	return 0;
}
