#include <stdio.h>
#include <stdlib.h>

int gcd(int x,int y){
    if(y==0){
    	return x;
    }
    return gcd(y,x%y);
}

int zz,c,n;
int table[1005];

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int i,j,temp,d;
    scanf("%d",&c);
    for(zz=1;zz<=c;zz++){
        scanf("%d",&n);
    	for(i=1;i<=n;i++){
    		scanf("%d",&table[i]);
    	}
    	temp=table[1];
    	for(i=1;i<n;i++){
    		table[i]=table[i+1]-table[i];
    		if(table[i]<0){
    			table[i]=-table[i];
    		}
    	}
    	table[n]=table[n]-temp;
    	if(table[n]<0){
    	    table[n]=-table[n];
        }
    	d=table[1];
    	for(i=1;i<=n;i++){
    		d=gcd(d,table[i]);
    	}
    	if(temp%d==0){
    	    printf("Case #%d: 0\n",zz);
    	}else{
    	    printf("Case #%d: %d\n",zz,d*((temp/d)+1)-temp);
        }
    }
	return 0;
}
