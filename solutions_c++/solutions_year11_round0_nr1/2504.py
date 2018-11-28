#include <stdio.h>

int n;
int b,o;
int sum,plus;
int table[105][2];

int inline ab(int x){
    if(x<0){
    	return -x;
    }
    return x;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int i,j;
    int xx,zz;
    scanf("%d",&zz);
    for(xx=1;xx<=zz;xx++){
        sum=0;
        plus=0;
    	scanf("%d",&n);
    	char str[3];
    	for(i=1;i<=n;i++){
    		scanf("%s",&str[1]);
    		scanf("%d",&table[i][1]);
    		if(str[1]=='B'){
                table[i][0]=0;
    		}else{
                table[i][0]=1;
    		}
    	}
    	b=1,o=1;
    	int temp;
    	table[0][0]=-1;
    	for(i=1;i<=n;i++){
            if(table[i][0]==table[i-1][0]){
                temp=ab(table[i][1]-table[i-1][1])+1;
                sum+=temp;
                plus+=temp;
                if(table[i][0]==0){
                	b=table[i][1];
                }else{
                    o=table[i][1];
                }
            }else{
                if(table[i][0]==0){
                    temp=ab(table[i][1]-b)-plus;
                    plus=0;
                	if(temp>0){
                	    sum+=temp;
                	    plus=temp;
                    }
                    sum+=1;
                    plus++;
                    b=table[i][1];
                }else{
                    temp=ab(table[i][1]-o)-plus;
                    plus=0;
                	if(temp>0){
                	    sum+=temp;
                	    plus=temp;
                    }
                    sum+=1;
                    plus++;
                    o=table[i][1];
                }
            }
    	}
    	printf("Case #%d: %d\n",xx,sum);
    }
	return 0;
}
/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
