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



char trans['z'-'a'+1] ={0};

int main(int argc, char* argv[])
{
	

	Test(argc,argv);
	
	return 0;
}



char sInFile[FILENAME_MAX] = 
	//"sample.in";
	"B-small-attempt5.in";

char sOutFile[FILENAME_MAX] = 
	//"sample.out";
	"B-small.out";

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

int __cdecl intcmp(const void*p1, const void*p2){
	return ((int)(*(int*)p1))-(int)(*(int*)p2);
}

int GO(  FILE* FIn, FILE* FOut , unsigned uCase)
{
	int N,S,p;

	fscanf(FIn,"%d",&N);
	fscanf(FIn,"%d",&S);
	fscanf(FIn,"%d",&p);
	int *t = new int[N];
	for( int i=0 ; i<N ; ++i)
		fscanf(FIn,"%d",&(t[i]));

	qsort(t, N, sizeof(int),intcmp);

	int sure = p*3-2;
	
	int sx=0;
	int dx=N-1;
	int c = sx+dx/2;
	while( sx < dx ){
		int c = (sx+dx)/2;
		if( t[c] == sure )
			break;
		else if( t[c] > sure ){
			dx = c-1;
		}
		else 
			sx = c+1;
	}

	if( c<N-1 && t[c] < sure )
		++c;
	while( c>=0 && t[c] >= sure ){
		--c;
	}

	int nSures = N-(c+1); //Questi sono certi
	
	int nS = 0;
	for( int i = c ; i>=0 && nS<S ;--i){
		if( t[i]>=sure-2 && t[i]>=p){
			++nSures;
			++nS;
		}
	}


	
	fprintf(FOut, "Case #%d: %d\n",uCase, nSures);

	delete[] t;
	return 0;
}


