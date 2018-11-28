// a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream is("A-large.in");
	ofstream os("small.out");
	int T;
	int N;
	is>>T;
	
	for(int i = 0; i < T; i++)
	{
		is>>N;
		int* A = new int[N];
		int* B = new int[N];

		for(int j = 0; j< N; j++)
		{
			is>>A[j]>>B[j];
		}
		
		int a,b;
		int c = 0;
		for(a = 0; a < N - 1; a++)
			for(b = a+1; b < N; b++)
			{
				if((A[a] < A[b] && B[a] < B[b])||(A[a] > A[b] && B[a] > B[b]))
					continue;
				else 
					++c;
			}
		os<<"Case #"<<(i+1)<<": "<<c<<endl;
	}

	is.close();
	os.close();

	
	return 0;
}

