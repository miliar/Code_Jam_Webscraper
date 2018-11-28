#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

bool G[101][11][2];

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int NCasos;
	cin>>NCasos;
	
	for(int caso=0; caso<NCasos; caso++)
	{
		int N, M;
		cin>>N>>M;
		
		memset(G, 0, sizeof(G));
		
		for(int i=0; i<M; i++)
		{
			int n;
			cin>>n;
			
			for(int j=0; j<n; j++)
			{
				int a, b;
				cin>>a>>b;
				G[i][a-1][b] = 1;
			}
		}
		
		int x = -1, minN = 1<<30;
		
		for(int mask=0; mask<(1<<N); mask++)
		{
			bool vale = true;
			for(int i=0; i<M; i++)
			{
				bool ok = false;
				for(int j=0; j<N; j++)
					if(G[i][j][(mask&(1<<j))!=0])
						ok = true;
				if(!ok) vale = false;
			}
			if(vale)
			{
				int tmp = __builtin_popcount(mask);
				if(tmp < minN)
				{
					minN = tmp;
					x = mask;
				}
			}
		}
		
		cout<<"Case #"<<caso+1<<":";
		if(x==-1) cout<<" IMPOSSIBLE"<<endl;
		else
		{
			for(int i=0; i<N; i++)
				cout<<" "<<((x&(1<<i))!=0);
			cout<<endl;
		}
	}
	return 0;
}
