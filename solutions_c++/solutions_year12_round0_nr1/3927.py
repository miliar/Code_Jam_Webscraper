// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <fstream>


using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

   
   int x;
   string str;
   string*tab;
   fstream plik;
   
   plik.open("A-small-attempt0.in",ios::in);

plik >> x;

if(x>=1 && x<=30) { 

	tab=new string[x];
	getline(plik,str);

for(int z=0; z<x; z++) {

	getline(plik,str);
	int dlugosc=str.size();
	for(int i=0; i<dlugosc; i++) {
		switch(str[i]) {

		case 'a': { str[i]='y'; break; }
	    case 'b': { str[i]='h'; break; }
        case 'c': { str[i]='e'; break; }
		case 'd': { str[i]='s'; break; }
	    case 'e': { str[i]='o'; break; }
        case 'f': { str[i]='c'; break; }
	    case 'g': { str[i]='v'; break; }
	    case 'h': { str[i]='x'; break; }
        case 'i': { str[i]='d'; break; }
		case 'j': { str[i]='u'; break; }
	    case 'k': { str[i]='i'; break; }
        case 'l': { str[i]='g'; break; }
		case 'm': { str[i]='l'; break; }
	    case 'n': { str[i]='b'; break; }
        case 'o': { str[i]='k'; break; }
		case 'p': { str[i]='r'; break; }
		case 'q': { str[i]='z'; break; }
	    case 'r': { str[i]='t'; break; }
		case 's': { str[i]='n'; break; }
	    case 't': { str[i]='w'; break; }
        case 'u': { str[i]='j'; break; }
		case 'v': { str[i]='p'; break; }
        case 'w': { str[i]='f'; break; }
		case 'x': { str[i]='m'; break; }
	    case 'y': { str[i]='a'; break; }
        case 'z': { str[i]='q'; break; }		  
		}
		
	}
	tab[z]=str;
}

plik.close();


plik.open("output.in",ios::out);

for(int i=0; i<x; i++){
plik << "Case #"<<i+1<<": "<<tab[i]<<"\n";
}

delete [] tab;
}
plik.close();



	return 0;
}


