#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define MAX_SIZE 3

int xlist[MAX_SIZE],ylist[MAX_SIZE],rlist[MAX_SIZE];

double cal(int a,int b1,int b2)
{
	double r = sqrt((double) ((xlist[b1] - xlist[b2]) * (xlist[b1] - xlist[b2]) + (ylist[b1] - ylist[b2]) * (ylist[b1] - ylist[b2])));
	r += (double) rlist[b1];
	r += (double) rlist[b2];
	r /= 2.0;

	if (r > ((double) rlist[a]))
	{
		return r;
	}
	return ((double) rlist[a]);
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int C;
	fin >> C;

	for (int ni = 1; ni <= C; ni++)
	{
		int n;
		fin >> n;

		for (int i = 0; i < n; i++)
		{
			fin >> xlist[i];
			fin >> ylist[i];
			fin >> rlist[i];
		}

		double ret = 1.0;

		if (n == 3)
		{
			ret = cal(0,1,2);
			double temp = cal(1,0,2);
			if (temp < ret)
			{
				ret = temp;
			}

			temp = cal(2,0,1);
			if (temp < ret)
			{
				ret = temp;
			}
		}
		else if (n == 2)
		{
			ret = (double) rlist[0];
			if (rlist[1] > rlist[0])
			{
				ret = (double) rlist[1];
			}
		}
		else if (n == 1)
		{
			ret = (double) rlist[0];
		}

		fout << "Case #" << ni << ": " << ret << endl;
	}

	fout.close();
	fin.close();

	return 0;
}