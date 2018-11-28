#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
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

typedef long long ll;
map<char, int>mp;

int main()
{

  	clock_t start=clock();
	
	int kases; fin>>kases;
	for(int kase = 0; kase<kases;++kase)
	{
		string inp; fin>>inp;
		set<char> s; REP(i, inp.sz)s.insert(inp[i]);
		int base = s.sz;		
		base = min(base, 10);
		base = max(base, 2);
		
		mp.clear();
		
		mp[inp[0]] = 1;
		int cur=0;
		FOR(i,1,inp.sz)
		if(!mp.count(inp[i]))
		{
			mp[inp[i]] = (cur > base ? 0 : cur);
			if(!cur)cur = 2; else cur++;
		}
		
		
		
		ll val = 0;
		ll power = 1;
		for(int i=inp.sz-1; i>=0; --i)
		{
			val += mp[inp[i]] * power;
			power *= base;
		}
		
		fout<<"Case #"<<(kase+1)<<": "<<val<<endl;
	}

	clock_t end=clock();
	cout <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	
	return 0;
}
