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
#include <set>
#include <functional>
#include <numeric>
#include <limits>

using namespace std;

int main(int argc, char *argv[])
{
	if ( argc < 2 )
	{
		return -1;
	}

	FILE *fp = fopen(argv[1], "rt");
	if ( fp == NULL )
	{
		cerr << "Fail to open file " << argv[1] << endl;
		return -1;
	}

	int N;
	if ( fscanf(fp, "%d\n", &N) < 1 || N <= 0 )
	{
		cerr << "Fail to read N" << endl;
		return -1;
	}

	for ( int i = 0; i < N; ++i )
	{
		int P, K, L;
		fscanf(fp, "%d %d %d\n", &P, &K, &L);
		if ( P * K < L )
		{
			cout << "Case #" << i + 1 << ": Impossible" << endl;
			continue;
		}

		long long ls[1000];
		for ( int j = 0; j < L; ++j )
		{
			fscanf(fp, "%d", ls+j);
		}
		sort(ls, ls + L, greater<long long>());

		long long ret = 0;
		for ( int j = 0; j < L; ++j )
		{
			ret += ls[j] * (j / K + 1);
		}
		cout << "Case #" << i + 1 << ": " << ret << endl;
	}

	return 0;
}
