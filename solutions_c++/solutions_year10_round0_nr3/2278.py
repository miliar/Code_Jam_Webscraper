#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>

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
		long long earning = 0;
		for(int j=0;j<R;j++)
		{
			int cap=0;
			for(int k=0;k<N;k++)
			{
				if((cap + que[0]) <= K)
				{
					cap += que[0];
					que.push_back(que[0]);
					que.erase(que.begin());
					continue;
				}	
				else break;
			}
			earning += cap;
		}

		cout << "Case #"<<i<<": "<<earning<<"\n";
	}
return 0;
}
