#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
vector<int> v;
int P,K,L,f;

long long sol()
{
	long long ret=0;
	sort(v.begin() , v.end());
	reverse(v.begin() , v.end());
	int i=0,k=1,j;
	while(i < v.size())
	{
		for(j=i ; j<i+K && j<v.size() ; j++)
			ret+=v[j]*k;
		k++;
		i=j;	
	}
	return ret;	
}

main()
{
	int test_case;
	scanf("%d",&test_case);
	for(int i=0;i<test_case;i++)
	{
		scanf("%d %d %d",&P,&K,&L);
		v.clear();
		for(int j=0;j<L;j++)
		{
			cin>>f;
			v.push_back(f);
		}
		if(P*K < L)
			cout<<"Case #"<<i+1<<": impossible"<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<sol()<<endl;		
	}
}
