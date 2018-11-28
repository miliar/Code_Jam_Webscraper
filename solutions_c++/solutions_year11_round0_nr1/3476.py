#include <iostream>
#include <vector>
#include <cstdlib>
#include <cassert>

using namespace std;

void process()
{
	int num_buttons,tot_time=0;
	cin>>num_buttons;
	vector<char> BColor(num_buttons);
	vector<int> BVal(num_buttons);
	vector<int> BB;
	vector<int> BO;
	for(int i=0;i<num_buttons;++i)
	{
		char x;int v;
		cin>>x>>v;
		BColor[i] = x; BVal[i] = v;
		if(x=='O') BO.push_back(v);
		else BB.push_back(v);
	}
	int currO=1,currB=1, currBidx=0, currOidx=0;
	for(int i=0;i<num_buttons;++i)
	{
		if(BColor[i]=='O')
		{
			int secs_req = abs(BVal[i]-currO)+1;
			tot_time += secs_req;
			currO = BVal[i];
			assert(BVal[i]==BO[currOidx]);
			currOidx++;
			if(currBidx < BB.size())
			{
				if(currB > BB[currBidx])
				{
					int diff = currB - BB[currBidx];
					if (diff < secs_req)
						currB = BB[currBidx];
					else
						currB -= secs_req;
				}
				else if (currB < BB[currBidx])
				{
					int diff = BB[currBidx] - currB;
					if (diff < secs_req)
						currB = BB[currBidx];
					else
						currB += secs_req;
				}
			}
		}
		else
		{
			int secs_req = abs(BVal[i]-currB)+1;
			tot_time += secs_req;
			currB = BVal[i];
			assert(BVal[i]==BB[currBidx]);
			currBidx++;
			if(currOidx<BO.size())
			{
				if(currO > BO[currOidx])
				{
					int diff = currO - BO[currOidx];
					if (diff < secs_req)
						currO = BO[currOidx];
					else
						currO -= secs_req;
				}
				else if ( currO < BO[currOidx] )
				{
					int diff = BO[currOidx] - currO;
					if (diff < secs_req)
						currO = BO[currOidx];
					else
						currO += secs_req;
				}
			}
		}
	}

	cout<<tot_time<<endl;
}

int main()
{
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;++i)
	{
		cout<<"Case #"<<i<<": ";
		process();
	}
	return 0;
}
