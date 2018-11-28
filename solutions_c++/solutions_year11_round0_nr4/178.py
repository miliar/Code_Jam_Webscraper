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

int main()
{
	ifstream fin("E:\\Buid\\Algorithm\\GoogleJam\\2011Qualification\\D-large.in");
	ofstream fout("E:\\Buid\\Algorithm\\GoogleJam\\2011Qualification\\D-large.out");
	ofstream test("E:\\Buid\\Algorithm\\GoogleJam\\2011Qualification\\D-small-attempt3.test");
	int T,N;
	fin>>T;
	test<<T<<endl;
    int ans;

	REP(TEST,T)
	{
		ans = 0;
		fin>>N;
		test<<N<<endl;
		intvec que;

		test<<"Case #"<<TEST+1<<endl;

		REP(i,N)
		{
			int tem;
			fin>>tem;
			test<<tem<<" ";
			que.push_back(tem);
		}

		test<<endl;

		REP(i,N)
		{
			if(que[i]!=i+1)
			{
				ans+=1;
			}
		}
		fout<<"Case #"<<TEST+1<<": "<<ans<<".000000"<<endl;
	}


	system("pause");
	return 0;
}