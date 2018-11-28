// ASnapperChain.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <tchar.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>

using namespace std;

int ASnapperChain( ifstream& inS, ofstream& outS, unsigned uCase);


int main(int argc, char* argv[])
{
	ifstream inS("A-large.in");
	ofstream outS("A-large.out");


	unsigned N;
	inS >> N;
	int iErr = 0;
	for(unsigned uCase=0 ; uCase < N ; ++uCase){
		cout <<"case:"<<uCase+1<<endl;
		int iInErr = ASnapperChain( inS, outS, uCase+1 );
		if( iInErr != 0 ){
			iErr = iInErr;
			cerr << "Something wrong for case "<<uCase+1;
		}
	}
	return iErr;


	outS.close();
	inS.close();

	return iErr;
}

int ASnapperChain( ifstream& inS, ofstream& outS, unsigned uCase)
{
	__int64 N,K;
	inS >> N >> K;
	__int64 div = 2;
	div<<= (N-1);

	if( (1+K) % (div) == 0 )
		outS << "Case #"<<uCase<<": "<<"ON"<<endl;
	else
		outS << "Case #"<<uCase<<": "<<"OFF"<<endl;


	return 0;
}