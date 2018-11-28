
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{

int T;
cin>>T;
for(int i=0;i<T;i++)
{
	int N,S,p;
	cin>>N>>S>>p;
	vector<int> t(N);
	for(int j=0;j<N;j++)
		cin>>t[j];
	sort(t.begin(),t.end());
	int count=0;
	int ret=0;
	for(int j=0;j<N;j++)
	{
	
		
		if (t[j]==0 && p>0)
		continue;


		if ( (t[j]+1)/3 > p-1)
		{
			ret++;
		}
		else 	if ( (t[j]+1)/3 == p-1)
		{
			if (t[j]%3!=1)
			{
			if(count<S)
			{
			count++;
			ret++;
			}
			}
			else
			ret++;
		}
		
	
	}
	cout<<"Case #"<<i+1<<": "<<ret<<endl;



}

}
