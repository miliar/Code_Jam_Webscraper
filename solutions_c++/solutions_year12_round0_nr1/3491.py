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
	ofstream fout ("salida.out");
	ifstream fin ("small.in");
	int t;
	string aux;
	fin>>t;
	
	map<char,char> mapa;
	mapa['y']='a';
	mapa['n']='b';
	mapa['f']='c';
	mapa['i']='d';
	mapa['c']='e';
	mapa['w']='f';
	mapa['l']='g';
	mapa['b']='h';
	mapa['k']='i';
	mapa['u']='j';
	mapa['o']='k';
	mapa['m']='l';
	mapa['x']='m';
	mapa['s']='n';
	mapa['e']='o';
	mapa['v']='p';
	mapa['z']='q';
	mapa['p']='r';
	mapa['d']='s';
	mapa['r']='t';
	mapa['j']='u';
	mapa['g']='v';
	mapa['t']='w';
	mapa['h']='x';
	mapa['a']='y';
	mapa['q']='z';
	mapa[' ']=' ';
	
	string entro;
	string salio;
	fi(t+1)
		{
		getline(fin,entro);
		salio=entro;
		if(i!=0)
			{
			fj(entro.size())
				{
				salio[j]=mapa[entro[j]];	
				}
			
			//cout<<"Case #"<<i<<": "<<entro<<"\n";
			fout<<"Case #"<<i<<": "<<salio<<"\n";		
			}
		}
	
	
	return 0;
}






















