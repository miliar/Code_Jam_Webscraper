#include <cstdio>
#include <cctype>
int main(){
	char x[] = "yhesocvxduiglbkrztnwjpfmaq";
	char ch;
	int t = 0;
	scanf("%d\n", &t);
	for(int k = 0; k <t; k++){
		printf("Case #%d: ", k+1);
		
		for(int i=0; i<101 && (ch = getchar())!= EOF && ch != '\n'; i++) {
			if(ch == ' '){
				putchar(' ');
			}else{
//			putchar(ch);
			ch-='a';
			if(t == 6)
				printf("%c",ch );
			putchar(x[(int)ch]);
			}
		 }
		 printf("\n");
	}
}
