#include <iostream>
using namespace std;
int n;

int main(){
	char mapping[] = "yhesocvxduiglbkrztnwjpfmaq";
	FILE * file;
  	file = fopen ("A-small-attempt2.in","r");
	fscanf(file, "%d",&n);
	char c;
	c = fgetc(file);
	for(int i=0;i<n;i++){
		printf("Case #%d: ",i+1);
		while((c=fgetc(file)) != '\n'){
			if(c == ' ') printf("%c",c);
			else printf("%c",mapping[c-97]);
		}
		printf("\n");
	}
}