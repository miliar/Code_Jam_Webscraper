#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("small3.txt");
	ofstream fout("out.txt");
	int T;
	fin>>T;
	for(int i=1;i<=T;++i)
	{
		int r,k,n,total=0;
		fin>>r>>k>>n;
		vector<int> vec(n);
		
		for(int j=0;j<n;j++)
		{
			int temp;
			fin>>vec[j];
		}
		int c = k;
		int ind = 0;
		for(int j=1;j<=r;++j)
		{
			for(int s=0;s<n && vec[ind]<=c;++s)
			{
				c -= vec[ind];
				total += vec[ind];
				++ind;
				if(ind==n)ind=0;
			}
			c=k;
		}
		fout<<"Case #"<<i<<": "<<total;
		if(i!=T)fout<<endl;
	}
	return 0;
}
