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
#define PII pair<int,int>
#define MOD 10000

ifstream fin("input.txt");
ofstream fout("output.txt");

string text;
string pattern = "welcome to code jam";
map<PII, int >mp;


int go(int patpos, int textpos)
{
	if(textpos >= text.sz && patpos != pattern.sz)return 0;
	if(patpos == pattern.sz)return 1;

	if(mp.count(PII(patpos, textpos)))return mp[PII(patpos, textpos)];
	int & res = mp[PII(patpos, textpos)] = 0;	

	FOR(i, textpos, text.sz)
	if(text[i] == pattern[patpos])
	{
		res = (res + go(patpos+1, i+1)) % MOD;
	}
	
	return res;
}

int main()
{
	int N; fin>>N;
	
	int kase = 0;
	char buf[1000];
	while(fin.getline(buf, 1000))
	{
		text = (string)buf;
		if(text.sz==0)continue;
		mp.clear();
		
		sprintf(buf, "%04d", go(0,0));
		fout<<"Case #"<<(++kase)<<": "<<((string)buf)<<endl;
	}
	
	return 0;
}
