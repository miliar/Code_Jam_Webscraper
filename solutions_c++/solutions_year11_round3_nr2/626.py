#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <ctype.h>
#include <bitset>
#include <cassert>

using namespace std;

typedef long long ll;

int tellForOne(int b1,int b2,vector<int> ai,ll t)
{
	bool boosterCompleted=false;
	int ans=0;
	for(int i=0;i<ai.size();i++)
	{
		if(ll(ans)>=t)
			boosterCompleted = true;
		
		// Case 1;
		if(boosterCompleted==true)
		{
			if(i==b1 || i==b2)
				ans += ai[i];
			else
				ans += ai[i]*2;
		}

		//Case 2:
		if(boosterCompleted==false)
		{
			if(ans+ai[i]*2<=t || (i!=b1 && i!=b2))
				ans += ai[i]*2;
			else
			{
				int distToBooster = (int(t)-ans)/2;
				ans +=  (int(t)-ans) + (ai[i]- (int(t)-ans)/2);
				boosterCompleted = true;
			}
		}
	}
	return ans;
}
int doForOne(int L,ll t, vector<int> ai)
{
	int min=-1;
	int b1=-1,b2=-1;
	int ans=0;
	switch(L)
	{
	case 0:
		ans=0;
		for(int i=0;i<ai.size();i++)
			ans += ai[i]*2;
		min = ans;
		return min;
		break;
	case 1:
		for(int i=0;i<ai.size();i++)
		{
			b1=-1;
			b2=i;
			int x =tellForOne(b1,b2,ai,t);
			if(min==-1 || x<min)
				min=x;
		}
		return min;
		break;
	case 2:
		for(int i=0;i<ai.size()-1;i++)
			for(int j=i+1;j<ai.size();j++)
			{
				b1=i;
				b2=j;
				int x =tellForOne(b1,b2,ai,t);
				if(min==-1 || x<min)
					min=x;
			}
		return min;
		break;
	}
	return min;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	
	int T;
	cin>>T;
	 
	for(int i=1;i<=T;i++)
	{
		int L,N,C;
		ll t;
		cin>>L>>t>>N>>C;
		vector<int> ai;

		for(int j=0;j<C;j++)
		{
			int temp;
			cin>>temp;
			ai.push_back(temp);
		}
		for(int j=C;j<N;j++)
			ai.push_back(ai[j%C]);
		
		assert(ai.size()==N);

		int val = doForOne(L,t,ai);
		printf("Case #%d: %d",i,val);
		if(i!=T)
			printf("\n");
	}
	return 0;
}
