#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
#include<cstdio>

using namespace std;
map<string,int>m;

void add(string s){
	string t="/";
	int k=1;
	while(k<s.size()){
		while(s[k]!='/' && k<s.size()){
			t+=s[k++];
		}
		//cout<<t<<endl;
		m[t]=1;
		t+=s[k];
		k++;
	}
}

int create(string s){
	int c=0;
	string t="/";
	int k=1;
	while(k<s.size()){
		while(s[k]!='/' && k<s.size()){
			t+=s[k++];
		}
		//cout<<t<<endl;
		if(m[t]!=1){
			c++;
			m[t]=1;
		}
		t+=s[k];
		k++;
	}
	return c;
}

int main(){
	string x;
	int n,k,t,c;
	cin>>t;
	for(int w=0;w<t;w++){
		cin>>n>>k;
		c=0;
		for(int i=0;i<n;i++){
			cin>>x;
			add(x);
		}
		for(int i=0;i<k;i++){
			cin>>x;
			c+=create(x);
		}
		cout<<"Case #"<<w+1<<": "<<c<<endl;
		m.clear();
	}
	return 0;
}
