#include<cstdio>
#include<string>
#include<iostream>
#include<cstdlib>

using namespace std;

inline char zamien(char a){
	if(a=='e') return 'o';
	if(a=='j') return 'u';
	if(a=='p') return 'r';
	if(a=='m') return 'l';
	if(a=='y') return 'a';
	if(a=='s') return 'n';
	if(a=='l') return 'g';
	if(a=='c') return 'e';
	if(a=='k') return 'i';
	if(a=='d') return 's';
	if(a=='x') return 'm';
	if(a=='v') return 'p';
	if(a=='n') return 'b';
	if(a=='r') return 't';
	if(a=='i') return 'd';
	if(a=='b') return 'h';
	if(a=='t') return 'w';
	if(a=='h') return 'x';
	if(a=='w') return 'f';
	if(a=='a') return 'y';
	if(a=='g') return 'v';
	if(a=='u') return 'j';
	if(a=='f') return 'c';
	if(a=='o') return 'k';
	if(a=='q') return 'z';
	if(a=='z') return 'q';
	else return ' ';
}

int t;
char s[120];
char tmp;

int main(){
	cin>>t;
	for(int i=0;i<=t;i++){
		//printf("*wypisuje kejsa*");
		if(i!=0)cout<<"Case #"<<i<<": ";
		//printf("*czytam*");
		cin.getline(s,119);
		int j=0;
		//printf("*zaczynam wypisywanie*");
		while(s[j]!=0){
			cout<<zamien(s[j]);
			j++;
		}
		//printf("*znak nowej linii*");
		if(i!=0)cout<<endl;
	}
	return 0;
}
