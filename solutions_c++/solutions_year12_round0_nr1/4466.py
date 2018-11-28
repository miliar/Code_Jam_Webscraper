#include<cstdio>
#include<cstring>

int t,i,k,j;
char q[107];

int main(){
	char x[]="yhesocvxduiglbkrztnwjpfmaq";	
	scanf("%d\n",&t);
	for(i=1;i<=t;++i){
			gets(q);
			k=strlen(q);
//			for(j=0;j<k;++j){
//				printf("%c",q[j]);
//			}
//			printf("\n");
			printf("Case #%d: ",i);
			for(j=0;j<k;++j){
				if(q[j]==' '){
					printf(" ");
					continue;
				}
				printf("%c",x[q[j]-'a']);

			}
		printf("\n");
	}


	return 0;
}
