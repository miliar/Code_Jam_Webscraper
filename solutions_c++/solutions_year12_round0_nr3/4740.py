#include "stdafx.h"
#include <sstream>
#include <string.h>
#include "fstream"
#include "iostream"
using namespace std ;


//program done with Visual c++ express 2010
//the libraries "stdafx.h" , "targetver.h" and the source file "input.in"
//are in the same folder with the source file "Problem_C_Recycled_Numbers.cpp"
//the output file is "output.in"
int main()
{
	char test2 [128] ;
	int nbr_ligne ;
	FILE * input, *output ;
	input = fopen ("input.in","r")  ;
	fgets(test2 ,sizeof test2 ,input) ;
	sscanf(test2 ,"%d" , &nbr_ligne);
	ofstream monFlux("output.in");
	int A ,B ,result(0), x, aux ,y ,a , aux3, aux4 ,aux5;
	char conv_A[20] ;
	for (int j=0; j<nbr_ligne ;j++ )
	{
		result = 0 ;
		fgets(test2 ,sizeof test2 ,input) ;
		sscanf(test2 ,"%d %d" , &A, &B);
		for (int i= A ; i<B; i++ )
			{
				itoa(i,conv_A,10 ) ;
				x = i ;
				y =B ;
				a =strlen(conv_A) ;
				aux =i ;
				if (a==3)
				{aux3 = (aux /10 + 100*(aux %10)) ;
				if ((aux3> x ) &&(aux3<= y))
				result += 1 ;
				
				
					aux5 = ((aux %100)*10 +aux /100) ;
				if ((aux5>x) && (aux5<= y)&&(aux5 != aux3))
				result += 1 ;
				
				
				}
				else if (a == 2)
				{aux4 = ((aux %10)*10 + aux /10 ) ;
					if ((aux4>x ) &&(aux4<= y ))
						result += 1 ;}
	
				
	}
	monFlux<< "Case #"<<j+1<<": " ;
	monFlux << result<< endl ;
	}
return 0;}

