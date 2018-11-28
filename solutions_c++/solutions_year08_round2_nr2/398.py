#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int test,a,b,p;
int don[1005][1005];
int find_set(int x,int A[])
{
	if(x!=A[x])  A[x]=find_set(A[x],A);
	return A[x];
}

bool pr(int x)
{
	int k=(int)sqrt(x);
	k+=1;
	for(int i=2;i<=k;++i)
		if(x%i==0) return 0;
return 1;
}

int main()
{
	cin>>test;
	int count=0;
	vector<int> prime;
	prime.push_back(2);
	for(int i=3;i<1000;++i)
		if(pr(i))
			prime.push_back(i);	
			
	for(int i=1;i<=1000;++i)
		for(int k=i+1;k<=1000;++k)
		{
			for(int j=0;j<prime.size();++j)
				if((i%prime[j]==0) && (k%prime[j]==0))
					don[i][k]=prime[j];
		}
	
	for(int i1=1;i1<=test;++i1)
	{
		cin>>a>>b>>p;
		int A[b-a+2],count=b-a+1;
		for(int i=0;i<=b-a;++i)
			A[i]=i;
		bool mark=1;
		while(mark)
		{
			mark=0;
			for(int i=0;i<=b-a;++i)
				for(int k=i+1;k<=b-a;++k)
				{
					if(don[i+a][k+a]>=p)
					if(find_set(i,A)!=find_set(k,A))
					{
						A[find_set(i,A)]=find_set(k,A);
						mark=1;
						count-=1;
					}
				}
		}
		printf("Case #%i: %i\n",i1,count);
	}
}