#include<iostream>
#include<vector>
#include<string>

using namespace std;
#define oo 10000
vector<string> name;
vector<string> q;
int dp[101][1001];

int fun(int ind,int st){
	if(st >= (int)q.size())return 0;
	if(dp[ind][st]!= -1) return dp[ind][st];
	int r = oo;
	if(name[ind] != q[st]){
		r = min(r,fun(ind,st+1));
	}else{
		for(int i=0;i<(int)name.size();i++){
			if(i == ind) continue;
			r = min(r,fun(i,st)+1);
		}
	}
	return dp[ind][st] = r;
}

int main(){
	freopen("sample.in","rt",stdin);
	freopen("sample.out","w",stdout);
	
	int n = 0,s,Q;
	string str;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>s;
		getline(cin,str);
		for(int j=0;j<s;j++)
		{
			getline(cin,str);
			name.push_back(str);
		//	cout<<str<<endl;
		}
		cin>>Q;
		getline(cin,str);
		for(int j=0;j<Q;j++){
			getline(cin,str);
			q.push_back(str);
		}
		
		memset(dp,-1,sizeof(dp));
		int sol = oo;
		
		for(int j=0;j<name.size();j++){
			sol = min(sol,fun(j,0));
		}
		
		cout<<"Case #"<<(i+1)<<": "<<sol<<endl;
		//cout<<"---------------------"<<endl;
		q.clear();
		name.clear();
	}
	
	return 0;
}
