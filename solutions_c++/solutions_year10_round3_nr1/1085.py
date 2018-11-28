#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int tc=0;tc<T;tc++)
	{
//		cout<<"Case "<<tc<<endl;
		int N,M;
		cin>>N;
		
		int *A = new int[N];
		int *B  = new int[N];
		
		for (int i=0;i<N;i++)
		{
			cin>>A[i]>>B[i];
//			cout<<A[i]<<" "<<B[i]<<endl;
		}
		
		int ret = 0;
		for (int i=0;i<N;i++)		
		{
			for (int j=0;j<N;j++)
			{
				if (j!=i)
				{
					if ((A[i]>A[j] && B[i]<B[j]) || (A[i]<A[j] && B[i]>B[j]))
					{
//						cout<<A[i]<<","<<B[i]<<" and "<<A[j]<<","<<B[j]<<endl;
						ret++;
					}
				}
			}
		}
		
		cout<<"Case #"<<tc+1<<": "<<(ret/2)<<endl;
	}
	
}
