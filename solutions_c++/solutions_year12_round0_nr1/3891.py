#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
char pass[30];
char str[1000];

void init(){
	gets(str);
	return;
}

void process(){
	int len=strlen(str);
	for (int i=0;i<len;i++){
		if ((str[i]>='a')&&(str[i]<='z')){
			str[i]=pass[str[i]-'a'];
		}
	}
	printf("%s\n",str);
	return;
}

int main(){
	pass[0]='y';
	pass[1]='h';
	pass[2]='e';
	pass[3]='s';
	pass[4]='o';
	pass[5]='c';
	pass[6]='v';
	pass[7]='x';
	pass[8]='d';
	pass[9]='u';
	pass[10]='i';
	pass[11]='g';
	pass[12]='l';
	pass[13]='b';
	pass[14]='k';
	pass[15]='r';
	pass[16]='z';
	pass[17]='t';
	pass[18]='n';
	pass[19]='w';
	pass[20]='j';
	pass[21]='p';
	pass[22]='f';
	pass[23]='m';
	pass[24]='a';
	pass[25]='q';
	int tcase;
	scanf("%d",&tcase);
	gets(str);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}
