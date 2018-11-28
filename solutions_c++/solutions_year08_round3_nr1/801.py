

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std ;

FILE *in = fopen("A-small.in","r") ;
FILE *out = fopen("A-small.out","w") ;

bool cmp(int a,int b)
{
	return a>b ;
}

int main()
{
	int i,j,k,l,g ;
	vector <int> fre ;
	int N,p,K ;

	fscanf(in,"%d",&N) ;
	for(g=1;g<=N;g++)
	{
		fre.clear() ;
		fscanf(in,"%d%d%d",&p,&K,&l) ;
		for(i=0;i<l;i++)
			fscanf(in,"%d",&j) , fre.push_back( j ) ;
		sort( fre.begin(), fre.end(), cmp ) ;
		l = 0 ;
		k = 1 ;
		i = 0 ;
		while( i < fre.size() ) 
		{
			for(j=0;j<K && i<fre.size();i++,j++)
				l += fre[i]*k ;
			k ++ ;
			if( k > p ) break ;
		}
		if( i >= fre.size() )
			fprintf(out,"Case #%d: %d\n",g,l) ;
		else fprintf(out,"Case #%d: IMPOSSIBLE\n",g) ;
	}
	
	
	return 0 ;
}

