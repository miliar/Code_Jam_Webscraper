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

	int l, d;
	cin >> l >> d;
	cin>>tc;
	vector< string > dict(d);
	for(int i = 0; i < d; ++i)
	{
		cin >> dict[i];
	}
	sort(dict.begin(), dict.end());
	for(int Case = 0; Case < tc; Case++)
	{
		int cnt = 0;
		string res;
		string patt;
		cin >> patt;
		vector<string> v;
		int i = 0, ind = 0;
		vector<int> indv;
		long long mul = 1;
		while(i < patt.length())
		{
			if(patt[i] == '(')
			{
				i++;
				string str;
				while(patt[i] != ')')
				{
					str.append(1, patt[i]);
					i++;
				}
				sort(str.begin(), str.end());
				for(int j = 1; j < str.length(); j++)
					while(j < str.length() && str[j] == str[j-1])
						str.erase(j-1, 1);
				v.push_back(str);
				mul *= (long long)str.length();
				res.append(1, ' ');
				indv.push_back(ind);
			}
			else
			{
				res.append(1, patt[i]);
			}
			i++;
			ind++;
		}

		for(int i = 0; i < d; i++)
		{
			bool flag = true;
			for(int j = 0; j < dict[i].length() && flag; j++)
			{
				if(res[j] == ' ')
				{
					int k = 0;
					while(indv[k] != j)
						k++;
					flag = false;
					for(int q = 0; q < v[k].length() && !flag; q++)
						if(v[k][q] == dict[i][j])
							flag = true;
				}
				else if(dict[i][j] != res[j])
					flag = false;
			}
			if(flag)
				cnt++;
		}
		cout<<"Case #"<<Case+1<<": "<< cnt << endl;
	}
	fout.close();
	fin.close();

	return 0;
}