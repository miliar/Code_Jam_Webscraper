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

int main()
{
//	inName = "A-small.in";
	inName = "A-large.in";
//	outName = "A-small.out";
	outName = "A-large.out";

	int tc;
	ifstream fin(inName.c_str());
	ofstream fout(outName.c_str());
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int n;
		cin >> n;
		char **matr = new char*[n];
		for(int i = 0; i < n; i++)
		{
			matr[i] = new char[n];
			for(int j = 0; j < n; ++j)
			{
				cin >> matr[i][j];
			}
		}
		int res = 0;
		for(int k = 0 ; k < n; k++)
		{
			for(int i = k; i < n; i++)
			{
				bool good = true;
				for(int j = k+1; j < n; j++)
				{
					if(matr[i][j] == '1')
					{
						good = false;
						break;
					}
				}
				if(good)
				{
					res += i-k;
					char *tmp = matr[i];
					for(int l = i; l > k; --l)
					{
						matr[l] = matr[l-1];
					}
					matr[k] = tmp;
					break;
				}
			}
		}
		cout<<"Case #"<<Case+1<<": "<< res << endl;
	}
	fout.close();
	fin.close();

	return 0;
}