#include<iostream>
#include<stdio.h>
#include<string>
#include <fstream>

using namespace std;

char f(char x){
if(x=='y')return 'a';
if(x=='n')return 'b';
if(x=='f')return 'c';
if(x=='i')return 'd';
if(x=='c')return 'e';
if(x=='w')return 'f';
if(x=='l')return 'g';
if(x=='b')return 'h';
if(x=='k')return 'i';
if(x=='u')return 'j';
if(x=='o')return 'k';
if(x=='m')return 'l';
if(x=='x')return 'm';
if(x=='s')return 'n';
if(x=='e')return 'o';
if(x=='v')return 'p';
if(x=='z')return 'q';
if(x=='p')return 'r';
if(x=='d')return 's';
if(x=='r')return 't';
if(x=='j')return 'u';
if(x=='g')return 'v';
if(x=='t')return 'w';
if(x=='h')return 'x';
if(x=='a')return 'y';
if(x=='q')return 'z';
if(x==' ')return ' ';
}

int main(){
int t,j=1;
string pal="",npal="";
ofstream fout;
ifstream fin;
fout.open ("A-small-attempt0.out", ofstream::out);
fin.open ("A-small-attempt2.in", ifstream::in);
fin>>t;

getline(fin,pal);

while(t--){

getline(fin,pal);
	for(int i=0;i<pal.length();i++){npal=npal+f(pal[i]);}

fout<<"Case #"<<j<<": "<<npal<<endl;
npal="";
j=j+1;
}


}