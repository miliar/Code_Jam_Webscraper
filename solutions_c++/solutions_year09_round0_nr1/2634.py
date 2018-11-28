#include <stdio.h>
#include <string.h>
char palavra[5001][20];
char pattern[1000000];


int casa(char *string, char *pattern){
	int i,j;
	bool abrindo;

	i = 0 ;
	j = 0 ;
	
	abrindo = false;
	
	while( i < strlen(string) && j < strlen(pattern) ){
		
		if( pattern[j] == '(' ) { abrindo = true; j++;}
		else if(string[i]==pattern[j]) {
			//printf("encontrou %c\n",string[i]);
			if(abrindo){
				while(pattern[j]!= ')') j++;
				abrindo = false;
			}
			j++;
			i++;
		}
		else if( abrindo && string[i]!=pattern[j]){
			//printf("nao encontrou %c\n", string[i]);
			j++;
		}
		else if( abrindo && pattern[j]==')') {  
			//printf("erro abrindo\n");
			return 0;
			}
		else if(!abrindo && string[i]!=pattern[j]){ 
			//printf("erro normal\n");
			return 0;
		}
	}
	
	if(i== strlen(string) && j == strlen(pattern) ){ return 1; }
	else return 0;

}

int main(){
	
	int d,l,i,j,cont,n;
	
	
		
		scanf("%d %d %d",&l,&d,&n);
	
		for(i=0;i<d;i++)
		 scanf("%s",palavra[i]);
	
		for(j=0;j<n;j++){
		
		  
			
			scanf("%s",pattern);
		
			
			cont = 0 ;
			
			for(i=0;i<d;i++){
				//printf("tentando casa %s %s\n",palavra[i],pattern);
				if( casa(palavra[i],pattern) ) cont++; 
			}
			
			printf("Case #%d: %d\n",j+1,cont);
	  }
		
	

}
