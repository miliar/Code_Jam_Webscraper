#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
#define bit(n,i) ((n&(1<<i))!=0)
int memo[300][300];
ifstream fin("A-small-attempt0.in");
ofstream fout("output.out");
vector<int> v1,v2;
int recurse(int mv1,int mv2,int c)
{
	if(memo[mv1][mv2]!=-1000000000)
		return memo[mv1][mv2];
	if(mv1==0 || mv2==0)
		return 0;
	int ret=1000000000,i,j;
	for(i=0;i<c;++i)
	{
		if(bit(mv1,i))
		{
			for(j=0;j<c;++j)
			{
				if(bit(mv2,j))
				{
					ret=min(ret,v1[i]*v2[j]+recurse( mv1&(~(1<<i)),mv2&(~(1<<j)), c));
				}
			}
		}
	}
	memo[mv1][mv2]=ret;
	return memo[mv1][mv2];
}

int main()
{
	int n,i,j,k;
	fin>>n;
	
	for(i=0;i<n;++i)
	{
		int c;
		for(j=0;j<300;++j)
			for(k=0;k<300;++k)
				memo[j][k]=-1000000000;
		fin>>c;
		v1.clear();
		v2.clear();
		v1.resize(c);
		v2.resize(c);
		for(j=0;j<c;++j)
		{
			fin>>v1[j];
		}
		for(j=0;j<c;++j)
		{
			fin>>v2[j];
		}
		int ans=recurse( (1<<c) -1, (1<<c) -1,c);
		fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}