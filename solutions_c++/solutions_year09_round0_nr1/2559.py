

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

int L, D, N ;
vector <string> dict ;

int main()
{
	int i, j, k, l, ans ;
	string str ;
	char c ;
	vector <int> count ;
	
	fscanf(in,"%d%d%d\n",&L,&D,&N) ;
	dict.clear() ;
	for(i=0;i<D;i++)
	{
		str = "" ;
		for(j=0;j<L;j++)
			fscanf(in,"%c",&c) , str += c ;
		fscanf(in,"\n") ;
		dict.push_back(str) ;
	}
	count.resize(dict.size()) ;
	
	for(i=0;i<N;i++)
	{
		ans = 0 ;
		str = "" ;
		while(1)
		{
			fscanf(in,"%c",&c) ;
			if( c == '\n' ) break ;
			str += c ;
		}
		
		j = 0 ;
		k = 0 ;
		while( k < str.size() )
		{
			if( str[k] == '(' )
			{
				k ++ ;
				while( str[k] != ')' )
				{
					for(l=0;l<D;l++)
					{
						if( j == 0 && str[k-1] == '(' ) count[l] = 0 ;
						if( str[k] == dict[l][j] ) count[l] ++ ;
						if( j == L-1 && str[k+1] == ')' )
							if( count[l] == L ) ans ++ ;
					}
					k ++ ;
				}
				j ++ ;
				k ++ ;
			}
			else
			{
				for(l=0;l<D;l++)
				{
					if( k == 0 ) count[l] = 0 ;
					if( str[k] == dict[l][j] ) count[l] ++ ;
					if( j == L-1 && count[l] == L ) ans ++ ;
				}
				j ++ ;
				k ++ ;
			}
		}

		fprintf(out,"Case #%d: %d\n",i+1,ans) ;
	}
	
	return 0 ;
}
