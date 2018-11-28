// A_Speaking_in_Tongues.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;

int GO(  FILE* FIn, FILE* FOut , unsigned uCase);

int Test(int argc, char* argv[]);


int main(int argc, char* argv[])
{
	

	Test(argc,argv);
	
	return 0;
}



char sInFile[FILENAME_MAX] = 
	//"sample.in";
	"C-large.in";
	//"C-large.in";

char sOutFile[FILENAME_MAX] = 
	//"sample.out";
	//"small.out";
	"large.out";


int Test(int argc, char* argv[])
{
	FILE* FIn = fopen(sInFile, "r");
	FILE* FOut = fopen(sOutFile, "w");
	
	if( !FIn ){
		cerr<<"Cannot open input"<<endl;
		return -1;
	}
	if( !FOut ){
		cerr<<"Cannot open output"<<endl;
		fclose( FIn);
		return -1;
	}
	unsigned N;
	fscanf(FIn,"%d\n",&N);
	int iErr = 0;
	for(unsigned uCase=0 ; uCase < N ; ++uCase){
		cout <<"case:"<<uCase+1<<endl;
		int iInErr = GO( FIn, FOut, uCase+1 );
		if( iInErr != 0 ){
			iErr = iInErr;
			cerr << "Something wrong for case "<<uCase+1;
		}
	}

	fclose(FOut);
	fclose(FIn);

	return iErr;
}

#define MAX 2000000
bool nums[MAX+1];

int coupled[10];

int rotate(int n, int exp10_nDig){
	int m = n/10+(n%10)*exp10_nDig;
	return m;
}

int computeExpNDig( int n){
	int i=0;
	for( i=0 ; n ; ++i )
		n/=10;
	return pow((float)10,i-1);
}


int GO(  FILE* FIn, FILE* FOut , unsigned uCase)
{
	int A,B;
	int nRes = 0;

	fscanf(FIn,"%d",&A);
	fscanf(FIn,"%d",&B);
	int exp10_nDig = computeExpNDig(B);
	if( exp10_nDig > 1 ){
		memset(&(nums[A]),false, (B-A+1)*sizeof(bool));

		for( int n=A ; n<=B ; ++n ){
			if( !nums[n] ){
				int m = n;
				nums[n] = true;
				int c = 0;
				int nCoupled = 0;
				while( (m= rotate(m,exp10_nDig)) != n){
					if( m>=A && m<=B ){
						bool bFound = false;
						for( int nc=0 ; nc<nCoupled ; ++nc){
							if( m == coupled[nc] ){
								bFound = true;
								break;
							}
						}
						if( !bFound){
							coupled[nCoupled++] = m;
							nums[m] = true;//m l'ho già analizzato con n
							++c;
						}
					}
				}
				for( int i=1;i<=c ; ++i)
					nRes += i;
			}
		}
	}
	
	fprintf(FOut, "Case #%d: %d\n",uCase, nRes);

	return 0;
}

