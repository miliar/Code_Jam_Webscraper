#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char googlerese(char input);

int main(){
	int tests,i;
	char c;
	char output;
	int count=1;

	FILE *fr;
	//fr=fopen("in1.txt","r");
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&tests);

	//printf("test %d\n",tests);
	while((c=getc(stdin))!=EOF){
	//	c=getc(fr);
		output=googlerese(c);

		if(output!='\n'){
		printf("%c",output);
		}
		else{
			if(count>1 && count<=tests) printf("\n");
			if(count<=tests) printf("Case #%d: ",count);
			count++;
		}
	}
	printf("\n");

return 0;
}

char googlerese(char input){
	char output;

	if(input=='a'){
		output='y';
		return output;
	}

	if(input=='b'){
		output='h';
		return output;
	}

	if(input=='c'){
		output='e';
		return output;
	}

	if(input=='d'){
		output='s';
		return output;
	}

	if(input=='e'){
		output='o';
		return output;
	}

	if(input=='f'){
		output='c';
		return output;
	}
	
	if(input=='g'){
		output='v';
		return output;
	}

	if(input=='h'){
		output='x';
		return output;
	}

	if(input=='i'){
		output='d';
		return output;
	}

	if(input=='j'){
		output='u';
		return output;
	}

	if(input=='k'){
		output='i';
		return output;
	}

	if(input=='l'){
		output='g';
		return output;
	}

	if(input=='m'){
		output='l';
		return output;
	}

	if(input=='n'){
		output='b';
		return output;
	}

	if(input=='o'){
		output='k';
		return output;
	}

	if(input=='p'){
		output='r';
		return output;
	}

	if(input=='q'){
		output='z';
		return output;
	}

	if(input=='r'){
		output='t';
		return output;
	}

	if(input=='s'){
		output='n';
		return output;
	}

	if(input=='t'){
		output='w';
		return output;
	}

	if(input=='u'){
		output='j';
		return output;
	}

	if(input=='v'){
		output='p';
		return output;
	}

	if(input=='w'){
		output='f';
		return output;
	}

	if(input=='x'){
		output='m';
		return output;
	}

	if(input=='y'){
		output='a';
		return output;
	}

	if(input=='z'){
		output='q';
		return output;
	}

	if(input=='\n'){
		output='\n';
		return output;
	}

	if(input==' '){
		output=' ';
		return output;
	}

	return input;

}
