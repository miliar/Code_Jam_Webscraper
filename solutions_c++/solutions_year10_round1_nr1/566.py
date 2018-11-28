// A.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>

using namespace std;


int A(  ifstream& inS, ofstream& outS, unsigned uCase);

int main(int argc, char* argv[])
{
	ifstream inS("A-small-attempt0.in");
	ofstream outS("A-small-attempt0.out");
	
	unsigned N;
	inS >> N;
	int iErr = 0;
	for(unsigned uCase=0 ; uCase < N ; ++uCase){
		cout <<"case:"<<uCase+1<<endl;
		int iInErr = A( inS, outS, uCase+1 );
		if( iInErr != 0 ){
			iErr = iInErr;
			cerr << "Something wrong for case "<<uCase+1;
		}
	}

		outS.close();
	inS.close();

	return iErr;

}

int A(  ifstream& inS, ofstream& outS, unsigned uCase)
{
	char table[50][50];

	int N,K;

	inS >> N >> K;
	for(int r=0 ; r<N ; ++r)
		for(int c=0 ; c<N ; ++c)		
			inS >> table[r][c];


	bool R=0;
	bool B=0;

	int iR=0;
	int iB=0;

	for(int r=0 ; r<N ; ++r){
		int nFull=0;
		iR=0;
		iB=0;
		for(int c=N-1 ; c>=0 ; --c){
			if(table[r][c] != '.'){
				table[r][N-1-nFull] = table[r][c];
				if(table[r][N-1-nFull] == 'R'){
					++iR;
					iB=0;
					if(iR >= K)
						R = true;
				}
				else{
					++iB;
					iR=0;
					if(iB >= K)
						B = true;
				}
				++nFull;
			}
		}
		if( R && B )
			break;
		memset(table[r],'.',N-nFull);
	}


	if( !R || !B ){

		for(int c=0 ; c<N ; ++c){
			iR=0;
			iB=0;
			for(int r=N-1 ; r>=0 ; --r){
				if(table[r][c] == 'R'){
					++iR;
					iB=0;
					if(iR >= K)
						R = true;
				}
				else if(table[r][c] == 'B'){
					++iB;
					iR=0;
					if(iB >= K)
						B = true;
				}
				else break;
			}
		}

		if( !R || !B ){
			for(int y=0;y<N+N ; ++y){
				int c,r;
				if(y<N){
					c= N-y;
					r = 0;
				}
				else{
					c = N-1;
					r = y-N;
				}
				iR=0;
				iB=0;
				for( ; c>=0 && r<N ; --c , ++r){
					if(table[r][c] == 'R'){
						++iR;
						iB=0;
						if(iR >= K)
							R = true;
					}
					else  if(table[r][c] == 'B'){
						++iB;
						iR=0;
						if(iB >= K)
							B = true;
					}
					else{
						iR=0;
						iB=0;}
				}
			}
		}

		if( !R || !B ){
			for(int y=0;y<N+N ; ++y){
				int c,r;
				if(y<N){
					c= N-y;
					r = 0;
				}
				else{
					c = N-1;
					r = y-N;
				}
				iR=0;
				iB=0;
				for( ; c>=0 && r>=0 ; --c , --r){
					if(table[r][c] == 'R'){
						++iR;
						iB=0;
						if(iR >= K)
							R = true;
					}
					else  if(table[r][c] == 'B'){
						++iB;
						iR=0;
						if(iB >= K)
							B = true;
					}
					else{
						iR=0;
						iB=0;}
				}
			}
		}

	}
	


	outS << "Case #"<<uCase<<": ";
	if( R && B )
		outS<<"Both"<<endl;
	else if( R && !B )
		outS<<"Red"<<endl;
	else if( !R && B )
		outS<<"Blue"<<endl;
	else
		outS<<"Neither"<<endl;

	return 0;
}


