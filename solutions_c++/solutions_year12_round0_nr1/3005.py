#include<cstdlib>
#include<stdio.h>

int main(){
	int function[26];
    function[0]='y';
    function[1]='h';
    function[2]='e';
    function[3]='s';
    function[4]='o';
    function[5]='c';
    function[6]='v';
    function[7]='x';
    function[8]='d';
    function[9]='u';
    function[10]='i';
    function[11]='g';
    function[12]='l';
    function[13]='b';
    function[14]='k';
    function[15]='r';
    function[16]='z';
    function[17]='t';
    function[18]='n';
    function[19]='w';
    function[20]='j';
    function[21]='p';
    function[22]='f';
    function[23]='m';
    function[24]='a';
    function[25]='q';
    int num;
    char question[101];
    scanf("%d ", &num);
    for(int i=0; i<num; i++){
	    gets(question);
	    printf("Case #%d: ", i+1);
	    for(int j=0; question[j]!='\0'; j++){
		    if(question[j]==32)  printf(" ");
		    else  printf("%c", function[question[j]-'a']);
		}
		printf("\n");
	}
    
    return 0;
}
