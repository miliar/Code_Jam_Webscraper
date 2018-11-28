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
//#define fin cin
//#define fout cout
////////////////////////

int main()
{
	ifstream fin("E:\\Buid\\Algorithm\\GoogleJam\\2011Qualification\\C-large.in");
	ofstream fout("E:\\Buid\\Algorithm\\GoogleJam\\2011Qualification\\C-large.out");
	int T;
	int N;
	
	fin>>T;
	REP(TEST,T)
	{
		int ans = 0;
		int right;
		int min;
		fin>>N;
		REP(i,N)
		{
			int tem;
			fin>>tem;
			if(i == 0)
			{
				right = tem;
				ans =  tem;
				min = tem;
			}
			else
			{
				ans+=tem;
				right^=tem;
				min = min<tem?min:tem;
			}
		}
		if(right == 0)
			fout<<"Case #"<<TEST+1<<": "<<ans-min<<endl;
		else
			fout<<"Case #"<<TEST+1<<": "<<"NO"<<endl;
	}
	
	system("pause");
	return 0;
}