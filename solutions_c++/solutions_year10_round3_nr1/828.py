#include <fstream>
using namespace std;
ifstream cin("A-large.in");
ofstream cout("A-large.out");
int T;
int N;
int A[1000], B[1000];

int main()
{
	cin>>T;
	for (int x=1; x<=T; x++)
	{
		cin>>N;
		int inter=0;
		for (int i=0; i<N; i++)
		{
			cin>>A[i]>>B[i];
		}
		
		for (int i=0; i<N-1; i++)
		{
			for (int j=i+1; j<N; j++)
			{
				if ( ((A[i]-A[j])*(B[i]-B[j])) < 0)
				{
					inter++;
				}
			}
		}
		cout<<"Case #"<<x<<": "<<inter<<endl;
	}
}
