// A.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <map>

using namespace std;


#ifndef MAX
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#endif

#ifndef MIN
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#endif

map< pair<int,int>,bool> mapDone;

int C(  ifstream& inS, ofstream& outS, unsigned uCase);

int main(int argc, char* argv[])
{
	ifstream inS("C-small-attempt1.in");
	ofstream outS("C-small-attempt1.out");
	
	unsigned N;
	inS >> N;
	int iErr = 0;
	for(unsigned uCase=0 ; uCase < N ; ++uCase){
		cout <<"case:"<<uCase+1<<endl;
		int iInErr = C( inS, outS, uCase+1 );
		if( iInErr != 0 ){
			iErr = iInErr;
			cerr << "Something wrong for case "<<uCase+1;
		}
	}

	outS.close();
	inS.close();

	return iErr;

}

bool IsWin( int iMax, int iMin );

int C(  ifstream& inS, ofstream& outS, unsigned uCase)
{
		int A1,A2,B1,B2;
	inS >> A1>>A2>>B1>>B2;

	int nWin=0;
	for(int A=A1; A<=A2 ; ++A){
		for(int B=B1; B<=B2 ; ++B){
			if( IsWin( MAX(A,B),MIN(A,B) ) )
				++nWin;
		}
	}

	
	outS << "Case #"<<uCase<<": "<<nWin<<endl;
	return 0;
}


bool IsWin( int iMax, int iMin ){
	if( iMin <=0 )
		return true;

	map< pair<int,int>,bool>::iterator it= mapDone.find( pair<int,int>(iMax,iMin) );
	if( it != mapDone.end() )
		return it->second;

	int iMaxK = iMax/iMin+1;

	for( int k=iMaxK; k>=1 ; --k){
		int v = iMax-k*iMin;
		if( ! ( (v>=iMin && IsWin( v , iMin)) || (v<iMin && IsWin( iMin , v)) ) ){
			mapDone.insert( pair< pair<int,int>,bool>(  pair<int,int>(iMax,iMin) , true )  );
			return true; //L'altro perde
		}
	}
	mapDone.insert( pair< pair<int,int>,bool>(  pair<int,int>(iMax,iMin) , false )  );
	return false; // non riesco a vincere
}
