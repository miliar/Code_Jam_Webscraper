#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <cstring>
#include <complex>
#include <numeric>
#include <functional>
//#define NDEBUG
#include <assert.h>
using namespace std;
#ifndef NDEBUG
    #define debug(x) cerr<<#x<<"=\""<<x<<"\""<<" at line#"<<__LINE__<<endl;
    #define hline() cerr<<"-----------------------------------------"<<endl;
#else
    #define debug(x)
    #define hline()
#endif
typedef long long int llint;
#define low(x) ((((x)^((x)-1))&x))
#define two(x)  ((1)<<(x))
#define PB(x) push_back((x))
#define SORT(x) sort(x.begin(),x.end())
const int dir[][2]={{-1,0},{0,1},{1,0},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
const char dname[]="NWSE";

vector<int> parse_pattern(string ss)
{
	vector<int> res;
	for(int i=0;i<ss.length();i++)
	{
		if(ss[i]!='(')res.push_back(two(ss[i]-'a'));
		else
		{
			int mk=0;
			for(i++;ss[i]!=')';i++)
				mk|=two(ss[i]-'a');
			res.push_back(mk);
		}
	}
	return res;
}

int main()
{
	int L,D,N;
	cin>>L>>D>>N;
	vector<string> word(D);
	for(int i=0;i<D;i++)cin>>word[i];
	for(int ca=1;ca<=N;ca++)
	{
		string pp;
		cin>>pp;
		vector<int> pset=parse_pattern(pp);
		assert(pset.size()==L);
		int ans=0;
		for(int i=0;i<D;i++)
		{
			bool ok=true;
			for(int j=0;j<L;j++)
				if(0==(pset[j]&two(word[i][j]-'a')))ok=false;
			if(ok)ans++;
		}
		cout<<"Case #"<<ca<<": "<<ans<<endl;
	}
	return 0;
}
