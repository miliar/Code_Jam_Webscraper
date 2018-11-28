#include <stdio.h>
#include <stdlib.h>

#define INF 999999999

int tt,zz,n;
int table[105][105],temp[105][105];

void clear(){
    for(int i=0;i<105;i++){
    	for(int j=0;j<105;j++){
    		table[i][j]=0;
    	}
    }
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int i,j,k;
    scanf("%d",&tt);
    int x1,x2,y1,y2;
    for(zz=1;zz<=tt;zz++){
    	scanf("%d",&n);
    	int maxR=0,maxC=0;
    	clear();
    	for(i=1;i<=n;i++){
    		scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
    		if(y2>maxR){
    		    maxR=y2;
            }
            if(x2>maxC){
                maxC=x2;
            }
    		for(j=y1;j<=y2;j++){
    			for(k=x1;k<=x2;k++){
    				table[j][k]=1;
    			}
    		}
    	}
    	int time=0;
    	int isNotDie=1;
    	while(isNotDie){
    	    isNotDie=0;
            for(i=1;i<=maxR;i++){
                for(j=1;j<=maxC;j++){
                    if(table[i][j]==1){
                        if(table[i-1][j]==0 && table[i][j-1]==0){
                            //printf("#%d %d\n",i,j);
                            temp[i][j]=-1;
                        }else{
                            temp[i][j]=0;
                        }
    	                isNotDie=1;
                    }else{
                        if(table[i-1][j]==1 && table[i][j-1]==1){
                            //printf("##%d %d\n",i,j);
                            temp[i][j]=1;
                        }else{
                            temp[i][j]=0;
                        }
                    }
                }
            }
            for(i=1;i<=maxR;i++){
                for(j=1;j<=maxC;j++){
                    table[i][j]+=temp[i][j];
                }
            }
            time++;
    	}
        printf("Case #%d: %d\n",zz,time-1);
    }
	return 0;
}
/*
1
3
5 1 5 1
2 2 4 2
2 3 2 4
*/
