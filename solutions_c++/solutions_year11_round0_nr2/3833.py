#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <fstream>
#include <map>

using namespace std;

#define GCJ
#ifdef GCJ
ifstream fin("B-small-attempt0.in");
ofstream fout("B.out");
#define cin	fin
#define cout fout
#endif

string decorate(const string& str);

int main()
{
	int T;
	cin >> T;

	int dict[256] = {0};
	//W, E, R, A, S, D, F
	dict['Q'] = 2;
	dict['W'] = 3;
	dict['E'] = 5;
	dict['R'] = 7;
	dict['A'] = 11;
	dict['S'] = 13;
	dict['D'] = 17;
	dict['F'] = 19;
	for(int t=0; t<T; ++t)
	{
		int combDict[400] = {0};
		char oppDict[256] = {0};
		int cntComb;
		cin >> cntComb;
		while(cntComb--)
		{
			string str;
			cin >> str;
			combDict[dict[str[0]] * dict[str[1]]] = str[2];
		}

		int cntOpp;
		cin >> cntOpp;
		while(cntOpp--)
		{
			string str;
			cin >> str;
			oppDict[str[0]] = str[1];
			oppDict[str[1]] = str[0];
		}
		
		int lenWord;
		cin >> lenWord;
		string word;
		cin >> word;
		string res; res += word[0];
		for(int i=1; i<lenWord; ++i)
		{
			if(res.empty())
			{
				res += word[i];
				continue;
			}
			char lastElem = res[res.size()-1];
			int combHash = dict[lastElem] * dict[word[i]];
			if(combDict[combHash] != 0)
			{
				res[res.size()-1] = combDict[combHash];
				continue;
			}

			char opp = oppDict[word[i]];
			if(opp != 0)
			{
				if(res.find(opp) != string::npos)
					res = "";
				else
					res += word[i];
				continue;
			}

			res += word[i];
		}

		cout << "Case #" << t+1 << ": " << decorate(res) << endl;
	}
	return 0;
}

string decorate(const string& str)
{
	string ret;
	ret += '[';
	if(str.size() > 0)
		ret += str[0];
	for(size_t i=1; i<str.size(); ++i)
	{
		ret += ", ";
		ret += str[i];
	}
	
	ret += ']';
	return ret;
}