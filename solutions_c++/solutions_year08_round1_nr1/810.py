#include <iostream>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iomanip>
#include <math.h>
#include <sstream>
#include <locale>
#include <fstream>
#include <stdio.h>

using namespace std;


vector<int> vx, vy;

int main()
{
	
	string str;
	int T;
	ifstream iFile("A-small-attempt0.in");
	ofstream oFile("small.out");

    int cases = 1;
	iFile >> T;

	for (;cases<=T;cases++)
	{
		int n,i;
		iFile >> n;

		vx.resize(0);
		vy.resize(0);
		
		for (i=0;i<n;i++)
		{
			int x;
			iFile >> x;
			vx.push_back(x);
		}
		for (i=0;i<n;i++)
		{
			int y;
			iFile >> y;
			vy.push_back(y);
		}

		sort(vx.begin(),vx.end());
		sort(vy.begin(),vy.end(),greater<int>());

		int res = 0;
		for (i=0;i<n;i++)
		{
			res+=vx[i]*vy[i];
		}

		oFile << "Case #" << cases << ": " << res << endl;
	}

	

	return 0;
}

