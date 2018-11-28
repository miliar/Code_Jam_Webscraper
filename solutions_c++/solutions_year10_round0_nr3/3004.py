#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

int main()
{
	int i,j,k,r,t,n,val,roller=0,x=0,y,len=0,cost=0;
	vector <int> queue,coaster;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>r>>k>>n;
		for(j=0;j<n;j++)
		{
			cin>>val;
			queue.push_back(val);
		}
		for(j=0,y=0;x<r;j++)
		{
			if(j < queue.size())
			{
			if(queue[j]<=(k-roller))
			{
				//cerr<<queue[j]<<endl;
				coaster.push_back(queue[j]);
				roller = roller+queue[j];
				cost=cost+queue[j];
				len++;
				//cerr<<coaster[y]<<endl;
			}
			else
			{
				x++;
				roller = 0;
				for(int xy=0;xy<len;xy++)
				{
					val = coaster[xy];
					queue.push_back(val);
				}
				coaster.clear();
				y=0;
				j--;
				len=0;
			}
			}
			else
			{
				x++;
				roller = 0;
				for(int xy=0;xy<len;xy++)
				{
					val = coaster[xy];
					queue.push_back(val);
				}
				coaster.clear();
				y=0;
				j--;
				len=0;
			}
		}
		cout<<"Case #"<<i+1<<": "<<cost<<endl;
		cost = 0;
		queue.clear();
		coaster.clear();
		roller = 0;
		y=0;
		len=0;
		x=0;
	}

}
