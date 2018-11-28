#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <stdarg.h>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <boost/smart_ptr.hpp>
#include <boost/function.hpp>
//SNAPPER!

int main(int argc, char** argv)
{
	std::ifstream fin("file.txt");
	std::ofstream fout("file2.txt");
	long int T, N, K;
	fin >> T;
	long int ikiUzeriN;
	for(int i=0; i<T; i++)
	{
		fin >> N >> K;
		ikiUzeriN = pow(2.0, N);
		K = K % ikiUzeriN;
		if(K == ikiUzeriN-1)
			fout << "Case #" << i+1 << ": ON" << std::endl;
		else
			fout << "Case #" << i+1 << ": OFF" << std::endl;
	}
	fout.close();
	return 0;
}

