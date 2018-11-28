#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

ifstream fin("btc");
#define cin fin

void stuff()
{
	int i,j,N,M,L,C;
	long long t,gt=0;
	//int a[1001]={0};
	vector<int> a;
	vector<int> v;
	set<int> s;
	cin>>L>>t>>N>>C;
	for(i=0;i<C;i++)
	{
		cin>>j;	
		a.push_back(j);
	}
	for(;i<N;i++)
		a.push_back(a[i-C]);	
	gt=t;
	int index=0;
	long long sum=0;
	while(2*sum<=t && index<N)
	{
		sum+=a[index];
		index++;
	}
	if(index==N && 2*sum<=t)
	{
		cout<<sum*2;
		return;
	}
	index-=1;
	sum-=a[index];
	a[index]-=(t-sum*2)/2;
	sort(a.begin()+index,a.end());
	for(j=N-1; (N-1-j)<L && j>=index;j--)
	{
		gt+=a[j];
		
	}
	if(j==index-1)
	{
		cout<<gt;
		return;
	}
	for(;j>=index;j--)
		gt+=a[j]*2;
	cout<<gt;
	
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
