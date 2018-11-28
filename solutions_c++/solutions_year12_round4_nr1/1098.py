#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	ifstream input("input.txt");
	ofstream ttout("ans.out");
	int t,n,d;
	int di[11000];
	int li[11000];
	int bi[11000];
	memset(di,0,sizeof(di));
	memset(li,0,sizeof(li));
	memset(bi,0,sizeof(bi));

	input>>t;
	for (int i=1;i<=t;++i)
	{
		input>>n;
		for(int j=1;j<=n;++j)
		{
			input>>di[j]>>li[j];
			bi[j]=0;
		}
		input>>d;
		bi[1]=di[1];
		bool isyes=false;
		for(int j=1;j<=n;++j)
		{
			if(di[j]+bi[j]>=d)
			{
				isyes=true;
				break;
			}
			for(int k=j+1;k<=n&&(di[k]-di[j])<=bi[j];++k)
			{
				bi[k]=max(bi[k],min(di[k]-di[j],li[k]));
			}
		}
		if(isyes)
			ttout<<"Case #"<<i<<": YES"<<endl;
		else
			ttout<<"Case #"<<i<<": NO"<<endl;
	}
	return 0;
}
