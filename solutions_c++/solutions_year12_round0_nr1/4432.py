#include <iostream>
#include <fstream>
//#include <stdlib.h>
#include <string.h>
using namespace std;

void translate( string & sntnc)
{
	for(int i=0; sntnc[i]!=0; i++)	
	switch (sntnc[i])
		{
			case 'a' : sntnc[i]='y'; break;
			case 'b' : sntnc[i]='h'; break;
			case 'c' : sntnc[i]='e'; break;
			case 'd' : sntnc[i]='s'; break;
			case 'e' : sntnc[i]='o'; break;
			case 'f' : sntnc[i]='c'; break;
			case 'g' : sntnc[i]='v'; break;
			case 'h' : sntnc[i]='x'; break;
			case 'i' : sntnc[i]='d'; break;
			case 'j' : sntnc[i]='u'; break;
			case 'k' : sntnc[i]='i'; break;
			case 'l' : sntnc[i]='g'; break;
			case 'm' : sntnc[i]='l'; break;
			case 'n' : sntnc[i]='b'; break;
			case 'o' : sntnc[i]='k'; break;
			case 'p' : sntnc[i]='r'; break;
			case 'q' : sntnc[i]='z'; break;
			case 'r' : sntnc[i]='t'; break;
			case 's' : sntnc[i]='n'; break;
			case 't' : sntnc[i]='w'; break;
			case 'u' : sntnc[i]='j'; break;
			case 'v' : sntnc[i]='p'; break;
			case 'w' : sntnc[i]='f'; break;
			case 'x' : sntnc[i]='m'; break;
			case 'y' : sntnc[i]='a'; break;
			case 'z' : sntnc[i]='q'; break;
		}
}

int main()
{
	string sntnc;
	short T;
	ifstream fi;
	ofstream fo;
	

	fi.open("A-small-attempt0.in");
	fo.open("A-small-attempt0.out");
	fi>>T;
	getline(fi,sntnc);
	for(int cases=0;cases<T;cases++)
	{
		getline(fi,sntnc);
		translate(sntnc);
		fo<<"Case #"<<cases+1<<": "<<sntnc<<endl;
	}


	fi.close();
	fo.close();
	return 0;
}
