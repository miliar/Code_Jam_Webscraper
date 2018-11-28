#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <assert.h>

using namespace std;

string calc(int A, int N, int M)
{
	int x1=0, y1=0;
	//for (int x1=0; x1<=N; ++x1)
	//for (int y1=0; y1<=M; ++y1)
		for (int x2=x1; x2<=N; ++x2)
		for (int y2=0; y2<=M; ++y2)
			for (int x3=0; x3<=N; ++x3)
			for (int y3=y1; y3<=M; ++y3)
			{
				if (x1==x2 && y1==y2) continue;
				if (x1==x3 && y1==y3) continue;
				if (x2==x3 && y2==y3) continue;
				int S = abs((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1)); // area * 2
				if (S==A)
				{
					stringstream iss;
					iss << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
					return iss.str();
				}
			}
	return "IMPOSSIBLE";	
}

int main(int argc, char *argv[])
{
	if (argc<2)
	{
		cout << "Filename needed\n";
		return -1;
	}
	fstream fin(argv[1]);
	int numcases;
	fin >> numcases;
	for (int i=0; i<numcases; ++i)
	{
		int A,N,M;
		fin >> N >> M >> A;
		cout << "Case #" << i+1 << ": " << calc(A,N,M) << endl;
	}
	fin.close();
	return 0;
}