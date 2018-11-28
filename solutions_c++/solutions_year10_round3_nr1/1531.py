#include <iostream.h>
#include <fstream.h>
//using namespace std;
int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");


	int t;
	int result;
	int n;
	int i,j;
	int A[10005];
	int B[10005];
	cin>>t;
	for(i=0;i<t;i++)
	{
		result=0;
		cin>>n;
		for(j=0;j<n;j++)
		{
			cin>>A[j];
			cin>>B[j];
			if(j>0)
			{
				if((A[j]-A[j-1])*(B[j]-B[j-1])<0)
				{
					result++;

				}

			}
		}
		cout<<"Case #"<<i+1<<": "<<result<<endl;

	}
	return 0;
}