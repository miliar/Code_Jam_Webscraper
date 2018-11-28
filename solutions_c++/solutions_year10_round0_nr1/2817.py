// code_jam_snapper_chain.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "fstream"
#include "iostream"

using namespace std;

int T;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin;
	int i;
	fin.open ( "A-large.in" );
	fin >> T;

	ofstream fout;
	fout.open ( "out.out" );


	for ( i = 0 ; i < T ; i++ )
	{
		int N;
		long int K;

		fout << "Case #" << i + 1 << ": " ; 

		fin >> N;
		fin >> K;
		long temp;
		temp = 1 << N;


		if ( (K + 1) % temp == 0 )
			fout << "ON" << endl;
		else
			fout << "OFF" << endl;
	}

	cout << endl;

	fin.close();
	fout.close ();

	return 0;
}

