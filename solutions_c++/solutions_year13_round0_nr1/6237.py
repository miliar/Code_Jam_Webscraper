#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int compute(char arr[6][6]){
	int i,j;
int countX=0,countO=0,countT=0,countall=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(arr[i][j]=='X'){countX=countX+1;}
				else if(arr[i][j]=='T'){countT=countT+1;}
				else if(arr[i][j]=='O'){countO=countO+1;}
			}
			if(countX==4||(countX==3&&countT==1)){
				return 1;
			}
			else if(countO==4||(countO==3&&countT==1)){	
				return 2;
			}			
			countX=countO=countT=0;			
		}
		
		for(j=0;j<4;j++){
			for(i=0;i<4;i++){
				if(arr[i][j]=='X')countX=countX+1;
				else if(arr[i][j]=='T')countT=countT+1;
				else if(arr[i][j]=='O')countO=countO+1;
			}
			if(countX==4||(countX==3&&countT==1)){
				return 1;
			}
			else if(countO==4||(countO==3&&countT==1)){	
				return 2;
			}
			countX=countO=countT=0;			
		}	
		countX=countO=countT=0;
			
		for(i=0;i<4;i++){
			j=i;
			if(arr[i][j]=='X'){countX=countX+1;}
			else if(arr[i][j]=='T'){countT=countT+1;}
			else if(arr[i][j]=='O'){countO=countO+1;}
			}
			if(countX==4||(countX==3&&countT==1)){
				return 1;
			}
			else if(countO==4||(countO==3&&countT==1)){	
				return 2;
			}	
			countX=countO=countT=0;	
			
			i=0;
		for(j=3;j>=0;j--){
			if(arr[i][j]=='X'){countX=countX+1;}
			else if(arr[i][j]=='T'){countT=countT+1;}
			else if(arr[i][j]=='O'){countO=countO+1;}
			i=i+1;
			}
			if(countX==4||(countX==3&&countT==1)){
				return 1;
			}
			else if(countO==4||(countO==3&&countT==1)){	
				return 2;
			}
		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(arr[i][j]!='.'){
					countall++;
				}

			}
		}
		if(countall==16)return 3;
	
		return 4;					
}


int main(){
	int t,k=0;
	FILE*in=fopen("A-Large.in","r");
	FILE*out=fopen("output.txt","w");
	fscanf(in,"%d",&t);
	while(k<t){
		char arr[6][6];		
		int i,j;
		for(i=0;i<4;i++){
				fscanf(in,"%s",&arr[i]);
		}
		
		int ans=compute(arr);
		if(ans==1)fprintf(out,"Case #%d: X won\n",k+1);
		else if(ans==2)fprintf(out,"Case #%d: O won\n",k+1);
		else if(ans==3)fprintf(out,"Case #%d: Draw\n",k+1);
		else fprintf(out,"Case #%d: Game has not completed\n",k+1);
		
		k++;
	}

	
}




