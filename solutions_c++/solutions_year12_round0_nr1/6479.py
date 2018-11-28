// google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include<fstream>
using namespace std;
int main(int argc, char* argv[])
{

	ifstream in;
	in.open("sanwal.in");
	int input;
	in>>input;
	cout<<input<<endl;
//cin.clear();
char cha=cin.get();
	cin.ignore();
  string G;

  //G= new string[12];
 // string temp[10];
int T;
string* S;
T=input;

S= new string[T];

int length;
in.ignore();

for(int mun=0;mun<T;mun++)
{

if(T>30)
{
break;
}
//	cin.ignore();
//cin.clear();
	cout<<mun<<": ";
//in>>G;
	
	getline(in,G);
cout<<G;

	//cin.ignore();

	//

length= G.length();

 for(int i=0;i<length;i++)
 {

	 if(length>100)
	 {
	 break;
	 }

	else  if(G[i]==' ')
	 {
//	 cout<<"Space"<<endl;
	 }

 else if(G[i]=='e')
 {
     G[i]='o'; 
}

 else if(G[i]=='j')
 {
 G[i]='u';
 }

 else if(G[i]=='p')
 {
 G[i]='r';
 }


 else if(G[i]=='m')
 {
 G[i]='l';
 }

 
else  if(G[i]=='y')
 {
 G[i]='a';
 }

 
else  if(G[i]=='s')
 {
 G[i]='n';
 }


 
else  if(G[i]=='l')
 {
 G[i]='g';
 }

 
else  if(G[i]=='j')
 {
 G[i]='u';
 }

 
else  if(G[i]=='y')
 {
 G[i]='a';
 }

 
else  if(G[i]=='c')
 {
 G[i]='e';
 }


else  if(G[i]=='k')
 {
 G[i]='i';
 }


else  if(G[i]=='d')
 {
 G[i]='s';
 }


else  if(G[i]=='x')
 {
 G[i]='m';
 }


else  if(G[i]=='v')
 {
 G[i]='p';
 }


else  if(G[i]=='n')
 {
 G[i]='b';
 }


else  if(G[i]=='r')
 {
 G[i]='t';
 }

else  if(G[i]=='i')
 {
 G[i]='d';
 }

else  if(G[i]=='b')
 {
 G[i]='h';
 }


else  if(G[i]=='t')
 {
 G[i]='w';
 }


else  if(G[i]=='a')
 {
 G[i]='y';
 }


else  if(G[i]=='h')
 {
 G[i]='x';
 }


else  if(G[i]=='w')
 {
 G[i]='f';
 }


else  if(G[i]=='f')
 {
 G[i]='c';
 }


else  if(G[i]=='o')
 {
 G[i]='k';
 }


else  if(G[i]=='u')
 {
 G[i]='j';
 }


else  if(G[i]=='g')
 {
 G[i]='v';
 }


else  if(G[i]=='z')
 {
 G[i]='q';
 }


else  if(G[i]=='q')
 {
 G[i]='z';
 }

 //cout<<G[i]<<" "<<"......."<<endl;

 }
//.............................................................................................


for(int j=0;j<length;j++)
{
//cout<<G[j];
}

cout<<endl;
S[mun].assign(G);


cout<<endl;
}

int faizi=1;

ofstream out;
out.open("g.txt");
//out<<"OUTPUT"<<endl;
for(int k=0;k<T;k++)
{
	if(T>30)
	{
	break;
	}
	if(length>100)
	{
	break;
	}
out<<"Case #"<<faizi<<": "<<S[k]<<endl;
faizi++;

}


//cout<<"google it"<<endl;

//	printf("Hello World!\n");

	return 0;
}

