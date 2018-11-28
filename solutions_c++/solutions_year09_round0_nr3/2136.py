#include<stdio.h>
#include<string.h>

#define MAXL 32
#define MAXT 1024
#define MM 10000

char buf[1024];
char *ss = " welcome to code jam\0";
int tam1 = 19,tam2;
int pd[MAXL][MAXT];

int main(){
	int n,i,j;
	char c;
	
	scanf("%d",&n);
	scanf(" ");
	
	
	int tot = n;

	while(n--){
		gets(buf + 1);
		tam2 = strlen(buf + 1);
		
		for(j=0;j<=tam2;j++){
			pd[0][j] = 1;
		}
		for(i=1;i<=tam1;i++){
			pd[i][0] = 0;
		}
		
		for(i=1;i<=tam1;i++){
			for(j=1;j<=tam2;j++){
				c = buf[j];
				if(c == ss[i]){
					pd[i][j] = (pd[i-1][j-1] + pd[i][j-1])%MM;
				}else{
					pd[i][j] = pd[i][j-1];
				}
			}
		}
		
		printf("Case #%d: %04d\n",tot-n,pd[tam1][tam2]);
	}
	return 0;
}
