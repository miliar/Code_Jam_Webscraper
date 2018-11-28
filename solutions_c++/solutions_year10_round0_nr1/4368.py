/*@JUDGE_ID: ##33 111  C++ "History Grading"*/

/* @BEGIN_OF_SOURCE_CODE */
/*C Headers*/
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<math.h>


/*C++ Headers*/
#include<iostream>
#include<string>
#include<cstdlib>
#include<map>
#include <algorithm>
#include <bitset>

/*Macros*/

/*Definições*/
   
using namespace std;
int test,N,K;
int S, E;



int main() 
{
	int MATCH;
	int ALL_BITS;
	string mystring;
	int Case = 1,aux1,aux2;
	scanf("%d\n",&test);
	
	ALL_BITS = ~0;
	//cout<<ALL_BITS<<endl;

	while(test--)
	{
		scanf("%d %d\n",&N,&K);
		S =0;
		E = 1;
		MATCH = (1<<N) -1;
		for(int i=0; i<K;++i)
		{
			S = (ALL_BITS & S)^( ALL_BITS & E);
			
			for(int j=1; j<N;++j){
				aux1 = (S&E) & 1<<j-1;
				if(aux1)
					E |= 1 << j;
				else
					 E &= ~(1 << j);

			}

		}
		if(MATCH == S)
			printf("Case #%d: ON\n",Case);
		else
			printf("Case #%d: OFF\n",Case);

		Case++;
		
	}
	return 0;
	
}


/* @END_OF_SOURCE_CODE */


/*comentarios:
a)Ao usar scanf e gets..não esquecça de eliminar o \n depois de usar scanf.
b)Presta a atenção em imprimir uma linha a mais no final pode causar WA!!!

*/