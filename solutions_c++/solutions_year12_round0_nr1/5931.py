#include <cstdio>
#include <iostream>
#include <fstream>
#include <cstring>

int T,k,n,i;
char s[1111];

int main(){
	
	//freopen("input.in","r",stdin);
	//freopen("output.out","w",stdout);
	
	scanf("%d\n", &T);
	
	for (k=1;k<=T;++k){
		
		gets(s);
		n=strlen(s);
		for (i=0;i<n;++i){
			 if (s[i]=='a') {s[i]='y';continue;}
			 if (s[i]=='b') {s[i]='h';continue;}
			 if (s[i]=='c') {s[i]='e';continue;}
			 if (s[i]=='d') {s[i]='s';continue;}
			 if (s[i]=='e') {s[i]='o';continue;}
			 if (s[i]=='f') {s[i]='c';continue;}
			 if (s[i]=='g') {s[i]='v';continue;}
			 if (s[i]=='h') {s[i]='x';continue;}
			 if (s[i]=='i') {s[i]='d';continue;}
			 if (s[i]=='j') {s[i]='u';continue;}
			 if (s[i]=='k') {s[i]='i';continue;}
			 if (s[i]=='l') {s[i]='g';continue;}
			 if (s[i]=='m') {s[i]='l';continue;}
			 if (s[i]=='n') {s[i]='b';continue;}
			 if (s[i]=='o') {s[i]='k';continue;}
			 if (s[i]=='p') {s[i]='r';continue;}
			 if (s[i]=='q') {s[i]='z';continue;}
			 if (s[i]=='r') {s[i]='t';continue;}
			 if (s[i]=='s') {s[i]='n';continue;}
			 if (s[i]=='t') {s[i]='w';continue;}
			 if (s[i]=='u') {s[i]='j';continue;}
			 if (s[i]=='v') {s[i]='p';continue;}
			 if (s[i]=='w') {s[i]='f';continue;}
			 if (s[i]=='y') {s[i]='a';continue;}
			 if (s[i]=='z') {s[i]='q';continue;}
			 if (s[i]=='x') {s[i]='m';continue;}
		}
		
		printf("Case #%d: %s\n",k,s);
	}
	
	return 0;
	
}
			 
		