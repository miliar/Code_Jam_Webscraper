#include<stdio.h>
#include<iostream>
#include<string>
#include<map>

using namespace std;

map<char, char> mp;

void declare(){
	mp['a'] = 'y';
	mp['b'] = 'h';
	mp['c'] = 'e';
	mp['d'] = 's';
	mp['e'] = 'o';
	mp['f'] = 'c';
	mp['g'] = 'v';
	mp['h'] = 'x';
	mp['i'] = 'd';
	mp['j'] = 'u';
	mp['k'] = 'i';
	mp['l'] = 'g';
	mp['m'] = 'l';
	mp['n'] = 'b';
	mp['o'] = 'k';
	mp['p'] = 'r';
	mp['q'] = 'z';
	mp['r'] = 't';
	mp['s'] = 'n';
	mp['t'] = 'w';
	mp['u'] = 'j';
	mp['v'] = 'p';
	mp['w'] = 'f';
	mp['x'] = 'm';
	mp['y'] = 'a';
	mp['z'] = 'q';
}


char* modify( char* str){
	char* p = str;
	while( *p !='\0'){
		*p = mp[*p];
		p++;
	}
	return str;
}
int main(){
	declare();
	int i,j,k,t;
	scanf("%d",&t);
	char str[1000];
	char ch;
 	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		while(1){
			
			scanf("%s",str);
			printf("%s",modify(str));
			ch = getchar();
			printf("%c",ch);
			if( ch == '\n') break;
		}
	}
	return 0;
}
