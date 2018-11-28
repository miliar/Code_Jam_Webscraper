#include<vector>
#include<iostream>
#include<map>
#include<queue>
#include<iterator>
#include<algorithm>
#include<iomanip>
#include<set>
#include<thread>
#include<mutex>
#include<condition_variable>
#include<iomanip>
#include<memory>
#include<utility>
#include<tuple>
using namespace std;
typedef vector<int> VI;
typedef vector<vector<int>> VII;typedef long long LL;
typedef long long LL;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		LL R, k, N;
		cin>>R>>k>>N;
		vector<LL> g(N);
		for(int i=0;i<N;i++) cin>>g[i];
		LL tot = accumulate(g.begin(),g.end(),0);
		LL total_sum=0;
		if(tot > k) 
		{
			int j = 0;
			LL sum = 0;
			for(int r=0;r<R;r++)
			{
				for(;;)
				{
					if(sum + g[j] > k)
					{
						total_sum += sum;
						sum = 0;
						break;
					}
					else
					{
						sum += g[j];
						j = (j+1)%N;
					}
				}
			}
		}
		else
		{
			total_sum = R*tot;
		}
		cout << "Case #"<<t<<": " << total_sum << endl;
	}
	
}

