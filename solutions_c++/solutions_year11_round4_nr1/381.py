#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cassert>
#include <cmath>
#include <algorithm>
typedef long long LL; 
using namespace std;
 
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)

int main()
{
	int testCaseCounter;
	cin >> testCaseCounter;
	cout.precision(9);
	for(int actTestCase=1;actTestCase<=testCaseCounter;++actTestCase)
	{
		int X,S,R,t,N;
		cin >> X >> S >> R >> t >> N;
		map<int,double> m;
		int suml=0;
		REP(i,N)
		{
			int B,E,W;
			cin >> B >> E >> W;
			m[W]+=E-B;
			suml+=E-B;
		}
		m[0]+=X-suml;
		double tt=0,rt=t;
		for(map<int,double>::iterator it=m.begin();it!=m.end();++it)
		{
			if(rt>0)
			{
				double runtime=it->second/(R+it->first);
				if(runtime<=rt)
				{
					rt-=runtime;
					tt+=runtime;
					it->second=0;
				}
				else
				{
					tt+=rt;
					it->second-=(rt*(R+it->first));
					rt=0;
				}
			}
			if(it->second>0)
			{
				double walkt=it->second/(S+it->first);
				tt+=walkt;
				it->second=0;
			}
		}
		cout << "Case #" << actTestCase << ": "<< tt << endl;
	}
	return 0;
}
