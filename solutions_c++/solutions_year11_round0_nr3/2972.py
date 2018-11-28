#include<iostream>
#include<vector>
#include<bitset>
#include<algorithm>
using namespace std;

int datain[1000];

bitset<30> add(bitset<30> a,bitset<30> b)
{
	bitset<30> data(0);
	for(int i=0;i<30;++i)
	{
		if(a[i]==b[i])
			data[i]=0;
		else
			data[i]=1;
	}
	return data;
}

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		int N;
		int sum=0;
		cin>>N;
		for(int j=0;j<N;++j)
		{
			cin>>datain[j];
			sum+=datain[j];
		}
		bitset<30> tmp(0);
		for(int j=0;j<N;++j)
		{
			bitset<30> tmpIn(datain[j]);
			tmp=add(tmp,tmpIn);
		}
		bool OK;
		if(tmp.to_ulong()==0)
			OK=true;
		else
			OK=false;
		if(OK)
		{
			sort(&datain[0],&datain[N]);
			printf("Case #%d: %d\n",i,sum-datain[0]);
		}
		else
		{
			printf("Case #%d: NO\n",i);
		}
	}
	return 0;
}