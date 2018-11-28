#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

ifstream fin("ctc");
#define cin fin

void stuff()
{
	long long i,j,N,M;
	vector<long long> v;
	set<int> s;
	long long L,H;
	long long cur,k;
	cin>>N>>L>>H;
	for(i=0;i<N;i++)
	{
		cin>>k;
		v.push_back(k);
	}	
	for(i=L;i<=H;i++)
	{
		for(j=0;j<N;j++)
			if(v[j]%i!=0 && i%v[j]!=0)
				break;
		if(j==N)
		{
			cout<<i;
			return;
		}
	}
	cout<<"NO";
}

int main(void)
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		stuff();
		cout<<endl;
	}
}
