// dummy.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdlib.h>
#include <fstream>

using namespace std;



void myconversion(char *str)
{
	int uzunluk=0, i;
	char geciciChar;

	while(str[uzunluk]!=0) // str'nin uzunlugunu bul
		uzunluk++;

	uzunluk--;

	for(i=0;i<(uzunluk+1)/2;i++) //str'nin yarisina kadar olan karakterleri, yarýsýndan sonraki karakterlerle degistir
	{
		geciciChar=str[i]; // char'i sakla
		str[i]=str[uzunluk-i]; // sondaki karakteri basa getir
		str[uzunluk-i]=geciciChar; // sakladigin karakteri yerine koy
	}

	return;
}

int main()
{
	
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int ncases=0;

	in >> ncases;

	for(int i=0; i<ncases; i++)
	{
		int n=0,k=0;

		in >> n >> k;


		{
			int necessaryClaps= 1 << n;
			if((k % necessaryClaps)==(necessaryClaps-1))
			{
				out << "Case #" << (i+1) << ": ON\n";
			}
			else
			{
				out << "Case #" << (i+1) << ": OFF\n";
			}
		}
	}
	
	return 0;
}

