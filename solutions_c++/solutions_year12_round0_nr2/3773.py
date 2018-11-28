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
   int**tab;
   fstream plik;
   int n;
  

   plik.open("B-large.in",ios::in);

plik >> x;

if(x>=1 && x<=100) { 

	tab=new int*[x];
	getline(plik,str);

for(int z=0; z<x; z++) {
	
	plik>>n;
	tab[z]=new int[3+n];
	tab[z][0]=n;
	plik>>tab[z][1];
	int s=tab[z][1];
	plik>>tab[z][2];
	int p=tab[z][2];

	
	for(int i=3; i<n+3; i++) {
	plik>>tab[z][i];
	}

	for(int i=3; i<n+3; i++){
	int g=tab[z][i]/3;

	if(tab[z][i]==0) { if (tab[z][i]==p) { tab[z][i]=-1; } }
	else if(tab[z][i]%3==0) {
		if(g>=p) {tab[z][i]=-1;}
		else if(g+1>=p && s>0) {tab[z][i]=-1; s--;}
	} else if(tab[z][i]%3==1) {
		if(g+1>=p){ tab[z][i]=-1; }
    } else if(tab[z][i]%3==2) {
		if(g+1>=p){tab[z][i]=-1;}
		else if(g+2>=p && s>0) {tab[z][i]=-1; s--;}
		} 
	


	}//for
	cout << endl;
	getline(plik,str);	

	}//for


plik.close();


plik.open("output1.in",ios::out);


int suma=0;
for(int i=0; i<x; i++){
	for(int h=3;h<tab[i][0]+3;h++) {
		if(tab[i][h]==-1) suma++;
		}
plik << "Case #"<<i+1<<": "<<suma<<"\n";
suma=0;
}

delete [] tab;
}
plik.close();


	return 0;
}


