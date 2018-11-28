#include<iostream>
#include<deque>
#include<vector>
using namespace std;

struct entry
{
	long long x;
	int pos;
};

int main()
{

	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{

		long long r,k,n;
		cin >> r >> k >> n;
		deque<entry> d;
		for(int i = 0; i < n;i++)
		{
			long long x;
			cin >> x;
			entry e;
			e.x = x;
			e.pos = i;
			d.push_back(e);
		}

		deque<entry> dq = d;

		vector<entry> v;
		long long euros = 0;
		long long period = r+1; //period is less than r so it doesnt matter
		long long mpp = 0;
		for(int i = 0; i < r;i++)
		{
			long long total = 0;
			if( i != 0 && d[0].pos == 0)
			{
				period = i;
				mpp = euros;
				break;
			}
			while(total <= k)
			{
				if(d.size() == 0)
					break;

				if(total + d[0].x > k)
					break;
				
				total += d[0].x;
				v.push_back(d[0]);
				d.pop_front();
			}
			for(int j = 0; j < v.size();j++)
				d.push_back(v[j]);

			
			euros += total;
			v.clear();
		}
		//cout << "period is " << period << endl;
		long long totalMoney = (r/period)*mpp;
		long long z = r % period;
		//cout << "z is " << z << endl;
		v.clear();
		for(int i = 0; i < z;i++)
		{
			long long total = 0;
			
			while(total <= k)
			{
				if(dq.size() == 0)
					break;

				if(total + dq[0].x > k)
					break;
				
				total += dq[0].x;
				v.push_back(dq[0]);
				dq.pop_front();
			}
			for(int j = 0; j < v.size();j++)
				dq.push_back(v[j]);

			
			totalMoney += total;
			v.clear();
		}


			
		cout << "Case #" << (t+1) << ": " << totalMoney << endl;


	} 


}
