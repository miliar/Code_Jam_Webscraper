#include<iostream>
#include<vector>
using namespace std;

void bubble(int A[],int n)
{
	int temp;
	
	int N=n;


  for (int i=0;i<N;i++)
  {
	  for(int j=N-1;j>=i+1;j--)
	  {
		  if (A[j-1] > A[j])
			{
			temp = A[j-1];
			A[j-1] = A[j];
			A[j] = temp;
		   
			}
	  }
  }
}

int main()
{
	int T;
	int N;
	int buf;

	int in1[800];
	int in2[800];

	cin>>T;

	for(int i=0;i<T;i++)
	{
		cin>>N;
		for(int j=0;j<2;j++)
			for(int k=0;k<N;k++)
			{
				cin>>buf;
				if(j)
					in2[k] = buf;
				else
					in1[k] = buf;
			}
			bubble(in2,N);
			bubble(in1,N);

			int prod = 0;
		for(int x=0;x<N;x++)
		{
			prod = prod + (in1[x]*in2[N-x-1]);
		}
		cout<<"Case #"<<i+1<<": "<<prod;
		if(i+1 != T)
			cout<<endl;

	}




	return 0;
}