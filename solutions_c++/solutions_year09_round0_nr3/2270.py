#include <stdio.h>
#include <string.h>

const char* pattern="welcome to code jam";
unsigned int occur[25];

int searchfor(const char* buff) {
	int i;
	for(i=0;i<25;i++) occur[i]=0;
	occur[0]=1;
	while(*buff) {
		for(i=0;i<strlen(pattern);i++) {
			if((*buff)==pattern[i]) {
				occur[i+1]=(occur[i+1]+occur[i])%10000;
			}
		}
		buff++;
	}
	return occur[strlen(pattern)];
}

void getline(char* buffer) {
	while(((*buffer)=getchar())!='\n') buffer++;
	(*buffer)=0;
}

int main(void) {
	char buffer[600];
	int line=1;
	int lines=0;
	int point=0;
	int i;
	scanf("%d\n",&lines);
	for(i=0;i<lines;i++) {
		getline(buffer);
		printf("Case #%d: %04d\n",i+1,searchfor(buffer));
	}
}

