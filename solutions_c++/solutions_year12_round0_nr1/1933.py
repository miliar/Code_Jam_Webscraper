#include <stdio.h>
#define SIZE 1001
int table[30] = {121, 104, 101, 115, 111, 99, 118, 120, 100, 117, 105, 103, 108, 98, 107, 114, 122, 116, 110, 119, 106, 112, 102, 109, 97, 113};
char s[SIZE];
int main(){
	int c;
	scanf("%d\n", &c);
	for(int i=1;i<=c;++i){
		gets(s);
		printf("Case #%d: ", i);
		for(int j=0;s[j];++j){
			if(s[j] < 97 || s[j] > 122) printf("%c", s[j]);
			else						printf("%c", table[s[j]-'a']);
		}
		printf("\n");
	}
	return 0;
}
