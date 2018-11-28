#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int num_cases,N;
	cin>>num_cases;
	for(int i=0;i<num_cases;i++)
	{
	cin>>N;
		vector<int> X(N,0);
		vector<int> Y(N,0);
		for(int j=0;j<N;j++)
		{
			cin>>X[j];
		}

		for(int j=0;j<N;j++)
		{
			cin>>Y[j];
		}
		sort(X.begin(),X.end());
		sort(Y.begin(),Y.end());
		int sol=0;
		for(int j=0;j<N;j++)
		{
			sol+=X[j]*Y[N-1-j];
		}
	cout<<"Case #"<<i+1<<": "<<sol<<'\n';
	}
	return(0);
}


