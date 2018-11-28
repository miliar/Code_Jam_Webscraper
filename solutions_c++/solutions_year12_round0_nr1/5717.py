#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>

using namespace std;

int main(){
	
	
	char * a;
	a=(char *)malloc(200*sizeof(char));
	char * b;
	b=(char *)malloc(200*sizeof(char));
	int i,j,t;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%c",&a[0]);
		scanf("%[^\n]",a);
		for(j=0;j<strlen(a);j++){
			b[j]=a[j];
			switch(b[j]){
			case 'a':b[j]='y';break;
			case 'b':b[j]='h';break;
			case 'c':b[j]='e';break;
			case 'd':b[j]='s';break;
			case 'e':b[j]='o';break;
			case 'f':b[j]='c';break;
			case 'g':b[j]='v';break;
			case 'h':b[j]='x';break;
			case 'i':b[j]='d';break;
			case 'j':b[j]='u';break;
			case 'k':b[j]='i';break;
			case 'l':b[j]='g';break;
			case 'm':b[j]='l';break;
			case 'n':b[j]='b';break;
			case 'o':b[j]='k';break;
			case 'p':b[j]='r';break;
			case 'q':b[j]='z';break;
			case 'r':b[j]='t';break;
			case 's':b[j]='n';break;
			case 't':b[j]='w';break;
			case 'u':b[j]='j';break;
			case 'v':b[j]='p';break;
			case 'w':b[j]='f';break;
			case 'x':b[j]='m';break;
			case 'y':b[j]='a';break;
			case 'z':b[j]='q';break;		
			}
		}
		b[j]='\0';
		cout<<"Case #"<<i+1<<": "<<b<<endl;
	}
	


return 0;
}
