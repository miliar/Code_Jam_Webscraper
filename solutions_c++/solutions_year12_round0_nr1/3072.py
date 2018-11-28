#include <iostream>
#include <string.h>
#include <cstdio>
using namespace std;
int main(){
	string decoded = "abcdefghijklmnopqrstuvwxyz";
	string encoded = "ynficwlbkuomxsevzpdrjgthaq";
	string referen = "yhesocvxduiglbkrztnwjpfmaq";
	FILE *ptrin,*ptrout;
	int N;
	ptrin = fopen("5.in","r");
	ptrout = fopen("5.out","w");
	fscanf(ptrin,"%d\n",&N);
	for(int i = 0; i < N;i++){
		char* s1 = new char[110],*s2 = new char[110];
		fgets(s1,110,ptrin);
		printf("%s",s1);
		for(int j = 0; j < strlen(s1);j++){
			if(s1[j] >='a' && s1[j] <= 'z'){
				printf("%d ",s1[j]);
				s2[j] = decoded[ referen[ s1[j] - 97 ] - 97 ];
			}
			else
				s2[j] = s1[j];
		}
		s2[strlen(s1)] = '\0';
		fprintf(ptrout,"Case #%d: %s",i+1,s2);
	}
}