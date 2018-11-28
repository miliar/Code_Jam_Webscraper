#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	int T,t;
	fin>>T;
	for(t=1;t<=T;++t)
	{
		fout<<"Case #"<<t<<": ";
		int N;
		fin>>N;
		int i,j,k,ai,bi;
		vector<int> a,b;
		for(i=0;i<N;++i)
		{
			fin>>ai>>bi;
			a.push_back(ai);
			b.push_back(bi);
		}
		int count=0;
		for(j=0;j<N;++j)
		{
			for(k=j+1;k<N;++k)
			{
				if((a[k]<a[j] && b[k]>b[j]) || (a[k]>a[j] && b[k]<b[j]))
				{
					++count;
				}
			}
		}
		fout<<count<<endl;

	}
	return 0;
}
