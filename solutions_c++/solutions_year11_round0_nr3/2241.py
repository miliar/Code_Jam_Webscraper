#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <queue>
#include <iostream>
#include <algorithm>


using namespace std;

int main()
{
   freopen("in","r",stdin);
   freopen("out","w",stdout);
   long long int T,kas=0;
   cin>>T;
	while(T--)
	{
		vector<long long int> V; 
		long long int sum=0;
		long long int N,ans;
		cin>>N;
		for(int i=0;i<N;i++)
		{
			long long int X;
			cin>>X;
			if(!i) ans=X;
			else ans=ans^X;
			V.push_back(X);
			sum+=X;
		}
		
		printf("Case #%lld: ",++kas);
		if(!ans){
			sort(V.begin(),V.end());;
			cout<<sum-V[0]<<endl;
		}
		else cout<<"NO"<<endl;
	}
    
    
    
    
    
}

