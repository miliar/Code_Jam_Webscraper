#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;
long long g[1001];
long long t[1001];
long long ind[1001];
vector<long long> order;
vector<long long> cumulative;

int main()
{
	int till;

	cin >> till;
	for(int Te=1 ; Te<=till ; Te++)
	{
		cout << "Case #"<<Te<<": ";
		long long r,k,n;
		cin >> r >> k >> n;
		

		for(int j=0 ; j<n ; j++)
			cin >>g[j];

		for(int j=0 ; j<n ; j++)
		{
			long long s = g[j] , c=(j+1)%n;
			while(c!=j && s+g[c]<=k)
			{
				s += g[c];
				c = (c+1)%n;
			}
			t[j] = s;
			ind[j] = c;
		}
		
		int done[1001];
		memset(done,-1,sizeof(done));

		//order.clear();
		cumulative.clear();

		long long s=0,money=0,c=0,temp=0;

		while(r && done[s]==-1)
		{
			//order.push_back(s);

			cumulative.push_back(temp+t[s]);
			money += t[s];
			done[s] = c++;
			temp = cumulative[cumulative.size()-1];

			s = ind[s];
			r--;
		}
		
		if(r)
		{
			long long rem = c - done[s];
			long long t = r/rem;
			
			long long val=0;
			val += cumulative[c-1];
			if(done[s] > 0)
				val -= cumulative[done[s]-1];
			val *= t;		

			long long rt = r - t*rem;
			money += val;
			if(rt)
			{
		    	val = cumulative[done[s]+rt-1];
				if(done[s])
					val -= cumulative[done[s]-1];
				money += val;
			}	
		}
		cout << money << endl;
	}
}
