#include <iostream>
#include <cstdio>
using namespace std;
char mappings[]=
{
	'y',//a
	'h',//b
	'e',//c
	's',//d
	'o',//e
	'c',//f
	'v',//g
	'x',//h
	'd',//i
	'u',//j
	'i',//k
	'g',//l
	'l',//m
	'b',//n
	'k',//o
	'r',//p
	'z',//q
	't',//r
	'n',//s
	'w',//t
	'j',//u
	'p',//v
	'f',//w
	'm',//x
	'a',//y
	'q'//z
};

int main(int argc, char *argv[]){
	int T;
	cin>>T;
	char temp;
	temp=getchar();
	for(int i=1;i<=T;i++){
		cout<<"Case #"<<i<<": ";
		while(true){
			temp=getchar();
			if(temp=='\n')
				break;
			else if(temp!=' ')
				cout<<mappings[temp-'a'];
			else
				cout<<temp;
		}
		cout<<endl;
	}
	return 0;
}
