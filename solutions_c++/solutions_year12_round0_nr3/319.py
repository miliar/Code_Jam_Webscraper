#include <stdio.h>

int pow[15];
int isGet[2000005];
int list[100],sList;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j;
    pow[0]=1;
    for(i=1;i<15;i++){
    	pow[i]=pow[i-1]*10;
    }
    int zz,xx;
    scanf("%d",&xx);
    int a,b,x,p,gen;
    long long c=0;
    for(zz=1;zz<=xx;zz++){
        c=0;
    	printf("Case #%d: ",zz);
    	scanf("%d%d",&a,&b);
    	int d=0,div=1;
    	x=a-1;
    	while(x!=0){
    		x/=10;
    		div*=10;
    		d++;
    	}
        for(i=a;i<b;i++){
            sList=0;
            if(i/div!=0){
            	div*=10;
            	d++;
            }
            for(j=1;j<d;j++){
                if((i%pow[j])/(pow[j-1])==0){
                	continue;
                }else{
                    x=(i%pow[j])*pow[d-j]+(i/pow[j]);
                    if(x>i && x<=b){
                        if(!isGet[x]){
                            list[++sList]=x;
                            isGet[x]=1;
                            c++;
                        }
                    }
                }
            }
            for(j=1;j<=sList;j++){
            	isGet[list[j]]=0;
            }
        }
    	printf("%lld\n",c);
    }
	return 0;
}
/*
4
1 9
10 40
100 500
1111 2222
*/
