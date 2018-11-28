#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int t,test,n,i,j;
	cin>>t;
	int nn,kk;
	for(test=1;test<=t;test++){
		cin>>n;
		vector<pair<int,int> >wn;
	
		for(i=0;i<n;i++){
			cin>> nn>>kk;
			wn.push_back(pair<int,int>(nn,kk));
		}
	
		int cnt=0;
		sort(wn.begin(),wn.end());
	//	for(i=0;i<n;i++){
		//	cout<<wn[i].first<<" "<<wn[i].second<<"\n";
		//}	
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				
				if(wn[i].first<=wn[j].first && wn[i].second>=wn[j].second)cnt++;
			}
		}
		cout<<"Case #"<<test<<": "<<cnt<<"\n";
	}
}	
	