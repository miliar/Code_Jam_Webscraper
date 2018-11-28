#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
using namespace std;

int main() {	
	int T = 0;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++) {
		string str;
		string strR; 

		//strcpy(str,"");
		//scanf("%s\n",str);
		//strcpy(strR,str);
		str = "";
		getline(cin,str);
		strR = str;		
		
		for (int j=0; j<str.length(); j++) {
			if (str[j] == 'a') {
				strR[j] = 'y';
			} else if (str[j] == 'b') {
				strR[j] = 'h';
			} else if (str[j] == 'c') {
				strR[j] = 'e';
			} else if (str[j] == 'd') {
				strR[j] = 's';
			} else if (str[j] == 'e') {
				strR[j] = 'o';
			} else if (str[j] == 'f') {
				strR[j] = 'c';
			} else if (str[j] == 'g') {
				strR[j] = 'v';
			} else if (str[j] == 'h') {
				strR[j] = 'x';
			} else if (str[j] == 'i') {
				strR[j] = 'd';
			} else if (str[j] == 'j') {
				strR[j] = 'u';
			} else if (str[j] == 'k') {
				strR[j] = 'i';
			} else if (str[j] == 'l') {
				strR[j] = 'g';
			} else if (str[j] == 'm') {
				strR[j] = 'l';
			} else if (str[j] == 'n') {
				strR[j] = 'b';
			} else if (str[j] == 'o') {
				strR[j] = 'k';
			} else if (str[j] == 'p') {
				strR[j] = 'r';
			} else if (str[j] == 'q') {
				strR[j] = 'z';
			} else if (str[j] == 'r') {
				strR[j] = 't';
			} else if (str[j] == 's') {
				strR[j] = 'n';
			} else if (str[j] == 't') {
				strR[j] = 'w';
			} else if (str[j] == 'u') {
				strR[j] = 'j';
			} else if (str[j] == 'v') {
				strR[j] = 'p';
			} else if (str[j] == 'w') {
				strR[j] = 'f';
			} else if (str[j] == 'x') {
				strR[j] = 'm';
			} else if (str[j] == 'y') {
				strR[j] = 'a';
			} else if (str[j] == 'z') {
				strR[j] = 'q';
			}
		}
		
		printf("Case #%d: ",i+1);
		cout << strR;
		printf("\n");
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	return 0;
}