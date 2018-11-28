#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for(int ti = 0;ti < t;ti++)
	{
		int N,K,T,B;
		scanf("%d%d%d%d",&N,&K,&B,&T);
		vector<int> V(N),X(N);
		vector<int> can;

		for(int i=0;i<N;i++)
			cin >> X[i];
		for(int i=0;i<N;i++)
			cin >> V[i];

		for(int i=V.size()-1;i>=0 && can.size() < K;i--)
			if((B - X[i]) <= T * V[i])
				can.push_back(V.size() - i - 1);

		if(can.size() < K)
		{
			cout << "Case #"<<ti+1<<": IMPOSSIBLE"<<endl;
			continue;
		}
		int res = 0;
		for(int i=0;i<can.size();i++)
		{
			res += can[i] - i;
		}
		cout << "Case #"<<ti+1<<": " << res << endl;



	}
	return 0;
}