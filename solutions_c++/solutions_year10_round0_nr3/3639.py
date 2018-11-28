// ThemePark.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <queue>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile;
	ofstream outfile;

	infile.open("input.txt", ios::in);
	outfile.open("output.txt", ios::out);

	if(!infile || !outfile)
		return 0;

	int T;
	infile >> T;

	int count = 1;

	while(T)
	{

		unsigned long long R;
		unsigned long long k;
		int N;

		infile >> R >> k >> N;

		queue<unsigned long long> q;
		unsigned long long g;

		while(N)
		{
			infile >> g;
			q.push(g);
			--N;
		}

		unsigned long cash = 0;
		unsigned long long size = 0;
		unsigned long long grp = 0;

		queue<unsigned long long> qw;

		while(R)
		{
			while(!q.empty())
			{
				grp = q.front();
				if((grp + size) > k)
					break;

				q.pop();
				qw.push(grp);

				size += grp;
			}

			while(!qw.empty())
			{
				q.push(qw.front());
				qw.pop();
			}

			cash += size;
			size = 0;
			--R;
		}

		outfile << "Case #" << count << ": " << cash << "\n";

		++count;
		--T;
	}

	infile.close();
	outfile.close();
}


