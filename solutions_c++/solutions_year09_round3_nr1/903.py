#include <stdio.h>
#include <string.h>
#include <map>
#include <iostream>
#define num_letra 'z' - 'a' + 1

using namespace std;

map <char,char> troca;

int digito[10];
int letra[num_letra];
char number[62];
int cont;
int d;
long long int n;

int main(){
	
	int i, teste=1;
	
	scanf("%d",&d);
	
	
	
	while(d--){
		
		
		
		scanf("%s",number);
		
		memset(digito, 0 , sizeof(digito) );
		
		memset(letra, 0 , sizeof(letra) );
		
		
		cont = 0;
		
		for(i=0;i<strlen(number);i++){
				if(number[i] >= 'a' && number[i] <= 'z'){
				 if(letra[number[i]-'a']==0){
				  letra[number[i]-'a']=1;
				  cont++;
				  if(cont==1){
						troca[ number[i] ] = '1';
						number[i] = '1';
					}else if(cont==2){
						troca[ number[i] ] = '0';
						number[i] = '0';
					}else {
					  troca[ number[i] ] = '0'+cont-1;
						number[i] = '0'+cont-1;
					}
		
				}else{
					number[i] = troca[number[i]];
				}
			}else if(number[i]>='0' && number[i] <= '9'){
			   if(digito[number[i]-'0']==0){
				  digito[number[i]-'0']=1;
				  cont++;
				  if(cont==1){
						troca[ number[i] ] = '1';
						number[i] = '1';
					}else if(cont==2){
						troca[ number[i] ] = '0';
						number[i] = '0';
					}else {
					  troca[ number[i] ] = '0'+cont-1;
						number[i] = '0'+cont-1;
					} 
				}else{
					number[i] = troca[number[i]];
				}
			}
		}
		
		
		troca.clear();
		
		if(cont==1) cont++;
		
		n = 0;
		
		for(i=0;i<strlen(number);i++){
			n = n * (long long int)cont;
			n = n + (long long int)number[i]-'0';
		}
		
		printf("Case #%d: ", teste++);
		cout << n << endl;
		
		
		
		
		
	}

}
