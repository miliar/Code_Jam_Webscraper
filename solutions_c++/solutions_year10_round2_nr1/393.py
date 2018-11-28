#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <queue>
#include <stack>
#include <iostream>

using namespace std;

//const string PATH = "A-small-attempt0";
const string PATH = "A-large";
//const string PATH = "A";

int add(vector<string> &made, string add)
{
	int ret = 0;
	stringstream cur;
	cur << "/";
	int pos = 1;
	while(pos < add.size())
	{
		if(add[pos] == '/')
		{
			if(find(made.begin(), made.end(), cur.str()) == made.end())
			{
				made.push_back(cur.str());
				ret++;
			}
		}
		cur << add[pos];
		pos++;
	}
	if(find(made.begin(), made.end(), cur.str()) == made.end())
	{
		made.push_back(cur.str());
		ret++;
	}
	return ret;
}

int main()
{
	stringstream inPath;
	inPath << PATH.c_str() << ".in";
	stringstream outPath;
	outPath << PATH.c_str() << ".out";
	ifstream inFile(inPath.str());
	ofstream outFile(outPath.str());
	int T;
	inFile >> T;
	for(int i = 0; i < T; i++)
	{
		int N, M;
		inFile >> N >> M;
		vector<string> made(N);
		string a;
		int ret = 0;
		for(int j = 0; j < N; j++)
		{
			inFile >> made[j];
		}
		for(int j = 0; j < M; j++)
		{
			inFile >> a;
			ret += add(made, a);
		}
		outFile << "Case #" << (i+1) << ": " << ret << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}