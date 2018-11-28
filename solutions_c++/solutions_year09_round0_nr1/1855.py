#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream ci("in");
ofstream co("out");

string t[5000];

int main()
{
	int L,D,N,ans,c;
	char ch;
	int a[16];
	ci>>L>>D>>N;
	for (int i=0;i<D;++i)
	{
		ci>>t[i];
	}
	for (int i=0;i<N;++i)
	{
		ans=0;
		int k=0;
		for (;k<L;++k)
		{
			a[k]=0;
			ci>>ch;
			if (ch=='(')
			{
				ci>>ch;
				while (ch!=')')
				{
					a[k]=a[k]+(1<<(int(ch)-96));
					ci>>ch;
				}
			}
			else
			{
				a[k]=1<<(int(ch)-96);
			}
		}
		for (int j=0;j<D;++j)
		{
			c=0;
			for (int y=0;y<L;++y)
			{
				if (((1<<(int(t[j][y])-96))&a[y])==0)
					++c;
			}
			if (c==0)
				++ans;
		}
		co<<"Case #"<<i+1<<": "<<ans<<endl;
	}
};