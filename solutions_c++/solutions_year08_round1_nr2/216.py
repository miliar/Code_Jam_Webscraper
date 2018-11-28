#include <cstdlib>
#include <iostream>
#include<vector>
#include<algorithm>

using namespace std;

int c1(int bt){
	int all=0;
	for(int i=0;i<16;i++){
		if(bt & (1<<i))all++;
	}
	
	return all;
}

bool ok(int bt,vector< pair<int,int> > mt[],int m){
	for(int i=0;i<m;i++){
		bool sat=0;
		for(int j=0;j<mt[i].size();j++){
			int fla=mt[i][j].first;
			int val=mt[i][j].second;
			
			if(bool(bt & (1<<fla))==val)
			    sat=1;
		}
		if(sat==0)return 0;
	}
	return 1;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	
	int C;
	cin>>C;
	for(int cc=1;cc<=C;cc++){
		int n;
		cin>>n;
		int m;
		cin>>m;
		
		vector< pair<int,int> > mt[128];
		
		for(int i=0;i<m;i++){
			int t;
			cin>>t;
			for(int j=0;j<t;j++){
				int like,malt;
				cin>>like>>malt;
				mt[i].push_back(make_pair(like-1,malt));
			}
		}
		
		int ans=10000000;
		int sta;
		
		for(int bt=0;bt<(1<<n);bt++){
			if(ok(bt,mt,m) && c1(bt)<ans){
				ans=c1(bt);
				sta=bt;
			}
		}
		
		cout<<"Case #"<<cc<<":";
		if(ans>10000)cout<<" IMPOSSIBLE\n";
		else {
			for(int i=0;i<n;i++){
				cout<<" ";
				if(sta&(1<<i))cout<<1;
				else cout<<0;
			}
			cout<<endl;
		}
	}
	
    //system("PAUSE");
    //return EXIT_SUCCESS;
    return 0;
}
