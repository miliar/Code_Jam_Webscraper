#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int L,D,N;
map<string,int> dic;
vector<string> dicw;
vector<string> chg(string s,int L)
{
	vector<string> ret;
	for(int i = 0; i< s.length(); ++i)
	{
		int j = i;
		if(s[i] == '(') 
		{
			j++;
			while(s[i] != ')') i++;
			ret.push_back(s.substr(j,i-j));
		}
		else 
		{
			ret.push_back(s.substr(i,1));
		}
	}
	return ret;
}

int compete(vector<string> pattern)
{
	int ans = 0;
	bool p[17][128];
	memset(p,0,sizeof(p));
	for(int i = 0; i< pattern.size(); ++i)
	{
		for(int j = 0; j< pattern[i].length(); ++j)
		{
			p[i][pattern[i][j]] = true;
		}
	}
	for(int i = 0; i< D; ++i)
	{
		bool ok = true;
		for(int j = 0; j< L; ++j)
		{
			if(p[j][dicw[i][j]] == false) { ok = false; break;}
		}
		if(ok) ans ++;
	}
	return ans;
}

int main()
{
	
	string str;
	int T = 1;
	while(cin >> L >> D >> N)
	{
		dic.clear();
		for(int i = 0; i< D; ++i) 
		{
			cin >> str;
			dicw.push_back(str);
		}
		vector<string> pattern;
		for(int i = 0; i< N; ++i)
		{
			cin >> str;
			pattern = chg(str,L);
			cout << "Case #" << T++ << ": " << compete(pattern) << endl;
		}
	}
	return 0;
}