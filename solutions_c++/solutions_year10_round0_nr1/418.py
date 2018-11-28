#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <fstream>
#include <memory.h>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");	
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		int n, k;
		ifs >> n >> k;
		ofs << "Case #" << test+1 << ": ";
		if (k % (1<<n) == (1<<n)-1)
		{
			ofs << "ON\n";
		}
		else 
		{
			ofs << "OFF\n";
		}
	}
  	return 0;
}
