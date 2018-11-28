#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

#define MAX 1010000

int prime[100005],primeS;
int table[100005];
long long n;

void genPrime(){
    prime[1]=2;
    primeS=1;
    int i,j;
    for(i=3;i<=MAX;i+=2){
    	for(j=1;j<=primeS;j++){
    		if(i%prime[j]==0){
    			break;
    		}
    	}
    	if(j==primeS+1){
    		prime[++primeS]=i;
    	}
    }
}

int ans=0;
double logN;
// all prime = 78498

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    genPrime();
    int i,j;
    int xx,zz;
    scanf("%d",&zz);
    for(xx=1;xx<=zz;xx++){
        scanf("%lld",&n);
        if(n==1){
        	printf("Case #%d: 0\n",xx);
        	continue;
        }
        ans=1;
        long long temp;
        for(i=1;prime[i]*prime[i]<=n;i++){
            temp=prime[i];
            j=1;
            while(temp<=n){
            	temp*=prime[i];
            	j++;
            }
            j-=1;
            if(j==1){
            	break;
            }else{
                ans+=j-1;
            }
            //temp=floor(logN/log(prime[i]));
        }
        //sort(table+1,table+i);
        /*
        if(table[1]*table[2]<=n){
        	printf("ERROR");
        }
        for(j=1;j<i;j++){
        	printf("%d %d\n",j,table[j]);
        }*/
    	printf("Case #%d: ",xx);
    	printf("%d\n",ans);
    }/*
    for(i=1;i<=primeS;i++){
    	if(table[i]==0){
    		break;
    	}
    	printf("%d %d %d\n",i,prime[i],table[i]);
    }*/
	return 0;
}
/*
4
1
3
6
16
*/
