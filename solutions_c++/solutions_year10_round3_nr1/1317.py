#include<iostream>
#include<fstream>
using namespace std;
const int M=1005;
int ncase;
int N;
int data[M][2];
ifstream fin("A-large.in");
ofstream fout("out");
int main()
{
	fin>>ncase;
	int count=0;
	while(ncase--)
	{
		fin>>N;
		for(int i=0;i<N;++i)
		{
			fin>>data[i][0]>>data[i][1];
		}
		int ans=0;
		int t,temp;
		for(int i=0;i<N;++i)
		{
			for(int j=i+1;j<N;++j)
			{
				t=data[i][0]-data[j][0];
				temp=data[i][1]-data[j][1];
				if((t>0 && temp<0 )|| (t<0 && temp>0))
					++ans;
			}
		}
		fout<<"Case #"<<++count<<": "<<ans<<endl;
	}
	return 0;
}