#include <stdio.h>
#include <stdlib.h>

int zz,tt;
int n;
int table[1000][2];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    scanf("%d",&tt);
    int count=0;
    for(zz=1;zz<=tt;zz++){
        count=0;
    	scanf("%d",&n);
    	for(i=1;i<=n;i++){
    		scanf("%d%d",&table[i][0],&table[i][1]);
    	}
    	for(i=1;i<=n;i++){
    		for(j=i+1;j<=n;j++){
    			if(table[i][0]>table[j][0] && table[j][1]>table[i][1]){
    			    count++;
                }
    			if(table[j][0]>table[i][0] && table[i][1]>table[j][1]){
    			    count++;
                }
    		}
    	}
    	printf("Case #%d: %d\n",zz,count);
    }
	return 0;
}
/*
2
3
1 10
5 5
7 7
2
1 1
2 2
*/
