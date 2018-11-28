#include<stdio.h>
#include<string.h>

int tile(char map[50][51],int r,int c){
	char temp[50][51];
	int flag=1;
	for(int i=0;i<r;i++){
		strncpy(temp[i],map[i],c+1);
		flag = flag & (!strchr(map[i],'#'));
	}
	if(flag) return 1;
	
	for(int i=0;i<(r-1);i++){
		for(int j=0;j<(c-1);j++){
			if((temp[i][j]=='#')&& (temp[i][j+1]=='#') && (temp[i+1][j]=='#') && (temp[i+1][j+1]=='#')){
				temp[i][j]=temp[i+1][j+1]='/';
				temp[i+1][j]=temp[i][j+1]='\\';
				if(tile(temp,r,c) ==1){
					for(int i=0;i<r;i++){
						strncpy(map[i],temp[i],c+1);
					}
					return 1;
				}
				else {
					temp[i][j]=temp[i][j+1]=temp[i+1][j]=temp[i+1][j+1]='#';
				}
			}
		}
	}
	return 0;
}

int main(){

    int T,cas=0,r,c;
    char map[50][51];
    scanf("%d",&T);
    while (cas++ <T) {
    	for(int i=0;i<50;i++){
    		for(int j=0;j<51;j++){
    			map[i][j]=0;
    		}
    	}
    	scanf("%d %d",&r,&c);
    	for(int i=0;i<r;i++){
    		scanf("%s",map[i]);
    	}
   		printf("Case #%d:\n",cas);
    	if(tile(map,r,c) == 1){
    		for(int i=0;i<r;i++){
    			printf("%s\n",map[i]);
    		}
    	}
    	else {
    		printf("Impossible\n");
    	}
    }
    return 0;
}
