#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
string arr;
int main(){
int i,t,l=1;
cin>>t;
cin.ignore();
while(l<=t){
getline(cin,arr);
printf("Case #%d: ",l);
	for(i=0;arr[i]!='\0';i++){
		switch(arr[i]){
			case 'a':printf("y");break;
			case 'b':printf("h");break;
			case 'c':printf("e");break;
			case 'd':printf("s");break;
			case 'e':printf("o");break;
			case 'f':printf("c");break;
			case 'g':printf("v");break;
			case 'h':printf("x");break;
			case 'i':printf("d");break;
			case 'j':printf("u");break;
			case 'k':printf("i");break;
			case 'l':printf("g");break;
			case 'm':printf("l");break;
			case 'n':printf("b");break;
			case 'o':printf("k");break;
			case 'p':printf("r");break;
			case 'q':printf("z");break;
			case 'r':printf("t");break;
			case 's':printf("n");break;
			case 't':printf("w");break;
			case 'u':printf("j");break;
			case 'v':printf("p");break;
			case 'w':printf("f");break;
			case 'x':printf("m");break;
			case 'y':printf("a");break;
			case 'z':printf("q");break;
			default:printf(" ");
			}
	}
	printf("\n");
	l++;
}
return 0;
}
