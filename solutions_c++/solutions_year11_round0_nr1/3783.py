#include<iostream>
#define abs(x) (((x)>0)?(x):(-(x)))
#define max(x,y) (((x)>(y))?(x):(y))
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int j = 1 ; j<=t ; j++)
	{
		int n;
		cin>>n;
		int pos;
		char bot;
		int otime = 0, btime = 0;
		int opos = 1, bpos = 1;
		for(int i=0 ; i<n ; i++)
		{
			cin>>bot>>pos;
			if(bot == 'O')
			{
				otime += abs(pos - opos) + 1;
				opos = pos;
				if(otime <= btime) otime = btime + 1;
			}
			if(bot == 'B')
			{
				btime += abs(pos - bpos) + 1;
				bpos = pos;
				if(btime <= otime) btime = otime + 1;
			}
		}
		cout<<"Case #"<<j<<": "<<max(otime,btime)<<endl;
	}
	return 0;
}
			
			
