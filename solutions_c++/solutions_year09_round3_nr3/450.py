#include<cstdio>
#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<map>
using namespace std;
int main()
{
	freopen("a.in","r",stdin) ;
	freopen("aout.txt","w",stdout) ;
	int T=0;
	scanf("%d",&T);
	for(int cs=1;cs<=T;++cs)
	{
		int P=0,Q=0;
		scanf("%d %d",&P,&Q);
		vector<int>as(Q);
		for(int i=0;i<Q;++i)
			scanf("%d",&as[i]);
		for(int i=0;i<as.size();++i)
			as[i]--;
		sort(as.begin(),as.end());
		
		int res=100000000;
		do{
			vector<int>pr(P,1);
			int cur=0;
			for(int j=0;j<as.size();++j)
			{
				pr[as[j]]=0;
				for(int k=as[j]-1;k>=0 && pr[k];k--)
					cur++;
				for(int k=as[j]+1;k<P && pr[k];k++)
					cur++;
			}
			res=min(res,cur);
		}while(next_permutation(as.begin(),as.end()));
		cout<<"Case #"<<cs<<": "<<res<<endl;
	}	
	return 0;
}