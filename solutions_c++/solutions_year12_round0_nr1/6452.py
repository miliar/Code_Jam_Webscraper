#include<iostream.h>
#include<conio.h>
#include<stdio.h>
char hash(char c){
	switch(c){
		case 'a':
			return 'y';
		case 'b':
			return 'h';
		case 'c':
			return 'e';
		case 'd':
			return 's';
		case 'e':
			return 'o';
		case 'f':
			return 'c';
		case 'g':
			return 'v';
		case 'h':
			return 'x';
		case 'i':
			return 'd';
		case 'j':
			return 'u';
		case 'k':
			return 'i';
		case 'l':
			return 'g';
		case 'm':
			return 'l';
		case 'n':
			return 'b';
		case 'o':
			return 'k';
		case 'p':
			return 'r';
		case 'q':
			return 'z';
		case 'r':
			return 't';
		case 's':
			return 'n';
		case 't':
			return 'w';
		case 'u':
			return 'j';
		case 'v':
			return 'p';
		case 'w':
			return 'f';
		case 'x':
			return 'm';
		case 'y':
			return 'a';
		case 'z':
			return 'q';
		default:
			return c;
	}
}
void main(){
	char G[31][255];
	int T,i,j;
	cin>>T;
	if(T<1||T>30){
		cout<<"INVALID INPUT, CHECK NUMBER OF LINES!";
		return;
	}
	for(i=0;i<T;i++)
		gets(G[i]);
	for(i=0;i<T;i++){
		cout<<"Case #"<<i+1<<": ";
		for(j=0;G[i][j]!='\0';j++)
			cout<<hash(G[i][j]);
		cout<<endl;
	}
}