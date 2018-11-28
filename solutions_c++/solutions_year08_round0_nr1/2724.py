#include<iostream>
#include<map>
#include<string>
#include<vector>

using namespace std;

int n,q;
int val[1001];
int dp[1001][101];

int cal(int pos,int pre){
	if(pos>=q){
		return 0;
	}
	int &ans=dp[pos][pre];
	if(ans!=-1)
		return ans;
	ans=1001;
	for(int i=0;i<n;i++){
		if(val[pos]==i)
			continue;
		if(i==pre)
			ans=min(ans,cal(pos+1,i));
		else
			ans=min(ans,1+cal(pos+1,i));
	}
	return ans;
}

int main(){
	int t;
	string s;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		memset(dp,-1,sizeof(dp));
		map<string,int> m;
		vector<string> v;
		cin>>n;
		getline(cin,s);
		for(int i=0;i<n;i++){
			getline(cin,s);
			v.push_back(s);
			m[s]=i;
		}
		cin>>q;
		getline(cin,s);
		int cnt=0;
		for(int i=0;i<q;i++){
			getline(cin,s);
			val[i]=m[s];
		}
		int ans=1001;
		for(int i=0;i<n;i++){
			if(val[0]!=i)
				ans=min(ans,cal(1,i));
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}
