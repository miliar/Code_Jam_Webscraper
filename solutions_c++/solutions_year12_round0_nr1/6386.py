#include<iostream>
#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;

char change(char test)
{

switch(test)
{

case 'a': return 'y';
case 'b':return 'h';
case 'c':return 'e';
case 'd':return 's';
case 'e':return 'o';
case 'f':return 'c';
case 'g':return 'v';
case 'h':return 'x';
case 'i':return 'd';
case 'j':return 'u';
case 'k':return 'i';
case 'l':return 'g';
case 'm':return 'l';
case 'n':return 'b';
case 'o':return 'k';
case 'p':return 'r';
case 'q':return 'z';
case 'r':return 't';
case 's':return 'n';
case 't':return 'w';
case 'u':return 'j';
case 'v':return 'p';
case 'w':return 'f';
case 'x':return 'm';
case 'y':return 'a';
case 'z':return 'q';
}



}  


int main()
{



ifstream ifile;
ofstream ofile;
ifile.open("input.in");
ofile.open("output.txt");
char buf;

int t;
while(ifile >> t){

ifile.get(buf);


char stt[10]="Case #";
	
for(int y=0;y<t;y++)
{





ofile<<stt<<y+1<<":"<<" ";
ifile.get(buf);
while(buf!='\n')
{

if(buf==32)
ofile<<buf;

else
{
buf=change(buf);
ofile<<buf;
}

ifile.get(buf);
}

ofile<<"\n";




}




}





}



