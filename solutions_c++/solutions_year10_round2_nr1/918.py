#include <iostream>
#include <set>
#include <string>
using namespace std;

set<string> record;

int T,N,M;

void solve(int cases)
{
	int i,j,sum=0;
	string temp;
	cin>>N>>M;
	record.clear();
	for(i=1; i<=N; ++i)
	{
		cin>>temp;
		record.insert(temp);
		while(temp.size() > 0)
		{
			while(temp[temp.size()-1] != '/')temp.erase(temp.size()-1, 1);
			temp.erase(temp.size()-1, 1);
			record.insert(temp);
		}
	}

	for(j=1; j<=M; ++j)
	{
		cin>>temp;
		while(temp.size() > 0 && record.find(temp) == record.end())
		{
			record.insert(temp);
			++sum;
			while(temp[temp.size()-1] != '/')
				temp.erase(temp.size()-1, 1);
			temp.erase(temp.size()-1, 1);
		}
	}
	cout<<"Case #"<<cases<<": "<<sum<<endl;
}

int main()
{
	int i;
	cin>>T;
	for(i=1; i<=T; ++i)
	{
		solve(i);
	}
}