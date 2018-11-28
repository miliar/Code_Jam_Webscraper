#include <stdio.h>
#include <string.h>

#define LEN 500
#define MENUS 10000

char s[LEN+1];
int times[19][LEN+1];
char *t;
int num = 0;
int len = 0;

int main(){
//	if(freopen("C-large.in", "r", stdin)!=NULL){
//		freopen("C-large.out", "w", stdout);
//	}
	int N;
	int i,j,k;
	scanf("%d",&N);
	gets(s);
	t="welcome to code jam";
	int ts=18;
	for(i=0;i<N;i++){
		gets(s);
		len = strlen(s);
		for(j=0;j<len;j++){
			if(s[j]=='m'){
				times[18][j] = 1;
			}
			else {
				times[18][j] = 0;
			}
		}
		for(j=17;j>=0;j--){
			for(k=len-1;k>=0;k--){
				times[j][k] = 0;
				if(s[k]==t[j]){
					for(int x=k+1;x<len;x++){
						times[j][k]+=times[j+1][x];
						times[j][k]%=10000;
					}
				}
			}
		}
		num = 0;
		for(j=0;j<len;j++){
			num+=times[0][j];
			num%=10000;
		}
		printf("Case #%d: %04d\n",i+1,num);
	}
	return 0;
}