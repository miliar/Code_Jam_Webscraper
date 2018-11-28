

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std ;

FILE *in = fopen("A-large.in","r") ;
FILE *out = fopen("A-large.out","w") ;

int N,S,Q ;
vector <string> s,q ;
int best[15][105] ;

string readLine()
{
	string ret ;
	char c ;
	
	ret = "" ;
	while( fscanf(in,"%c",&c) != EOF && c != '\n' ) ret += c ;
	return ret ;
}


int main()
{
	int i,j,k,l,g,u,v ;
	string str ;
	char c ;
	vector <string> hold ;
	
	fscanf(in,"%d",&N) ;
	for(g=1;g<=N;g++)
	{
		fscanf(in,"%d\n",&S) ;
		s.clear() ;
		for(i=0;i<S;i++)
			s.push_back( readLine() ) ;
		fscanf(in,"%d\n",&Q) ;
		q.clear() ;
		for(i=0;i<Q;i++)
			q.push_back( readLine() ) ;

		k = 0 ;
		l = 0 ;
		while( 1 )
		{
			hold.clear() ;
			for(i=l;i<Q;i++)
			{
				for(j=0;j<hold.size();j++)
					if( q[i] == hold[j] ) break ;
				if( j == hold.size() )
					hold.push_back( q[i] ) ;
				if( hold.size() == S ) break ;
			}
			if( hold.size() < S ) break ;
			str = hold[ hold.size()-1 ] ;
			while( str != q[l])
			{
				l ++ ;
				if( l == Q ) break ;
			}
			if( l == Q ) break ;
			k ++ ;
		}
		
		fprintf(out,"Case #%d: %d\n",g,k) ;
	}
	
	
	return 0 ;
}

