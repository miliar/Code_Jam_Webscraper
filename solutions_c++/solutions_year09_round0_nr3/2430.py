

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

int N ;
string text, str ;
int best[20][500] ;

int solve(int ind, int let)
{
	if( let >= text.size() ) return 1 ;
	if( best[let][ind] != -1 ) return best[let][ind] ;
	int i, ret = 0 ;
	for(i=ind;i<str.size();i++)
	{
		if( str[i] == text[let] )
			ret += solve(i+1, let+1) ;
	}
	
	best[let][ind] = ret ;
	return ret ;
}


int main()
{
	int i, j, k, l ;
	char c ;
	
	text = "welcome to code jam" ;
	fscanf(in,"%d\n",&N) ;
	for(l=0;l<N;l++)
	{
		str = "" ;
		while(1)
		{
			fscanf(in,"%c",&c) ;
			if( c == '\n' ) break ;
			str += c ;
		}
		
		for(i=0;i<20;i++)
			for(j=0;j<str.size();j++)
				best[i][j] = -1 ;
		
		k = solve(0, 0) ;
		k = k % 10000 ;
		
		fprintf(out,"Case #%d: %04d\n",l+1,k) ;
	}
	
	return 0 ;
}
