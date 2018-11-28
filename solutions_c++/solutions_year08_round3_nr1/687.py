#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <iostream>
#include <iomanip>
#include <set>
#include <hash_map>
#include <string>
#include <fstream>

using namespace std;

#define long double LD
#define long long LL

#define Rep(i,n) for (int i = 0; i < n; ++i)

vector<string> Split(const string& line, char delim)
{
	string curStr;
	vector<string> tokens;
	char curChar;

	for(int i = 0; i < (int)line.size(); i++)
	{
		curChar = line[i];
		if(curChar == delim)
		{
			tokens.push_back(curStr);
			curStr.clear();
		}
		else
		{
			curStr += curChar;
		}
	}
	if(!curStr.empty())
		tokens.push_back(curStr);
	return tokens;
}

void one()
{
	freopen("A-small-attempt0.in.txt", "rt", stdin);
	freopen("outOne.txt", "wt", stdout);

	string filename("A-small-attempt0.in.txt");
	ifstream in;
	in.open(filename.c_str());

	int n;
	string first;
	getline(in, first, '\n');
	istringstream f(first);
	f >> n;

	Rep(i, n)
	{
		int perKey;
		int keys;
		int alph;
		string params;
		getline(in, params, '\n');
		vector<string> paramstr = Split(params, ' ');
		istringstream iss1(paramstr[0]);
		iss1 >> perKey;
		istringstream iss2(paramstr[1]);
		iss2 >> keys;
		istringstream iss3(paramstr[2]);
		iss3 >> alph;
		
		string strAlph;
		getline(in, strAlph, '\n');
		vector<string> strs = Split(strAlph, ' ');
		vector<int> freqs;
		Rep(j, strs.size())
		{
			istringstream iss(strs[j]);
			int freq;
			iss >> freq;
			freqs.push_back(freq);
		}

		sort(freqs.rbegin(), freqs.rend());

		vector<vector<int>> vec;

		Rep(j, keys)
		{
			vector<int> sub;
			vec.push_back(sub);
		}

		int index = 0;
		Rep(j, alph)
		{
			if(index >= keys - 1)
				index = 0;
			else
				++index;
			//cout << "\t" << index << endl;
			vec[index].push_back(freqs[j]);
		}

		int sum = 0;

		Rep(j, vec.size())
		{
			Rep(k, vec[j].size())
			{
				sum += vec[j][k] * (k + 1);
			}
		}


		cout << "Case #" << (i + 1) << ": " << sum << endl;
	}

}

/*
void two()
{
	freopen("demo2.txt", "rt", stdin);
	freopen("outOne.txt", "wt", stdout);

	int n;
	scanf("%d", &n);

	Rep(i, n)
	{

	}

}

void three()
{
	freopen("demo3.txt", "rt", stdin);
	freopen("outOne.txt", "wt", stdout);

	int n;
	scanf("%d", &n);

	Rep(i, n)
	{

	}

}
*/
void main()
{
	one();
	return;
}