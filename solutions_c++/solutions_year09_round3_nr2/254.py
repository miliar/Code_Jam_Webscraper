
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int T;
void solve()
{
}

void test()
{
	solve();
}

int main()
{
	test();
	ifstream f("");
	ofstream of("output.out");

	f >> T;
	for (int i = 0; i < T; i++)
	{
		solve();
		of << "Case #" << i+1 << ": ";
	}
}
