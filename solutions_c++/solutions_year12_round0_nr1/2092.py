#include<iostream>
#include<cstdio>
#include<cstdlib>
//#include<ctype>

#define forloop(i,a,b) for(int i=(a);i<(b);i++)

char mapping[30]="yhesocvxduiglbkrztnwjpfmaq";

void testing(){
	int count[26]={0};
	for(int i=0;mapping[i]!='\0';i++){
		count[mapping[i]-'a']++;
		printf("%d\n",mapping[i]-'a');
	}

	forloop(i,0,26){
		printf("%d",count[i]);
	}
	putchar('\n');
}

void run(int testcases){
	char *in_buffer = NULL;
	size_t len = 0;
    ssize_t read;

	for(int test=1;test<=testcases;test++){
		read = getline(&in_buffer, &len, stdin);
		//printf("Case #%d: %s",test,in_buffer);		

		for(int i=0;in_buffer[i]!='\0';i++){
			if(isalpha(in_buffer[i])){
				in_buffer[i]=mapping[in_buffer[i]-'a'];	
			}
		}	
		printf("Case #%d: %s",test,in_buffer);
	}

	free(in_buffer);
}

main(){
	//testing();
	int testcases;
	scanf("%d\n",&testcases);
	run(testcases);
}

