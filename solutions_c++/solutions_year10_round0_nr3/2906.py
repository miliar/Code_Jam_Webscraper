#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ofstream fout ("gig.out");
	ifstream fin ("C-small-attempt0.in");
	int T,R,k,N,P[1001];
	bool h[1001];
	fin>>T;
	for(int i=0;i<T;i++)
	{
		fin >>R;
		fin>>k;
		fin>>N;
		int a=0,pool=0;
		for(int j=0;j<N;j++)
			fin>>P[j];
		for(int j=0;j<R;j++)
		{
			int x=0;
			for(int k=0;k<N;k++)
				h[k]=true;
			while(x+P[a]<=k && h[a] )
			{
				x+=P[a];
				h[a]=false;
				if(a==N-1)
					a=0;
				else
					a++;
			}
			pool+=x;
		}
		fout<<"Case #"<<i+1<<": "<<pool<<endl;
	}
	return 0;
}