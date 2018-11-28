#include <iostream>
using namespace std;
unsigned int T=0;
unsigned long R=0,k=0,N=0;

int main()
{
	unsigned long revenue;
	unsigned long count;
	cin>>T;
	for(unsigned int i=1;i<=T;i++)
	{
		revenue=0;
		cin>>R>>k>>N;
		unsigned long *g=new unsigned long[N];
		for(unsigned int n=0;n<N;n++) cin>>g[n];

		unsigned int n=0;
		unsigned int nstart;
		for(unsigned int r=0;r<R;r++)
		{
			nstart=n;
			count=0;
			while(count<k)
			{
				if(count+g[n]<=k)
				{
					count+=g[n];
					if(++n==N)n=0;
					if(n==nstart)break;
				}
				else
					break;
			}
			revenue+=count;
		}
		cout<<"Case #"<<i<<": "<<revenue<<endl;
		delete[] g;
	}
	return 0;
}
