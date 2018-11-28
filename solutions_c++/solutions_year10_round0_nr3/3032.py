// CThemePark.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>

using namespace std;

int CThemeParkSlow( ifstream& inS, ofstream& outS, unsigned uCase);



int main(int argc, char* argv[])
{
	ifstream inS("C-small-attempt3.in");
	ofstream outS("C-small-attempt3.out");

	int iErr = 0;

	unsigned N;
	inS >> N;
	for(unsigned uCase=0 ; uCase < N ; ++uCase){
		cout <<"case:"<<uCase+1<<endl;
		int iInErr = CThemeParkSlow( inS, outS, uCase+1 );
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


int CThemeParkSlow( ifstream& inS, ofstream& outS, unsigned uCase)
{
	__int64 Gi[2000];

	__int64 R,K,N;
	inS >> R >> K >> N;
	for( int i=0 ; i<N ; ++i){
		inS >> Gi[i];
	}

	__int64 start = 0;
	__int64 cntMoney=0;
	__int64 r;
	for( r=0 ; r<R ; ++r ){
		__int64 idx;
		bool bBegin=true;
		__int64 cnt=0;
		for( idx=start; (bBegin ||(idx!= start)) && (cnt+Gi[idx]<=K) ; idx=(idx+1)%N ){
			cnt += Gi[idx];
			bBegin = false;
		}
		cntMoney += cnt;
		start = idx;
	}
	outS << "Case #"<<uCase<<": "<<cntMoney<<endl;
	return 0;
}

