
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std ;


FILE *in = fopen("data.in","r") ;
FILE *out = fopen("data.out","w") ;



int main()
{
	int i, j, k, l, g, T;
	char c ;
	string str ;
	vector<char> digists ;
	int minn ;
	
	fscanf(in,"%d\n",&T) ;
	for(g=1;g<=T;g++)
	{
		str = "" ;
		digists.clear() ;
		minn = 1 << 30 ;
		while(1)
		{
			fscanf(in,"%c",&c) ;
			if( c == '\n' ) break ;
			str += c ;
			for(i=0;i<digists.size();i++)
				if( digists[i] == c ) break ;
			if( i == digists.size() ) digists.push_back(c) ;
		}
		l = digists.size() ;
		if( l == 1 )
		{
			c = digists[0] ;
			digists.clear() ;
			digists.push_back(c) ;
			digists.push_back('0') ;
			l = 2 ;
		}
 		swap(digists[0], digists[1]) ;
//		sort(digists.begin(), digists.end()) ;
		
//		do
		{
			k = 0 ;
			for(i=0;i<str.size();i++)
			{
				for(j=0;j<digists.size();j++)
					if( digists[j] == str[i] ) break ;
				if( i == 0 && j == 0 ) break ;
				k += (int)pow(l, str.size()-1-i)*j ;
			}
			if( i == str.size() )
				minn = minn < k ? minn : k ;
		}
//		while( next_permutation(digists.begin(), digists.end()) ) ;
		if( str.size() == 1 ) minn = 1 ;
		fprintf(out, "Case #%d: %d\n",g,minn) ;
	}
	
	
	return 0 ;
}
