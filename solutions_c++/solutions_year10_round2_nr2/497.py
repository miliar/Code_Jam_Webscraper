#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;
bool poss(long long x,long long v,long long time,long long dist)
{
	long long newD=x+v*time;
	if(newD>=dist)
		return 1;
	return 0;


}
int main()
{
	long long T1;
	cin>>T1;
	for(long long i1=1;i1<=T1;++i1)
	{
		long long N,K,B,T;
		cin>>N>>K>>B>>T;
		long long V[N],X[N],P[N];
		for(long long i=0;i<N;++i) cin>>X[i];
		for(long long i=0;i<N;++i) cin>>V[i];
		for(long long i=0;i<N;++i)
		{
			if(poss(X[i],V[i],T,B))
				P[i]=1;
			else
				P[i]=0;
		}
		long long mark=N-1;
		long long res=0,ans=0;
		for(long long i=mark;i>=0;--i)
		{
			if(P[i])
			{
				res++;
				continue;
			}
			mark=i;
			if(res>=K)
				break;
			long long pos=mark;
			while(pos>=0 && P[pos]!=1)
				pos--;
			if(pos<0) break;
			swap(P[pos],P[mark]);
			ans+=mark-pos;
			res+=1;
		}
		if(res>=K)
			cout<<"Case #"<<i1<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<i1<<": "<<"IMPOSSIBLE"<<"\n";
	}
}