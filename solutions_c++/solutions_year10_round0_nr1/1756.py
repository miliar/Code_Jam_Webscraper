#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ofstream fout("output");
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int N,K;
		cin>>N>>K;
		K++;
		int count = 0;
		//cout<<K<<" ";
		while(K%2 == 0)
		{
			count++;
			K=K/2;
		}
		//cout<<count<<endl;
		string ans;
		if(N <= count)
			ans="ON";
		else
			ans="OFF";
		fout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
