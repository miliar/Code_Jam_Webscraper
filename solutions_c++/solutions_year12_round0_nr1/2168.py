//============================================================================
// Name        : Qua-A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

char code[] = "yhesocvxduiglbkrztnwjpfmaq";
char str[200];

int main() {
	int nc, c;
	scanf("%d", &nc);
	gets(str);
	for (c = 1; c <= nc; ++c) {
		//scanf("%s", str);
		gets(str);
		printf("Case #%d: ", c);
		int l = strlen(str);
		for (int i = 0; i < l; ++i)
			if (str[i] >= 'a' && str[i] <= 'z')
				printf("%c", code[str[i] - 'a']);
			else
				printf("%c", str[i]);
		printf("\n");
	}
	return 0;
}
