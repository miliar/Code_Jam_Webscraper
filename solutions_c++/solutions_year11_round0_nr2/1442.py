// b.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"


#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#define N 27
using namespace std;
int main(){
	int T;
	int c,d,n;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	int i,j;
	string a;
	char t,tmp;
	int com[N][N];
	int o[N][N];
	int cas=1;
	vector<char> s;
	while(T--){
		s.clear();
		cin>>c;
		memset(com,0,sizeof(com));
		memset(o,0,sizeof(o));
		for(i=0;i<c;i++)
		{
			cin>>a;
			com[a[0]-'A'][a[1]-'A']=a[2];
			com[a[1]-'A'][a[0]-'A']=a[2];
		}
		cin>>d;
		for(i=0;i<d;i++){
			cin>>a;
			o[a[0]-'A'][a[1]-'A']=1;
			o[a[1]-'A'][a[0]-'A']=1;
		}
		cin>>n;
		for(i=0;i<n;i++){
			cin>>t;
			if(s.empty()){
				s.push_back(t);
				continue;
			}
			if(com[s.back()-'A'][t-'A']!=0)
			{
				tmp=s.back();
				s.pop_back();
				s.push_back(com[tmp-'A'][t-'A']);
			}
			else{
				s.push_back(t);
			}
			for(j=0;j<s.size()-1;j++){
				if(o[s[j]-'A'][s.back()-'A']==1)
				{
					s.clear();
					break;
				}
			}
		}
		cout<<"Case #"<<cas++<<": [";
		if(s.size()!=0){
		for(j=0;j<s.size()-1;j++)
			cout<<s[j]<<", ";
		cout<<s[j]<<"]"<<endl;
		}
		else{
			cout<<"]"<<endl;
		}
	}
	return 0;
}