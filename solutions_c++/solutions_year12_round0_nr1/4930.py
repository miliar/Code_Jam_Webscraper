#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <functional>
#include <cstdlib>
#include <iostream>
#include <map>

using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int cases;
	map<char, char> mymap;
	typedef pair <char, char> Char_Pair;

	// a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z

	mymap.insert( Char_Pair ('a', 'y') );
	mymap.insert( Char_Pair ('b', 'h') );
	mymap.insert( Char_Pair ('c', 'e') );
	mymap.insert( Char_Pair ('d', 's') );
	mymap.insert( Char_Pair ('e', 'o') );	//
	mymap.insert( Char_Pair ('f', 'c') );
	mymap.insert( Char_Pair ('g', 'v') );
	mymap.insert( Char_Pair ('h', 'x') );
	mymap.insert( Char_Pair ('i', 'd') );
	mymap.insert( Char_Pair ('j', 'u') );
	mymap.insert( Char_Pair ('k', 'i') );
	mymap.insert( Char_Pair ('l', 'g') );
	mymap.insert( Char_Pair ('m', 'l') );
	mymap.insert( Char_Pair ('n', 'b') );
	mymap.insert( Char_Pair ('o', 'k') );
	mymap.insert( Char_Pair ('p', 'r') );
	mymap.insert( Char_Pair ('y', 'a') );	//
	mymap.insert( Char_Pair ('r', 't') );
	mymap.insert( Char_Pair ('s', 'n') );
	mymap.insert( Char_Pair ('t', 'w') );
	mymap.insert( Char_Pair ('u', 'j') );
	mymap.insert( Char_Pair ('v', 'p') );
	mymap.insert( Char_Pair ('w', 'f') );
	mymap.insert( Char_Pair ('x', 'm') );
	mymap.insert( Char_Pair ('q', 'z') );	//
	mymap.insert( Char_Pair ('z', 'q') );	

	mymap.insert( Char_Pair (' ', ' ') );
	mymap.insert( Char_Pair ('\n', '\0') );
	mymap.insert( Char_Pair ('\r', '\0') );
	mymap.insert( Char_Pair ('\0x10', '\0') );
	mymap.insert( Char_Pair ('\0x13', '\0') );

	scanf("%d", &cases);
	char* G = (char *)malloc( 110 );
	fgets( G, 110, stdin );
	
	for (int i = 1; i <= cases; i++)
	{
		char* G = (char *)malloc( 110 );

		if( fgets( G, 110, stdin ) == NULL)
		{
           printf( "fgets error\n" );
		   continue;
		}
        
		for (int i=0; i < strlen(G); i++)
		{
			if (mymap.find(G[i]) != mymap.end() )
				G[i] = mymap[G[i]];
			else
				G[i] = '\0';
		}

		cout << "Case #" << i << ": " << G << endl;
		free(G);
	}

	return 0;
}