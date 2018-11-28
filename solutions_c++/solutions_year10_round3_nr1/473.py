#include<iostream>
#include<vector>
using namespace std;

main()
{
	int T,N;
	long long int count=0;

	cin >> T;

	for(int l=0;l<T;l++)
	{
		cin >> N;
		vector<int> A(N,0);
		vector<int> B(N,0);
		
		for(int i=0;i<N;i++) cin >> A[i]>>B[i];
		count=0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(i==j)continue;
				
				if((A[i] > A[j]) && (B[i] < B[j])) count++;
				if((A[j] > A[i]) && (B[j] < B[i])) count++;
			}
		}
		cout<<"Case #"<<l+1<<": "<< count/2<<'\n';
	}
				
}
