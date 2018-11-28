#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
typedef unsigned long long ll;

#if 0
ll hash(string s)
{
	ll r = 0;
	for(int i=0; i<s.length(); ++i)
		r += s[i]*(31+s[i]);
	return r;
}
#endif

string token(string s, int& off)
{
	string tok;
	if(s.length() <= off) return tok;
	if(s[off] == '/') off++;
	
	int i=off;
	for(; i<s.length(); ++i)
	{
		if(s[i] == '/')
		{
			tok = s.substr(off, i-off);
			off=i+1;
			return tok;
		}
	}
	tok = s.substr(off, s.length()-off);
	off = i;
	return tok;
}

#define MAX_LEVEL 51
#define MAX_DIRS_IN_EACH_LEVEL 101

int main()
{
	ifstream fin("C:\\A-large.in");
	ofstream fout("C:\\large.out");
	int T, nCase=1;
	fin>>T;
	
	while(nCase <= T)
	{
		vector< vector<string> > exist(MAX_LEVEL);
		ll N,M; //total bits, total snaps.
		fin>>N>>M;
		vector<int> v;
		
		//read exisiting dirs
		string s;
		int off=0;
		string dir;
		while(N>0)
		{
			fin>>s;
			off = 0;
			int len = s.length();
			int level = 0;
			string curS;
			while(off < len)
			{
				dir = token(s,off);
				string tH = curS + "#" + dir;
				exist[level].push_back(tH);
				curS = tH;
				++level;
			}
			--N;
		}
		
		ll res = 0;
		while(M>0)
		{
			fin>>s;
			off = 0;
			int len = s.length();
			int level = 0;
			string curH;
			vector<string>::iterator it;
			while(off < len)
			{
				dir = token(s,off);
				string tH = curH + "#" + dir;
				it = find(exist[level].begin(), exist[level].end(), tH);
				if(it == exist[level].end())
				{
					//this dir does not exist. so let's create this dir;
					res ++;  //std::count(s.begin()+off, s.end(), '/')+1;
					exist[level].push_back(tH);
				}
				curH = tH;
				++level;
			}
			--M;
		}
		fout<<"Case #"<<nCase<<": "<<res<<endl;
		++nCase;
	}
	fout<<flush;
	fout.close();
	return 0;
}