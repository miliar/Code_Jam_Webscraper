#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<set>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;
typedef long long LL;
LL R,K,N;
vector<LL> A,P,S;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		scanf("%lld%lld%lld",&R,&K,&N);
		A.resize(N);
		P.clear();
		S.resize(N);
		for(int j=0;j<N;j++)
		{
			scanf("%lld",&A[j]);
		}
		vector<bool> done(N,false);
		LL index=0;
		LL sum=0;
		LL start=0;
		LL period=0;
		while(true)
		{
			LL Count=1;
			S[index]=P.size();
			sum=A[index];
			done[index]=true;
			index=(index+1)%N;
			while(Count<N && sum+A[index]<=K)
			{
				sum+=A[index%N];
				Count++;
				index=(index+1)%N;
			}
			P.push_back(sum);
			if(done[index])
				break;
		}
		start=S[index];
		period=P.size()-start;
				
		/*cout<<start<<" "<<period<<endl;
		for(int j=0;j<P.size();j++)
			cout<<P[j]<<" ";
		cout<<endl;
		*/
		
		if(R<=P.size())
		{
			LL ans=0;
			for(int j=0;j<R;j++)
				ans+=P[j];
			printf("Case #%d: %lld\n",i,ans);
		}
		else
		{
			
			LL ans=0;
			LL cycle_cost=0;
			for(int j=0;j<start;j++)
				ans+=P[j];
			for(int j=start;j<P.size();j++)
				cycle_cost+=P[j];
			R-=start;
			ans+=cycle_cost*((LL)(R/period));
			for(int j=start;j<start+R%period;j++)
				ans+=P[j];
			printf("Case #%d: %lld\n",i,ans);
		}
	}
	return 0;
}