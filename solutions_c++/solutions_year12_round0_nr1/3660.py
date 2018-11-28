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

using namespace std;




int main( )
{
	
	map<char, char> translate;
	map<char, char>::iterator it;

    translate.insert( pair<char,char>('a','y') );
	translate.insert( pair<char,char>('b','h') );
	translate.insert( pair<char,char>('c','e') );
	translate.insert( pair<char,char>('d','s') );
	translate.insert( pair<char,char>('e','o') );
	translate.insert( pair<char,char>('f','c') );
	translate.insert( pair<char,char>('g','v') );
	translate.insert( pair<char,char>('h','x') );
	translate.insert( pair<char,char>('i','d') );
	translate.insert( pair<char,char>('j','u') );
	translate.insert( pair<char,char>('k','i') );
	translate.insert( pair<char,char>('l','g') );
	translate.insert( pair<char,char>('m','l') );
	translate.insert( pair<char,char>('n','b') );
	translate.insert( pair<char,char>('o','k') );
	translate.insert( pair<char,char>('p','r') );
	translate.insert( pair<char,char>('q','z') );
	translate.insert( pair<char,char>('r','t') );
	translate.insert( pair<char,char>('s','n') );
	translate.insert( pair<char,char>('t','w') );
	translate.insert( pair<char,char>('u','j') );
	translate.insert( pair<char,char>('v','p') );
    translate.insert( pair<char,char>('w','f') );
	translate.insert( pair<char,char>('x','m') );
	translate.insert( pair<char,char>('y','a') );
	translate.insert( pair<char,char>('z','q') );
	translate.insert( pair<char,char>(' ',' ') );

	int t,tt=0;	
	char current;
	FILE * INPUT = NULL;
	INPUT = fopen( "input.txt", "r");
	FILE * OUTPUT = NULL;
	OUTPUT = fopen( "output.txt", "w");

	fscanf(INPUT,"%d\n", &tt);
	for( t = 1; t <= tt;  ++t )
	{
		fprintf(OUTPUT, "Case #%d: ", t);
		current = fgetc(INPUT);
		while(current != '\r' && current != '\n' && current != NULL && !feof(INPUT))
		{
			fprintf(OUTPUT,"%c", translate.find(current)->second);
			current = fgetc(INPUT);
		}
		if(!feof(INPUT))
			fprintf(OUTPUT,"\n");
	}

}
