#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;


int main()
{
	ifstream input("A-large.in");
	ofstream outputfile("output.txt");
//#define outputfile cout
	int sz ;
	
	input >> sz ;

	for( int casen = 1 ; casen <= sz;  ++casen)
	{
		long long n,k;

		input >> n >> k;
		long long lim = 1 ;
		lim <<= n;
		k %= lim;
		
		outputfile << "Case #" << casen << ": "  ;

		if( k == lim - 1) outputfile << "ON";
		else outputfile << "OFF" ;
		outputfile << endl;
	}
	getchar();
	return 0;
}
