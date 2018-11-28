#include <iostream>
#include <vector>
using namespace std;
int fuck(string t, string check, vector<string> dic)
{
	if(dic.size()==1)
		return 0;
	int hap=false;
	int incheck=false;
	for(int i=0; i<(int)check.size(); i++)
		if(check[i]==t[0])
			incheck=true;
	for(int i=0; i<(int)dic.size(); i++)
	{
		for(int j=0; j<(int)dic[i].size(); j++){
			if(t[0]==dic[i][j])
				hap=true;
		}
	}
	if(!hap)
		return fuck(t.substr(1, t.size()), check, dic)+0;
	int del[100];
	memset(del, 0, sizeof del);
	for(int i=0; i<(int)check.size(); i++){
		if(check[i]==t[0]){
			//vector<string> now;
			for(int j=0; j<(int)dic.size(); j++){
				if(dic[j][i]!=check[i])
					del[j]=true;
					//now.push_back(dic[j]);
			}
			//dic=now;
		}
	}
	for(int i=0; i<(int)dic.size(); i++){
		for(int j=0; j<(int)dic[i].size(); j++){
			if(dic[i][j]==t[0]&&check[j]!=t[0]){
				del[i]=true;
			}
		}
	}
	vector<string> now;
	for(int i=0; i<(int)dic.size(); i++){
		if(!del[i])
			now.push_back(dic[i]);
	}
	dic=now;
	if(incheck)
		return fuck(t.substr(1, t.size()), check, dic)+0;
	else
		return fuck(t.substr(1, t.size()), check, dic)+1;
}
void doo()
{
	int ncase,n;
	cin >> n >> ncase;
	vector<string> dic;
	dic.clear();
	for(int i=0; i<n; i++){
		string t;
		cin>> t;
		dic.push_back(t);
	}
	int maxn=-1;
	string ans;
	while(ncase--)
	{
		string str;
		cin >> str;
		maxn=-1;
		for(int i=0; i<(int)dic.size(); i++){
			vector<string> now;
			for(int j=0; j<(int)dic.size(); j++)
			{
				if(dic[i].size()==dic[j].size())
					now.push_back(dic[j]);
			}
			//cerr<<"fuck " <<str<<endl;
			int res=fuck(str, dic[i], now);
			//cerr<<res<<" " << dic[i]<<endl;
			if(maxn<res){
				maxn=res;
				ans=dic[i];
			}
		}
		cout<<" "<<ans;
	}
	cout<<endl;
}
int  main()
{
	long long  ncase=0;
	cin>>ncase;
	for(long long  i=0; i<ncase; i++)
	{
		cout<<"Case #"<<i+1<<":";
		doo();
	}
}
