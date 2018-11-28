#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int main()
{
	int num_cases,N;
	cin>>num_cases;
	long long n,x0,y0,A,B,C,D,M;

	for(int i=0;i<num_cases;i++)
	{
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		int count=0;
		vector<long long> X;
		vector<long long> Y;
		X.push_back(x0);
		Y.push_back(y0);
		for(int j=1;j<n;j++)
		{
			x0 =( ((A*x0)% M) +(B%M))%M;
			y0 =( ((C*y0)% M) +(D%M))%M;
			X.push_back(x0);
			Y.push_back(y0);
		}
		for(int j=0;j<n;j++)
		{
			for(int k=j+1;k<n;k++)
			{
				for(int p=k+1;p<n;p++)
				{
					if((((X[j]%3)+(X[k]%3)+(X[p]%3))%3==0) &&(((Y[j]%3)+(Y[k]%3)+(Y[p]%3))%3==0))
					{
						count++;
					}
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<'\n';	
	}
	return(0);
}

		

			


	
