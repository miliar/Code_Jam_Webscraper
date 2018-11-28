// problema11.cpp : Defines the entry point for the console application.
/*
ID: fersarr1
PROG: ariprog
LANG: C++
*/

//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <sstream>
using namespace std;



#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define fz(a) fr( z, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )


int main()
{
	ofstream fout ("salidita3.out");
	ifstream fin ("input.in");
	int t;
	fin>>t;
	int  a=1111;
	int b=2222;
	double potencia=1;
	int exponenciado,expo2;
	double cantDigitosA;
	double resto;
	double rotado,aChico;
	double debug=1212;
	int RESPUESTA=0;
	int recordar[10],cantRecordada;
	bool yaEstaba;
	bool seguir=true;
	fj(t)
	{
	fin>>a>>b;
	RESPUESTA=0;
	while(a<=b)
		{
		if      (a>9999999) {cantDigitosA=8;}
		else if (a>999999) cantDigitosA=7;
		else if (a>99999) cantDigitosA=6;
		else if (a>9999) cantDigitosA=5;
		else if (a>999) cantDigitosA=4;
		else if (a>99) cantDigitosA=3;
		else if (a>9) cantDigitosA=2;
		potencia=1;
		cantRecordada=0;
		seguir=true;
		while(seguir)
			{
			exponenciado=pow(10.0,potencia);
			resto=a%exponenciado;
			aChico=(a-resto)/exponenciado;
			expo2=cantDigitosA-potencia;
			rotado=resto*pow(10.0,expo2)+aChico;
			//if(a==debug) cout<<"a: "<<a<<" rotado: "<<rotado<<endl;
			//if(a<debug) cout<<"res "<<resto<<" exp "<<exponenciado<<" cantDig "<<cantDigitosA<<" expo2 "<<expo2<<endl;
			if (rotado<=b && a<rotado) 
				{
				yaEstaba=false;
				for(int i=0;i<cantRecordada && !yaEstaba;i++)
					{
					yaEstaba= (recordar[i]==rotado);
					}
				if(!yaEstaba)
					{
					recordar[cantRecordada]=rotado;
					cantRecordada++;
					//if(a==debug)cout<<"***********a y rotado "<<a<<" "<<rotado<<" rota# "<<potencia<<endl<<endl;
					RESPUESTA++;
					}
				}
			seguir=(a/exponenciado!=0); //mientras sea menor
			potencia++;
			}
		a++;
		}
	
	fout<<"Case #"<<j+1<<": "<<RESPUESTA<<endl;
	}
	return 0;
}






















