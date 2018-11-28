#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int main()
{
	int t,k,n,r,cnt = 0;
	cin>>t;
	while(t--)
	{
		++cnt;
		cin>>r>>k>>n;
		long long sum = 0;
		queue <int> q;
		int temp;
		for(int i=0; i<n; ++i){cin>>temp;q.push(temp);}
		int this_round = 0;
		while(r)
		{
			queue <int> thisone;
			while(!q.empty() && this_round + q.front() <= k)
			{
				this_round += q.front();
				thisone.push(q.front());
				q.pop();
			}
			while(!thisone.empty())
				q.push(thisone.front()),thisone.pop();
			sum += this_round;
			this_round = 0;
			--r;
		}
		cout<<"Case #"<<cnt<<": "<<sum<<endl;
	}
	return 0;
}