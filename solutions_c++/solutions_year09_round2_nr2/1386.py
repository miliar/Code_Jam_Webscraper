
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

int integers[10] ;
int hold[10] ;

string write(int n)
{
	int i,j;
	string str;

	if(n==0) return "0" ;
	str.resize(0);

	while( n!=0 )
	{
		str += (n%10 + '0')  ;
		n /= 10;
	}

	for(i=0,j=str.size()-1;i<str.size()/2;i++,j--)
		swap(str[i],str[j]);

	return str;
}

int main()
{
	int i, j, k, l, g, T ;
	char c ;
	string str ;
	
	fscanf(in,"%d",&T) ;
	for(g=1;g<=T;g++)
	{
		fscanf(in,"%d",&k) ;
		for(i=1;i<=9;i++) integers[i] = 0 ;
		str = write(k) ;
		for(i=0;i<str.size();i++) integers[str[i]-'0'] ++ ;
		while(1)
		{
			k ++ ;
			str = write(k) ;
			for(i=1;i<=9;i++) hold[i] = 0 ;
			for(i=0;i<str.size();i++) hold[str[i]-'0'] ++ ;
			for(i=1;i<=9;i++) if( hold[i] != integers[i] ) break ;
			if( i > 9 ) break ;
		}
		fprintf(out,"Case #%d: %d\n",g,k) ;
	}
	
	
	return 0 ;
}
