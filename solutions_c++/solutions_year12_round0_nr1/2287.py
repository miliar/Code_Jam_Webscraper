#include<iostream>
#include<stdio.h>
#include<fstream>
#include<string>

using namespace std;


int main(int argc , char * argv[]){
	char code[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t,i=1;
	ifstream fin;
	fin.open(argv[1]);
	cin>>t;
	cin.get();
	while(t-->0){
		char str[105];
		fflush(stdin);
		cin.clear();
		//cin.getline(str,101,'\n');
		//fflush(stdin);
		cin.getline(str,101);
		printf("Case #%d: ",i);
		int j=0;
		while(str[j]!='\0'){
			if(str[j]==' ')
				printf(" ");
			else {
				printf("%c",code[str[j]-97]);
			}
			++j;
		}
		printf("\n");
		++i;
	}
}