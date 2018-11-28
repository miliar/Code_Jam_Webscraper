#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

	int i,j,vstupy;

	scanf("%d\n", &vstupy);

	char *riadok;
	char pomz;
	riadok = (char *) malloc(101*sizeof(char));

	for(i=1;i<=vstupy;i++){
	
	gets(riadok);

	printf("Case #%d: ", i);

	j=0;
	while(j<strlen(riadok)){

		if (riadok[j]=='a')
			printf("y");
		if (riadok[j]=='b')
			printf("h");
		if (riadok[j]=='c')
			printf("e");
		if (riadok[j]=='d')
			printf("s");
		if (riadok[j]=='e')
			printf("o");
		if (riadok[j]=='f')
			printf("c");
		if (riadok[j]=='g')
			printf("v");
		if (riadok[j]=='h')
			printf("x");
		if (riadok[j]=='i')
			printf("d");
		if (riadok[j]=='j')
			printf("u");
		if (riadok[j]=='k')
			printf("i");
		if (riadok[j]=='l')
			printf("g");
		if (riadok[j]=='m')
			printf("l");
		if (riadok[j]=='n')
			printf("b");
		if (riadok[j]=='o')
			printf("k");
		if (riadok[j]=='p')
			printf("r");
		if (riadok[j]=='q')
			printf("z");
		if (riadok[j]=='r')
			printf("t");
		if (riadok[j]=='s')
			printf("n");
		if (riadok[j]=='t')
			printf("w");
		if (riadok[j]=='u')
			printf("j");
		if (riadok[j]=='v')
			printf("p");
		if (riadok[j]=='w')
			printf("f");
		if (riadok[j]=='x')
			printf("m");
		if (riadok[j]=='y')
			printf("a");
		if (riadok[j]=='z')
			printf("q");
		if (riadok[j]==' ')
			printf(" ");

		j++;
	}

	printf("\n");

	}

	return 0;
}