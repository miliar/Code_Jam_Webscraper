#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cassert>
#include <algorithm>
typedef long long LL;

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;++i)
	{
		int N,tmpi;
		cin >> N;
		vector<pair<int,char> > v;
		char tmpc;
		for(int j=0;j<N;++j)
		{
			cin >> tmpc >> tmpi;
			v.push_back(make_pair(tmpi,tmpc));
		}
		int lastBPos=1,lastBTime=0,lastOPos=1,lastOTime=0,actTime=0;
		for(int j=0;j<N;++j)
		{
			if(v[j].second=='O')
			{
				int moveTime = abs(v[j].first-lastOPos);
				actTime+=max(moveTime+lastOTime-actTime,0);
				++actTime;
				lastOPos=v[j].first;
				lastOTime=actTime;
			}
			if(v[j].second=='B')
			{
				int moveTime = abs(v[j].first-lastBPos);
				actTime+=max(moveTime+lastBTime-actTime,0);
				++actTime;
				lastBPos=v[j].first;
				lastBTime=actTime;
			}
		}
		cout << "Case #" << i << ": "<< actTime << endl;
	}
	return 0;
}
