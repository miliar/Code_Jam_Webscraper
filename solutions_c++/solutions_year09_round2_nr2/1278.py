#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string tmp;
		cin>>tmp;
		cout<<"Case #"<<i+1<<": ";
		vector<int> A(tmp.size());
		for(int j=0;j<tmp.size();j++)
			A[j]=tmp[j];
		if(next_permutation(A.begin(),A.end()))
			for(int j=0;j<A.size();j++)
				cout<<A[j]-'0';
		else
		{
			while(A[0]=='0')
				next_permutation(A.begin(),A.end());
			cout<<A[0]-'0'<<0;
			for(int j=1;j<A.size();j++)
				cout<<A[j]-'0';
		}
		cout<<endl;
	}
	return 0;
}
