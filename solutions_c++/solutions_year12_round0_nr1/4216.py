#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <cmath>
//#include <string.h>
#include <unordered_map>
#include <algorithm>

using namespace std;

void out_me(string in, unordered_map <string, string> &char_map)
{
	cout << char_map[in];
}

void scanner(string in, unordered_map <string, string> &char_map)
{
	int i;
	for(i = 0;i<in.size();i++)
	{
		out_me(in.substr(i,1), char_map);
	}
	cout << endl;
}
/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/
void initMapping(unordered_map <string, string> &char_map)
{
	char_map["a"] = "y";//
	char_map["b"] = "h";//
	char_map["c"] = "e";//
	char_map["d"] = "s";//
	char_map["e"] = "o";//
	char_map["f"] = "c";//
	char_map["g"] = "v";//
	char_map["h"] = "x";//
	char_map["i"] = "d";//
	char_map["j"] = "u";//
	char_map["k"] = "i";//
	char_map["l"] = "g";//
	char_map["m"] = "l";//
	char_map["n"] = "b";//
	char_map["o"] = "k";//
	char_map["p"] = "r";//
	char_map["q"] = "z";//
	char_map["r"] = "t";//
	char_map["s"] = "n";//
	char_map["t"] = "w";//
	char_map["u"] = "j";//
	char_map["v"] = "p";//
	char_map["w"] = "f";//
	char_map["x"] = "m";//
	char_map["y"] = "a";//
	char_map["z"] = "q";//
	char_map[" "] = " ";//
}

int main (int argc, char ** argv)
{
	int count = 1;
	static const char filename[] = "speaking_in_tongues.in";
	unordered_map <string, string> char_map;
	initMapping(char_map);
	FILE *file = fopen ( filename, "r" );
	if ( file != NULL )
	{
		char line [ 2001 ]; /* or other suitable maximum line size */
		fgets ( line, sizeof line, file ); // first line not used
		while ( fgets ( line, sizeof line, file ) != NULL ) /* read a line */
		{
			cout << "Case #" << count << ": "; 
			scanner(line, char_map);
			count++;
		}
		fclose ( file );
	}
	else
	{
		perror ( filename ); /* why didn't the file open? */
	}
	return 0;
}
