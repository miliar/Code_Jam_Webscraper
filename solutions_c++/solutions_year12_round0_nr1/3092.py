#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int main(){
	char c;
	char map[]="yhesocvxduiglbkrztnwjpfmaq";
	int i,j,z;
	scanf("%d",&z);
	c=getchar();
	for(i=1;i<=z;i++){
		printf("Case #%d: ",i);
		while(1){
			c=getchar();
			if(c=='\n'){
				printf("\n");
				break;
			}
			else if(c>='a'&&c<='z')
				printf("%c",map[c-'a']);
			else
				printf(" ");
		}
			
	}
	return 0;
}
