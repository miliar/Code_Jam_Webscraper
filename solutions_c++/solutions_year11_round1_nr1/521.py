#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<list>
#include<stdio.h>
#include<sstream>
#include<set>
#include<deque>
#include<cmath>
#include<numeric>
#include<fstream>

using namespace std;

typedef long long LInt;
typedef vector<int> intvec;
typedef vector<intvec> intvec2;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define FOR(i,k,n) for (int i=(k); i<(int)(n); ++i)
#define DEC(i,k) for (int i=(k); i>=0; --i)
#define FORIT(i,c) for (decltype((c).begin())i=(c).begin();i!=(c).end();++i)

/////////////////////////
#define fin cin
#define fout cout
////////////////////////

int gcd(int m,int n)
{
	int rem;
	while(n>0)
	{
		rem = m%n;
		m = n;
		n = rem;
	}
	return m;
}

int main()
{
	ifstream fin("E:\\Buid\\Algorithm\\GoogleJam\\2011Round1A\\A-large.in");
	ofstream fout("E:\\Buid\\Algorithm\\GoogleJam\\2011Round1A\\A-large.out");
	
	int T;
	LInt N;
	string ans;
	int pd,pg;

	fin>>T;
	REP(TEST,T)
	{
		fin>>N>>pd>>pg;
		if(pg == 100 && pd!=100)
			ans = "Broken";
		else if(pg==0 && pd!=0)
			ans = "Broken";
		else
		{
			int x = 100/gcd(pd,100);
			if(x<=N)
				ans = "Possible";
			else
				ans = "Broken";
		}

	
		fout<<"Case #"<<TEST+1<<": "<<ans<<endl;
	}
	system("pause");
	return 0;
}