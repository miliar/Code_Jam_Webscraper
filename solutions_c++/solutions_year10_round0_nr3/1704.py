#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
#include<map>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int R,K,N;
		cin >> R >> K >> N;
		vector<int> que;
		for(int j =0 ;j<N;j++)
		{
			int x;
			cin >> x;
			que.push_back(x);
		}
		long long cost[N];
		int index[N];
		for(int j =0;j<N;j++)
		{
			int x =j;
			long long y = 0;
			for(int k=0;k<N;k++)
			{
				if((y + que[x])<= K)
				{
					y += que[x];
					x ++;
					if(x == N)
						x = 0;
					continue;
				}
				break;
			}
			cost[j]=y;
			index[j] = x;
		}
		int next = 0;
		long long money = 0;
		for(int j = 0;j<R;j++)
		{
			money +=cost[next];
			next = index[next];
		}	
		cout << "Case #"<<i<<": "<<money<<"\n";
	}
return 0;
}
