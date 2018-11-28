#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define REP(i,u) for(long long i=0;i<u;i++)
#define FOR(i,z,u) for(long long i=(z);i<=(u);i++)
#define FORO(i,z,u,p) for(long long i=(z);i<=(u);i=i+(p))
#define M 100
using namespace std;

int N,NA,NB,TOt,a,b,c,d,P[2],kto;
char ch;
vector<pair<pair<int,int> ,int> > spoj;
multiset<int> mam[2];

int main() 
{
	cin>>N;
	REP(p,N)
	{
		P[0]=P[1]=0;
		spoj.clear();
		mam[0].clear();
		mam[1].clear();
		cin>>TOt>>NA>>NB;
		REP(i,NA)
		{
			cin>>a>>ch>>b>>c>>ch>>d;
			spoj.push_back(make_pair(make_pair(a*60+b,c*60+d),0));
		}
		REP(i,NB)
		{
			cin>>a>>ch>>b>>c>>ch>>d;
			spoj.push_back(make_pair(make_pair(a*60+b,c*60+d),1));
		}
		sort(spoj.begin(),spoj.end());
		REP(i,spoj.size())
		{
			kto=spoj[i].second;
			if(mam[kto].size()==0)
				P[kto]++;
			else
				if(*mam[kto].begin()<=spoj[i].first.first)
					mam[kto].erase(mam[kto].begin());
				else 
					P[kto]++;
			mam[!kto].insert( spoj[i].first.second+TOt );
		}
		cout<<"Case #"<<p+1<<": "<<P[0]<<" "<<P[1]<<endl;
	}
	return 0;
}
