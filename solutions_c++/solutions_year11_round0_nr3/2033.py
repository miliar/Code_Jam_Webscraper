#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int ntests;

int n;
vector<int> b;
string rseq;


int main()
{
	cin>>ntests;
	for(int ii=0;ii<ntests;ii++)
	{
		cin>>n;
		b.clear();
		for(int i=0;i<n;i++)
		{
			int val;
			cin>>val;
			b.push_back(val);
		}

		sort(b.begin(),b.end());
		int sum=0,x=0;
		for(int i=1;i<n;i++)sum+=b[i];
		for(int i=0;i<n;i++)x=x^b[i];
		
		cout<<"Case #"<<ii+1<<": ";
		if(x==0)cout<<sum<<endl;
		else cout<<"NO"<<endl;
		
	}
	return 0;
}