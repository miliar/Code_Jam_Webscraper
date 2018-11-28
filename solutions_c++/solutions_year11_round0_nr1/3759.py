/**#include<iostream>
#include <stdlib.h>
#include"string.h"
using namespace std;

int main(){
	char str[]="4 O 2 B 1 B 2 O 4 ";
	char * p; 
	const char* split=" ";
	p = strtok (str,split); 

	int bnum=0;
	int ob[100];int ostate=0;int opos=0;
	int bb[100];int bstate=0;int bpos=0;
	int allflag=0;string order[100];
	memset(ob,0,100);memset(bb,0,100);memset(order,"",100);
	int osiz=0;
	while(p!=NULL) {
		if(allflag==0){
			bnum=atoi(p);
			allflag=1;
			p = strtok(NULL,split);
			continue;
		}
		if(strcmp(p,"B")==0){
			order[osize]="B"
			osize++;
			p = strtok(NULL,split);
			bb[atoi(p)]=1;
			p = strtok(NULL,split);
			continue;
		}
		if(strcmp(p,"O")==0){
			order[osize]="O";
			osize++;
			p = strtok(NULL,split);
			ob[atoi(p)]=1;
			p = strtok(NULL,split);
		}
	}
	int time=0;
	
	


}**/