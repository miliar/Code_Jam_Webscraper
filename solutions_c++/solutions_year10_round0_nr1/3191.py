// codeJam.cpp : Defines the entry pounsigned int for the console application.
//

#include "stdafx.h"
#include <iostream>

using std::cout;
using std::cin;	
using std::endl;


int _tmain(int argc, _TCHAR* argv[])
{
	int T,N;
	long K, mask = 0;
	cin>>T;
	for ( int i = 0; i < T; i++) 
	{
		cin>>N>>K;
		mask = 2;
		for ( int j = N; j>1 ; j--) 
			mask *= 2;
		mask--;
		if ( (mask -1) > K ) {
			cout<<"Case #"<<(1+i)<<": OFF"<<endl;
			continue;
		}
		if ( (K & mask) == mask )
			cout<<"Case #"<<(1+i)<<": ON"<<endl; 
		else
			cout<<"Case #"<<(1+i)<<": OFF"<<endl;
	}
	return 0;
}

