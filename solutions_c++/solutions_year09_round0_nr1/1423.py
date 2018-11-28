#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
#define LET(x,a) typeof(a)x(a)
#define FOR(i,a,n) for(LET(i,a);i<n;++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define cs c_str()
#define GI ({int t; scanf("%d",&t); t;})
#define EACH(it,v) for(LET(it,v.begin()); it!=v.end(); ++it)
#define dbg(x) (fout << #x << ":" << (x) << "\t")
#define dbge(x) (dbg(x), fout << endl)

ifstream fin("input.txt");
ofstream fout("output.txt");
map<string, int> mp;
vector<string>v;
int L, D, N;
map<string, int> resmap;

int go(string prefix, int pos)
{
	if(pos && !mp.count(prefix))return 0;
	if(resmap.count(prefix))return resmap[prefix];
	
	int &res = resmap[prefix] = 0;
	if(pos == L)return res = mp[prefix];
	
	REP(i, v[pos].sz)
	{
		string str= prefix + string(1,v[pos][i]);
		res += go(str, pos+1);
	}
	
	return res;
}

int main()
{
	mp.clear();	
	fin>>L>>D>>N;
	
	string str="";
	REP(i, D)
	{
		fin>>str;
		string s="";
		REP(i, L){s += str[i]; mp[s]++;}
	}
	
	REP(kase,N)
	{
		v.clear();
		resmap.clear();
		string inp;
		fin>>inp;
		
		int token = 0;
		bool newToken = false;
		string s="";
		REP(i, inp.sz)
		if(inp[i] == '(')newToken = true;
		else
		if(inp[i] == ')')
		{
			v.pb(s);
			s="";
			newToken = false;
		}
		else
		{
			if(newToken)s+= inp[i];
			else
			{
				v.pb(string(1, inp[i]));
			}
		}
				
		int res = go("", 0);
		
		fout<<"Case #"<<(kase+1)<<": "<<res<<endl;
	}
	
	return 0;
}
