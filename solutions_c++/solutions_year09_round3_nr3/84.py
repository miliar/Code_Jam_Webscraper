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

using namespace std;

int readint()
{
  int n;
  cin >> n;
  return n;
}

string readstring()
{
  string s;
  cin >> s;
  return s;
}

string readline()
{
	char buff[1000];
	cin.getline(buff,1000);
	
	if (cin.gcount() < 2)
	{
		cin.getline(buff,1000);
	}
	
	return string(buff);
}

vector<int> rel;

int answers[101][101];

int Calc(int firstC, int lastC, int firstInd, int lastInd)
{
	if (lastInd <= firstInd || lastInd > rel.size())
	{
		return 0;
	}
	
	if (answers[firstInd][lastInd] != -1)
	{
		return answers[firstInd][lastInd];
	}
	
	int bestCost = 1000000000;
	
	for (int i=firstInd; i<lastInd; i++)
	{
		int cost = Calc(firstC, rel[i]-1, firstInd, i) 
					+ lastC-firstC 
					+ Calc(rel[i]+1, lastC, i+1, lastInd);
		
		if (cost < bestCost)
		{
			bestCost = cost;
		}
	}

	answers[firstInd][lastInd] = bestCost;
	
	return bestCost;
}


int main(int argc, char* argv[])
{
	int start = clock();
	
	int T=readint();
	
	for (int test=1; test<=T; test++)
	{
		int P=readint();
		int Q=readint();
		rel.clear();
		memset(answers, -1, sizeof(answers));
		
		for (int i=0; i<Q; i++)
		{
			rel.push_back(readint());
		}
		
		int cost = Calc(1, P, 0, Q);
		
		cerr << "Case #" << test << ": " << cost << endl;
	}
	
	cout << "time used " << float(clock()-start)/CLOCKS_PER_SEC << endl;
}

