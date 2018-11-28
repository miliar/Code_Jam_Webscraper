// Task 3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdafx.h"
#include <fstream>
#include <iosfwd>
#include <string>

int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;
	ifstream in;
	ofstream out;
	in.open("C:\\C-small-attempt0.in");
	out.open("C:\\C-small-attempt0.out");

	string empt;

	int n_tests, tests;
	in>>n_tests;
	getline(in, empt);

	int k, n;
	int i, j;
	int count;
	int cur;
	int d;
	int *deck;
	for (tests=0; tests<n_tests; ++tests)
	{
		in>>k;
		getline(in, empt);

		cur = 0;
		count = 0;
		deck = new int[k];
		for (i=0; i<k; ++i)
		{
			deck[i] = 0;
		}
		for (i=1; i<k+1; ++i)
		{
			while (count != i)
			{
				if (deck[cur] == 0)
				{
					++count;
					++cur;
				}
				else
				{
					++cur;
				}
				if (count == i)
				{
					deck[cur-1] = count;
				}
				if (cur == k)
				{
					cur = 0;
				}
			}
			count = 0;
		}
		out<<"Case #"<<tests+1<<": ";

		in>>n;

		for (j=0;j<n;++j)
		{
			in>>d;
			out<<deck[d-1]<<" ";
		}
		getline(in, empt);

		out<<endl;

	}



	in.close();
	out.close();
	return 0;
}

