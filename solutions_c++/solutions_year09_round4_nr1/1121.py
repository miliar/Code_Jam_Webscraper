#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>

using namespace std;

int v[64];

int main(){
	int teste,tot,i,max1,j,troca,pos,n,aux;
	char c;
	
	scanf("%d",&teste);
	tot = teste;
	while(teste--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			max1 = 0;
			for(j=0;j<n;j++){
				scanf(" %c",&c);
				if(c == '1')
					max1 = max(max1,j+1);
			}
			v[i] = max1;
		}
		
		troca = 0;
		for(i=0;i<n;i++){
			if(v[i] > i+1){
				pos = i;
//				printf("entro\n");
				while(v[pos] > pos+1){
//					printf("pos= %d v = %d\n",pos+1,v[pos]);

					for(j = pos+1;j<n;j++)
						if(v[j] <= pos+1)
							break;
							
					for(; j != pos;j--){
						troca++;
						aux = v[j-1];
						v[j-1] = v[j];
						v[j] = aux;
					}
					
					pos++;
				}
			}
		}
		
		printf("Case #%d: %d\n",tot-teste,troca);
		
	}
	return 0;
}
