#include "stdafx.h"
#include "string.h"
#include <cstdio>
#include "fstream"
#include <iostream>
using namespace std ;

//program done with Visual c++ express 2010
//the libraries "stdafx.h" , "targetver.h" and the source file "input.in"
//are in the same folder with the source file "Problem_A_Speaking_in_Tongues.cpp"
//the output file is "output.in"
int main()
{
	char * ligne , *result;
	char test2 [128] ;
	ligne = new char[100] ;
	result = new char[100] ;
	int nbr_ligne ;
	FILE * input, *output ;
 input = fopen ("input.in","r")  ;

fgets(test2 ,sizeof test2 ,input) ;
sscanf(test2 ,"%d" , &nbr_ligne);
ofstream monFlux("output.in");
  
  
   for (int j=0 ; j< nbr_ligne ; j++)
  {
  fgets(test2 ,sizeof test2,input ) ;
  ligne= test2 ;
   
		
	for (int i=0 ;i <strlen(ligne) ; i++)
	{
		switch (*(ligne+ i)) 
		{
			
		case 'a' : *(result +i )= 'y' ;
			break ;
		case 'b' : *(result +i )= 'h' ;
			break ;
		case 'c' : *(result +i )= 'e' ;
			break ;
		case 'd' : *(result +i )= 's' ;
			break ;
		case 'e' : result [i]= 'o' ;
			break ;
		case 'f' : *(result +i )= 'c' ;
			break ;
		case 'g' : *(result +i )= 'v' ;
			break ;
		case 'h' : *(result +i )= 'x' ;
			break ;
		case 'i' : *(result +i )= 'd' ;
			break ;
		case 'j' : *(result +i )= 'u' ;
			break ;
		case 'k' : *(result +i )= 'i' ;
			break ;
		case 'l' : *(result +i )= 'g' ;
			break ;
		case 'm' : *(result +i )= 'l' ;
			break ;
		case 'n' : *(result +i )= 'b' ;
			break ;
		case 'o' : *(result +i )= 'k' ;
			break ;
		case 'p' : *(result +i )= 'r' ;
			break ;
		case 'q' : *(result +i )= 'z' ;
			break ;
		case 'r' : *(result +i )= 't' ;
			break ;
		case 's' : *(result +i )= 'n' ;
			break ;
		case 't' : *(result +i )= 'w' ;
			break ;
		case 'u' : *(result +i )= 'j' ;
			break ;
		case 'v' : *(result +i )= 'p' ;
			break ;
		case 'w' : *(result +i )= 'f' ;
			break ;
		case 'x' : *(result +i )= 'm' ;
			break ;
		case 'y' : *(result +i )= 'a' ;
			break ;
		case 'z' : *(result +i )= 'q' ;
			break ;
		case ' ' : *(result +i )= ' ' ;
			break ;
		default : *(result +i )= ' ' ;
	
		}
	}
	monFlux<< "Case #"<<j+1<<": " ;
	for (int k=0 ;k <strlen(ligne) ; k++)
	{ 
		monFlux << result[k] ;
	}
	monFlux << endl ;
	
	}
	
	return 0 ;
}

