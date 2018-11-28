#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <map>
using namespace std;


int main()
{
	int C;
	ifstream file("B-large.in");
	ofstream out("output.txt");
	file>>C;
	for(int i=0;i<C;i++)
	{
		int N,K,B,T;
		file>>N>>K>>B>>T;
		vector<int> loc;
		vector<int> speed;
		for(int j=0;j<N;j++)
		{
			int t;
			file>>t;
			loc.push_back(t);
		}
		for(int j=0;j<N;j++)
		{
			int t;
			file>>t;
			speed.push_back(t);
		}
		//calculate the time
		vector<float> time(N);
		for(int j=0;j<N;j++)
		{
			time[j]=(float)(B-loc[j])/speed[j];
		}
		//count the number
		int sum=0;
		for(int j=0;j<N;j++)
		{
			if(time[j]<=T)
				sum++;
		}
		if(sum<K)
		{
			out<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			sum=0;
			int count=0;
			for(int j=N-1;j>=0;j--)
			{
				if(time[j]<=T)
				{
					sum++;
					for(int l=j+1;l<N;l++)
					{
						if(time[l]>T) count++;
					}
					if(sum==K) break;
				}
			}
			out<<"Case #"<<i+1<<": "<<count<<endl;
		}

	}
	return 1;
}
