#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<string.h>
#include<algorithm>
#include<list>
#include<cmath>
using namespace std;
//int bas_dec(string s,int base){
long long func(int nn,int base){
	vector<int>v;
	long long ff=0;
	while(nn){
		v.push_back(nn%10);
		nn/=10;
	}
//	reverse(v.begin(),v.end());
	stringstream ss;
	for(int i=0;i<v.size();i++){
		ff+=v[i]*pow(base,i);

		
	}
	
//	ss>>f;
	return ff;
}


int main(){
	int t,k,i;
	cin>>t;
	string s;
	getline(cin,s);
	int cnt=1;
	while(t--){
		cin>>s;
		list<int>l;
		for(i=0;i<s.size();i++){
			l.push_back(s[i]);
		}
		l.sort();
		l.unique();
		int base=l.size();
		if(base==1)base=2;
		map<char,int>m;
		m[s[0]]=1;
		k=-1;
//		int m[37]={-1};
//		m[s[0]-48]=1;
//		if(m[s[1]]==0)
//			m[s[1]]=k;
//		else
//			m[s[1]]=m[s[0]];
	//	k=0;
	//	k=0;	
		for(i=1;i<s.size();i++){
			if(m[s[i]]==0){
//				cout<<i<<" "<<k<<"\n";
				if(k==1 || k==0)k++;
				if(k==1)k++;
				m[s[i]]=k;
				k++;

				
			//	if(k==1)k++;
			}
		}
	//	cout<<m['0']<<"\n";
//		map<char,int>::iterator it=m.begin();
//		while(it!=m.end()){
//			cout<<(*it).first<<" "<<(*it).second;
//			it++;
//		}
//		cout<<"\n";	
		string s1;
		stringstream ss;
		for(i=0;i<s.size();i++){
			if(m[s[i]]!=-1)
				ss<<m[s[i]];
			else
				ss<<0;
		}
		ss>>s1;
/*		if(s1[0]=='0'){
			j=0;
			while(s1[j]=='0')j++;
			char temp=s1[j];*/
	//	cout<<s1<<"\n";
		stringstream ss1;
		ss1<<s1;
		long long nn,k_k;
		ss1>>nn;
		k_k=func(nn,base);
		cout<<"Case #"<<cnt<<": "<<k_k<<"\n";
		cnt++;

	}
}
			
			

		



