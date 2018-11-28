#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int main()
{
	int res = 0;
	fstream fin,fout;
	fin.open("D:\\coding\\codejam2010_round1\\codejam2010_round1\\A-large.in",ios_base::in);
	fout.open("D:\\coding\\codejam2010_round1\\codejam2010_round1\\A-large.out",ios_base::out);
	
	int T;
	fin >> T;
	
	for (int caseId = 0; caseId < T; caseId++)
	{
		int intersects = 0;
		int N;
		fin >> N;
		vector<int> v1,v2;
		for (int i = 0; i < N; i++)
		{
			int x,y;
			fin >> x >> y;
			v1.push_back(x);
			v2.push_back(y);
			//fin >> v1[i] >> v2[i];
		}

		for (int i = 0; i < N; i++)
		{
			int x1 = v1[i];
			int y1 = v2[i];
			for (int j = 0; j < N; j++)
			{
				if ((x1 < v1[j] && y1 > v2[j]) || (x1 > v1[j] && y1 < v2[j]))
				{
					intersects++;
				}
			}
		}
		fout << "Case #" << caseId+1 << ": " << intersects/2 << endl;
	}
	
	fin.close();
	fout.close();
	return res;
}