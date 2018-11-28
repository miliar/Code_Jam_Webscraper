#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <stack>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int c[1100],n;

int solve()
{
	int sum = 0,i,gumar = 0,minim = c[0];

	for (i = 0 ; i < n; ++i)
	{
		sum = sum ^ c[i];
		if (minim > c[i])
			minim = c[i];
		gumar += c[i];
	}

	if (sum == 0)
		return gumar - minim;
	return -1;
}

int main()
{
	int test,t,i;

	in >> test;

	for (t = 1; t <= test; ++t)
	{
		in >> n;
		for (i = 0 ; i < n; ++i)
			in >> c[i];
		
		int answer = solve();
		
		if (answer == -1)
			out << "Case #" << t << ": NO" << endl;
		else
			out << "Case #" << t << ": " << answer << endl;
	}

	return 0;
}