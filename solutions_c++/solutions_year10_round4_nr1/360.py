#include <stdio.h>
#include <stdlib.h>

#define INF 999999999

int tt,zz,N;
int n,table[500][500],last[500],temp[500][500];

int isDiamon(int n, int r,int first){
    int i,j;
    for(i=0;i<n;i++){
        for(j=1;j<=n-i;j++){
        	if(table[r+i][first-1+j]!=table[r+i][first+n-i-j]){
        	    return 0;
            }
        	if(table[r-i][first-1+j]!=table[r-i][first+n-i-j]){
        	    return 0;
            }
        }
    }
    return 1;
}

int isDiamonUp(int n,int r,int first){
    if(n==r){
        int i,j,k=0;
        for(i=1;i<n;i++){
            if(r+i<=N){
                k++;
            }
            for(j=1;j<=n-i;j++){
                if(table[r-i][j]!=table[r+i][k+j]){
                    return 0;
                }
            }
        }
    }else{
        int i,j,k=0,r=n;
        for(i=1;i<n;i++){
            if(r+i<=N){
                k++;
            }
            for(j=1;j<=n-i;j++){
                if(temp[r-i][j]!=temp[r+i][k+j]){
                    return 0;
                }
            }
        }
    }
    return 1;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    scanf("%d",&tt);
    int x,sum;
    for(zz=1;zz<=tt;zz++){
        sum=0;
    	scanf("%d",&n);
    	N=n;
    	for(i=1;i<=n;i++){
    		for(j=1;j<=i;j++){
    			scanf("%d",&table[i][j]);
    			sum+=table[i][j];
    		}
    		last[i]=j-1;
    	}
    	x=n+1;
    	for(i=n-1;i>=1;i--){
    	    for(j=1;j<=i;j++){
    	    	scanf("%d",&table[x][j]);
    	    	sum+=table[x][j];
    	    }
    	    last[x]=j-1;
    	    x++;
    	}
        long long min=INF;
        int size,hSize;
        for(size=n;size>=1;size--){
            if(isDiamon(size,n,n-size+1)){
        	    min=n*n-(size*size)+2*(n-size)*(n-size);
        	    break;
            }
        	if(isDiamon(size,n,1)){
        	    min=n*n-(size*size)+2*(n-size)*(n-size);
        	    break;
            }
        }
        hSize=size;
        int p;
        for(i=1,p=2*n-1;i<=2*n-1;i++,p--){
        	for(j=1;j<=last[i];j++){
        		temp[p][j]=table[i][j];
        	}
        }
        for(size=n;size>=1;size--){
        	if(isDiamonUp(size,size,1)){
        	    size=n-hSize+size;
        	    n=2*n-hSize;
        	    min+=n*n-(size*size);
        	    min+=2*(n-size)*(n-size);
                break;
            }
            if(isDiamonUp(size,2*n-size,1)){
        	    size=n-hSize+size;
        	    n=2*n-hSize;
        	    min+=n*n-(size*size);
        	    min+=2*(n-size)*(n-size);
                break;
            }
        }
        printf("Case #%d: %lld\n",zz,min);
    }
	return 0;
}
/*
1
2
  1
 2 3
  4

2
1
0
2
 1
2 2
 1

4
1
0
2
 1
2 2
 1
2
 1
1 2
 1
3
  1
 6 3
9 5 5
 6 3
  1
*/
