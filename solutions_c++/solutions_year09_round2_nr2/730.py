#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
const int SIZE = 100;
char buff[SIZE];
void work();
int main(){
	int cas;
	scanf("%d",&cas);
	int i;
	for (i=1;i<=cas;i++){
		scanf("%s",buff);
		work();
		printf("Case #%d: %s\n",i,buff);
	}
	return 0;
}
void work(){
	char tmp[SIZE];
	strcpy(tmp,buff);
	int len=strlen(tmp);
	if (next_permutation(tmp,tmp+len)){
		strcpy(buff,tmp);
	}else{
		string cmd(tmp);
		cmd="0"+cmd;
		strcpy(tmp,cmd.c_str());
		int i;
		for (i=0;tmp[i];i++){
			if (tmp[i]!='0'){	
				swap(tmp[0],tmp[i]);
				break;
			}
		}
		strcpy(buff,tmp);
	}
}