#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;
bool match(const string& a,const string& b){
	if(a.size()!=b.size())return false;
	bool in[256]={0};
	for(int i=0;i<b.size();i++)in[b[i]]=1;
	for(int i=0;i<a.size();i++)
		if(b[i]!=' ' && a[i]!=b[i])
			return false;
		else if(b[i]==' ' && in[a[i]])
			return false;
	return true;
}
bool allIn(const string& s,bool* nin){
	for(int i=0;i<s.size();i++)
		if(nin[s[i]])return false;
	return true;
}
void filter(vector<string>& d,const string& g,bool *in,bool* nin){
	for(int i=0;i<d.size();){
		if(!match(d[i],g) || !allIn(d[i],nin))
			d.erase(d.begin()+i);
		else
			i++;
	}
	for(int i='a';i<='z';i++)in[i]=0;
	for(int i=0;i<d.size();i++)
		for(int j=0;j<d[i].size();j++)
			in[d[i][j]]=1;
}
int f(vector<string> d, string s,string tar){
	int ans=0;
	string g="";
	int len=tar.size();
	for(int i=0;i<len;i++)g+=" ";
	int idx=0;
	bool in[256],nin[256]={0};
	filter(d,g,in,nin);
	while(d.size()>1){
		while(!in[s[idx]])idx++;
		bool flag=false;
		for(int i=0;i<len;i++){
			if(tar[i]==s[idx]){
				g[i]=tar[i];
				flag=true;
			}
		}
		if(!flag){
			ans++;
			nin[s[idx]]=1;
		}
		filter(d,g,in,nin);
		idx++;
	}
	return ans;
}
int main(int argc, const char *argv[])
{
	int times;
	int N,M;
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		printf("Case #%d:",tm);
		cin>>N>>M;
		vector<string> dict;
		string s;
		for(int i=0;i<N;i++){
			cin>>s;
			dict.push_back(s);
		}
		for(int i=0;i<M;i++){
			cin>>s;
			int m=-1,ans=-1;
			for(int j=0;j<N;j++){
				int t=f(dict,s,dict[j]);
				if(t>m){
					m=t;
					ans=j;
				}
			}
			cout<<" "<<dict[ans];
		}
		cout<<endl;
	}
	return 0;
}
