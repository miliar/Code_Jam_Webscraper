//============================================================================
// Name        : qualification_round.cpp
// Author      : Georget Olivier
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cmath>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main(int argc, char ** argv) {

	ifstream ifs(argv[1]);
	int nbL, i=1;
	ifs >> nbL;
	while(ifs.good() && i <= nbL)
	{
		unsigned long long N, K;
		ifs >> N >> K;

		unsigned long long No = (unsigned long long) pow(2, (long double)N);
		cout << "Case #" << i++ << ": ";
		if( (K+1)%No == 0)
			cout << "ON" << endl;
		else cout << "OFF" << endl;
	}

	return EXIT_SUCCESS;
}
