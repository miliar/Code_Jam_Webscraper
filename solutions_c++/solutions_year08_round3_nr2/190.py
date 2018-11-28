#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<map>
#include<set>
#include<vector>

using namespace std;
char num[100];
char sign[100];/* 0 + 1 - 2 . */
long long int total;
int tam;
int dive[] = {2, 3, 5, 7};
void vai(int p){
	int i;
	int long long aux,temp;
	char op;
	if(p==(tam-1)){
		
		aux = num[0];
		i = 0;
		op = -1;
		while(1){
			while(i<(tam-1) && sign[i]==2){
				aux = aux*10 + num[i+1];
				i++;
			}
			if(op!=-1){
				if(op==0){
					temp = temp+aux;
				}else
					temp = temp-aux;
			}else
				temp = aux;

			if(i==(tam-1))
				break;

			op = sign[i];
			aux = num[i+1];
			i++;
		}
/*		for(i=0;i<(tam-1);i++){
			printf("%d ",sign[i]);
		}
		cout << temp <<endl;
		printf("\n");*/
		if(temp<0)
			temp = -temp;
		for(i=0;i<4;i++)
			if(temp%dive[i] == 0)
				break;
		if(i<4)
			total++;
		
		return;
	}
	sign[p] = 0;
	vai(p+1);
	sign[p] = 1;
	vai(p+1);
	sign[p] = 2;
	vai(p+1);
	return;
}

int main(){
	int tc,ntc,i;
	
	scanf("%d",&ntc);

	for(tc=0;tc<ntc;tc++){
		char ch;
		i=0;
		scanf(" %c",&ch);
		while((ch>='0')&&(ch<='9')){
			num[i] = ch - '0';
			i++;
			scanf("%c",&ch);
		}
		tam = i;
		
		num[tam] = '\0';
		total = 0;
		vai(0);

		cout <<"Case #"<<tc+1<<": "<<total<<endl;

	}

}

