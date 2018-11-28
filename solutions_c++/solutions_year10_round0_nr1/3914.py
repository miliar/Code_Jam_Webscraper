// GCL.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"

/*
int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}

*/

#include <iostream>
#include <fstream>

using namespace std;

bool check_status( int n , int k )
{
	int pos = 1 << n;
	if( k % pos == pos - 1 ){
		return true;
	} else {
		return false;
	}
}

void main()
{
	int t,n, k, i=1;
	bool status;
	ifstream in("A-large.in");
	ofstream out("out.txt");

	in >> t;

	while( t-- )
	{
		in >> n >> k;
		//cout << "out " << n << k << "\n";
		out << "Case #" << i << ": " ;
		status = check_status(n, k );
		if( status ){
			out << "ON\n";
		} else {
			out << "OFF\n";
		}

		++i;
	}
}


	/*
	vector<bool> a;
	for( int i = 0; i < n; ++i ){
		a.push_back(0);
	}

	int pos;
	for( int i = 0; i < k; ++i ){
		pos = 0;
		for( int j = 0; j < n ; ++j ){
			if( a[j] == 0 ){
				pos = j + 1;
				break;
			}
		}

		if( pos == 0 ){
			pos = n;
		}
		
		for( int j = 0; j < pos; ++j ){
			a[j] = !a[j];
		}
	}

	for( int i = 0; i < n; ++i ){
		if( a[i] == 0 ){
			return false;
		}
	}

	return true;*/