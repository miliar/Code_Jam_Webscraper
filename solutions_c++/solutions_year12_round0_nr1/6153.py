#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

char abc[] ={	'y'      ,
	'h',
	'e',
	's',
	'o',
	'c',
	'v',
	'x',
	'd',
	'u',
	'i',
	'g',
	'l',
	'b',
	'k',
	'r',
	'z',
	't',
	'n',
	'w',
	'j',
	'p',
	'f',
	'm',
	'a',
	'q'
};

int main(){
int k=1;
    int cases;
    cin>>cases;
    getchar();
    while(cases--){
        int i=0;
        char s[102];
        gets(s);
        while(s[i]){
            if(s[i]!=' ')
            s[i]=abc[s[i]-97];
            else
            s[i]=' ';
            i++;
        }
printf("Case #%d: ",k++);
        puts(s);
    }
}
