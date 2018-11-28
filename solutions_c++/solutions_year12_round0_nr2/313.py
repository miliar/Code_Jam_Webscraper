#include <stdio.h>

int n,s,p;
int ans;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j;
    int zz,x;
    scanf("%d",&zz);
    for(int z=1;z<=zz;z++){
    	printf("Case #%d: ",z);
    	scanf("%d%d%d",&n,&s,&p);
    	ans=0;
    	for(i=1;i<=n;i++){
    		scanf("%d",&x);
    		if(x==0){
    			if(x>=p){
    				ans++;
    			}
    		}else if((x+2)/3>=p){
    			ans++;
    		}else if((x+2)/3 +1 == p && s!=0 && x%3!=1){
    			s--;
    			ans++;
    		}
    	}
    	printf("%d\n",ans);
    }
	return 0;
}
/*
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
*/
