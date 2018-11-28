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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

string inName;
string outName;

#define cin fin
#define cout fout

#define pii pair<int,int>
int** alt;
char** Map;
int h, w;
char l;
char dfs(int i, int j)
{
	if(Map[i][j] != 0)
		return Map[i][j];
	pii next(i, j);
	if(i > 0 && alt[i-1][j] < alt[next.first][next.second])
	{
		next.first = i-1;
		next.second = j;
	}
	if(j > 0 && alt[i][j-1] < alt[next.first][next.second])
	{
		next.first = i;
		next.second = j-1;
	}
	if(j < w-1 && alt[i][j+1] < alt[next.first][next.second])
	{
		next.first = i;
		next.second = j+1;
	}
	if(i < h-1 && alt[i+1][j] < alt[next.first][next.second])
	{
		next.first = i+1;
		next.second = j;
	}
	if(next.first == i && next.second == j)
	{
		Map[i][j] = l;
		l++;
	}
	else
		Map[i][j] = dfs(next.first, next.second);
	return Map[i][j];
}

int main()
{
//	inName = "B-small.in";
	inName = "B-large.in";
//	outName = "B-small.out";
	outName = "B-large.out";

	int tc;
	ifstream fin(inName.c_str());
	ofstream fout(outName.c_str());
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		l = 'a';
		cin >> h >> w;
		alt = new int*[h];
		Map = new char*[h];
		for(int i = 0; i < h; i++)
		{
			alt[i] = new int[w];
			Map[i] = new char[w];
			for(int j = 0; j < w; j++)
			{
				cin >> alt[i][j];
				Map[i][j] = 0;
			}
		}
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
				dfs(i, j);
		cout<<"Case #"<<Case+1<<":"<<endl;
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
				cout << Map[i][j] <<' ';
			cout<<endl;
		}

		delete []alt;
		delete []Map;
	}
	fout.close();
	fin.close();

	return 0;
}