#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>

using namespace std;

int main(int argc, char *argv[])
{
	if ( argc < 2 )
	{
		return -1;
	}

	FILE *fp = fopen(argv[1], "rt");
	if ( NULL == fp )
	{
		cerr << "Fail to open file " << argv[1] << endl;
		return -1;
	}

	int N;
	if ( fscanf(fp, "%d\n", &N) < 1 )
	{
		cerr << "Fail to read N" << endl;
		return -1;
	}

	for ( int i = 0; i < N; ++i )
	{
		int c;
		fscanf(fp, "%d\n", &c);
		vector<int> v1, v2;

		for ( int j = 0; j < c; ++j )
		{
			int v;
			fscanf(fp, "%d", &v);
			v1.push_back(v);
		}

		for ( int j = 0; j < c; ++j )
		{
			int v;
			fscanf(fp, "%d", &v);
			v2.push_back(v);
		}

		assert(v1.size() == v2.size());

		sort(v1.begin(), v1.end());
		int minv = 0;
		for ( size_t k = 0; k < v1.size(); ++k )
		{
			minv += v1.at(k) * v2.at(k);
		}

		while(next_permutation(v1.begin(), v1.end()))
		{
			int val = 0;
			for ( size_t k = 0; k < v1.size(); ++k )
			{
				val += v1.at(k) * v2.at(k);
			}
			minv = min(minv, val);
		}

		cout << "Case #" << i+1 << ": " << minv << endl;

	}

	return 0;
}
