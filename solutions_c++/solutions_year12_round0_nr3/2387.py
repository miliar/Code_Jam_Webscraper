#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>


using namespace std;

static int intcmp(const void *p1, const void *p2)
{   
	/* The actual arguments to this function are "pointers to
	   pointers to char", but strcmp(3) arguments are "pointers
	   to char", hence the following cast plus dereference */

	return ((*(int const *) p1) - *((int const*)p2));
}




int main(){

	int case_i ;
	int CasesN;
	
	cin>>CasesN;

	int i,j,k;
	for(case_i=0;case_i<CasesN;case_i++){
		
		int A,B;
		cin>>A>>B;

		int Nrn=0; //Number of recyclable numbers

		int dl,dh,d;
		for(int i=A;i<=B;i++){
			dl = i%10;
			dh = i/10;
			d=dl*100+dh;
			if(d>=A&&d<=B&&d>i){
				Nrn++;
			}
			if(dh<10){
				d=dl*10+dh;
				if(d>=A&&d<=B&&d>i){
					Nrn++;
				}
			}

			dl = i%100;
			dh = i/100;
			d=dl*10+dh;
			if(d>=A&&d<=B&&d>i){
				Nrn++;
			}
		}

		printf("Case #%d: %d\n",case_i+1,Nrn);

	}


	return 0;
}
