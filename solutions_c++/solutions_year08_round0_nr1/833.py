#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <string>
using namespace std;

#define DIST(x1, y1, x2, y2) (float)((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
#define SORT(x) sort(x.begin(),x.end());

ifstream fin("d:\\gcj\\q.in");
ofstream fout("d:\\gcj\\sol.out");
#define cin fin
#define cout fout

// Walk through the query list till all the search engines 
// have been hit. Increment hit count and perform the same on the
// same operation on the rest of the string.
char buf[101];

vector<string> searchEngines;
map<string, int> srchEngMap;

void clearmap()
{
	for(int i=0;i<searchEngines.size();++i)
		srchEngMap[searchEngines[i]]=0;
}

void Solution()
{
	searchEngines.clear();
	srchEngMap.clear();

	int S = 0;
	cin >> S;
	cin.getline(buf,100);
	for(int i=0;i<S;++i)
	{
		cin.getline(buf, 100);
		searchEngines.push_back(string(buf));
		srchEngMap[searchEngines[i]]=0;	
	}

	int Q = 0;
	cin >> Q;
	cin.getline(buf,100);

	int num=0;
	int numFound=0;
	for(int j=0; j<Q; ++j)
	{
		cin.getline(buf, 100);
		string tmp(buf);
		
		if(srchEngMap[tmp]==0)
		{
			++numFound;
			srchEngMap[tmp]++;
			if(numFound == S)
			{				
				++num;
				clearmap();
				numFound = 1;
				srchEngMap[tmp]++;
			}			
		}
	}

	cout << num;
}

int main(int argc, TCHAR* argv[])
{
    int N = 0;
	cin >> N;

	vector<float> len(3,0);
	
	for(int i=0;i<N;++i)
	{
		cout << "Case #" << i+1 << ": ";
		Solution();
		cout << endl;
	}

	return 0;
}
