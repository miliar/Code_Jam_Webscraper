#include <iostream>
#include <algorithm>
#include <map>
#include <cstring>
#include <vector>

using namespace std;

int a[1002];
int b[1002];
int seen[1002];


int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int N;
		cin >> N;
		map<int,int> reMap;
		vector<int> cycle;
		memset(seen,0,sizeof(seen));
		for(int j=0;j<N;j++)
		{
			cin >> a[j];
			b[j] = a[j];
		}
		sort(a, a+N);
		for(int j=0;j<N;j++)
		{
			reMap[a[j]] = j;
		}
		for(int j=0;j<N;j++)
		{
			a[j] = reMap[b[j]];
		}
		for(int j=0;j<N;j++)
		{
			int cycleLen = 0;
			if(!seen[j])
			{
				int k = j;
				while(!seen[k])
				{
					cycleLen++;
					seen[k] = 1;
					k = a[k];
				}
			}
			if(cycleLen >= 2) cycle.push_back(cycleLen);
		}
		int ret = 0;
		for(int j=0;j<cycle.size();j++) ret += cycle[j];
		cout << "Case #" << i << ": " << ret << endl;
	}
}
