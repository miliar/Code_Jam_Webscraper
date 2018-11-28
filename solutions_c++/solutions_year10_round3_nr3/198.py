#include <stdio.h>
#include <stdlib.h>

int zz,tt;
int r,c;
int table[520][520];
int m[520][520];
int ans[520][2];

int min(int a,int b){
    if(a<b){
    	return a;
    }
    return b;
}

int min(int a,int b,int c){
    return min(min(a,b),c);
}

void reTable(){
    int i,j;
    for(i=1;i<=r;i++){
        for(j=1;j<=c;j++){
            if(m[i][j]==0){
                continue;
            }else if(table[i-1][j-1]==table[i][j] && table[i-1][j]==((table[i][j]+1)%2) && table[i-1][j]==table[i][j-1]){
                m[i][j]=min(m[i-1][j-1],m[i-1][j],m[i][j-1])+1;
            }else{
                m[i][j]=1;
            }
        }
    }
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,l;
    scanf("%d",&tt);
    char k;
    int temp;
    for(zz=1;zz<=tt;zz++){
    	scanf("%d%d",&r,&c);
    	scanf("%c",&k);
    	for(i=1;i<=r;i++){
    		for(j=1;j<=c;j++){
    			m[i][j]=0;
    		}
    	}
    	temp=c/4;
    	for(i=1;i<=r;i++){
    	    for(j=1;j<=temp;j++){
                scanf("%c",&k);
                if(k=='0'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=0;
                	table[i][4*j]=0;
                }else if(k=='1'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=0;
                	table[i][4*j]=1;
                }else if(k=='2'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=1;
                	table[i][4*j]=0;
                }else if(k=='3'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=1;
                	table[i][4*j]=1;
                }else if(k=='4'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=0;
                	table[i][4*j]=0;
                }else if(k=='5'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=0;
                	table[i][4*j]=1;
                }else if(k=='6'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=1;
                	table[i][4*j]=0;
                }else if(k=='7'){
                	table[i][4*j-3]=0;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=1;
                	table[i][4*j]=1;
                }else if(k=='8'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=0;
                	table[i][4*j]=0;
                }else if(k=='9'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=0;
                	table[i][4*j]=1;
                }else if(k=='A'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=1;
                	table[i][4*j]=0;
                }else if(k=='B'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=0;
                	table[i][4*j-1]=1;
                	table[i][4*j]=1;
                }else if(k=='C'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=0;
                	table[i][4*j]=0;
                }else if(k=='D'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=0;
                	table[i][4*j]=1;
                }else if(k=='E'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=1;
                	table[i][4*j]=0;
                }else if(k=='F'){
                	table[i][4*j-3]=1;
                	table[i][4*j-2]=1;
                	table[i][4*j-1]=1;
                	table[i][4*j]=1;
                }
    	    }
    	    scanf("%c",&k);
    	}
    	for(i=1;i<=r;i++){
    		for(j=1;j<=c;j++){
    			if(table[i-1][j-1]==table[i][j] && table[i-1][j]==((table[i][j]+1)%2) && table[i-1][j]==table[i][j-1]){
                    m[i][j]=min(m[i-1][j-1],m[i-1][j],m[i][j-1])+1;
                }else{
                    m[i][j]=1;
                }
    		}
    	}
    	int max=0;
    	for(i=1;i<=r;i++){
    		for(j=1;j<=c;j++){
    		    if(m[i][j]>max){
    		    	max=m[i][j];
    		    }
    		}
    	}
    	int countType=0,count=0;
    	for(i=max;i>=1;i--){
    	    count=0;
    	    for(j=1;j<=r;j++){
    	    	for(l=1;l<=c;l++){
    	    		if(m[j][l]==i && m[j-i+1][l-i+1]!=0 && m[j-i+1][l]!=0 && m[j][l-i+1]!=0){
    	    			count++;
    	    			int p,q;
    	    			for(p=j-i+1;p<=j;p++){
    	    				for(q=l-i+1;q<=l;q++){
    	    					m[p][q]=0;
    	    				}
    	    			}
    	    		}
    	    	}
    	    }
    		if(count!=0){
    		    countType++;
    			ans[countType][0]=i;
    			ans[countType][1]=count;
    			reTable();
    		}
    	}
    	printf("Case #%d: %d\n",zz,countType);
    	for(i=1;i<=countType;i++){
    		printf("%d %d\n",ans[i][0],ans[i][1]);
    	}
    }
	return 0;
}
/*
4
15 20
55555
FFAAA
2AAD5
D552A
2AAD5
D542A
4AD4D
B52B2
52AAD
AD552
AA52D
AAAAA
5AA55
A55AA
5AA55
4 4
0
0
0
0
4 4
3
3
C
C
4 4
6
9
9
6
*/
