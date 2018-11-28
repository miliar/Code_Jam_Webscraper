//============================================================================
// Name        : googlejam.cpp
// Author      : lw
// Version     :
// Copyright   : ;]
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <map>
#include <string>

using namespace std;


int main() {
	int i;
	scanf("%d", &i);
	string str;
	char text1[150] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char text2[150] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	char translate[255];
	for (int j = 0; j < 255; j++)translate[j]='#';
	int j = 0;
	while ( text1[j] != 0 ){
		translate[(int)text1[j]] = text2[j];
		j++;
	}
	translate['q'] = 'z';
	translate['z'] = 'q';
	//for (int j = 97; j < 123; j++) printf("%c -> %c \n", j, translate[j]);
	char c;
	c = getchar();
	for (int j = 0; j < i; j++){
		printf("Case #%d: ", j+1);
		while( ( c = getchar() ) != '\n' ){
			printf("%c", translate[c]);
		}
		printf("\n");
	}


	return 0;
}

