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
		string str;
		cin >> str;
		int n = str.length();
		int ii = -1;
		char r;
		for(int i = n-1; i > 0; i--)
		{
			if(str[i-1] < str[i])
			{
				ii = i-1;
				r = str[i-1];
				break;
			}
		}
		if(ii == -1)
		{
			str.insert(str.begin(), '0');
			ii = 0;
			r = '0';
		}
		else
		{
			;
		}
		string::iterator it = str.begin() + ii + 1;
		sort(it, str.end());
		for(int i = ii+1; i < str.length(); i++)
			if(str[i] > r)
			{
				char t = str[i];
				str.erase(i, 1);
				str.insert(ii, 1, t);
				break;
			}
		it = str.begin() + ii + 1;
		sort(it, str.end());
		cout<<"Case #"<<Case+1<<": "<< str << endl;
	}
	fout.close();
	fin.close();

	return 0;
}