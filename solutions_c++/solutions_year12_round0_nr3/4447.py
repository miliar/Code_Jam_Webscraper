//#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<map>
using namespace std;

ifstream cin("in");
ofstream cout("out");

int recycle(int n,int d){
	string s;
	stringstream ss1;
	ss1<<n; s=ss1.str();
	int l=s.length();
	string s1,s2;
	s1=s.substr(0,l-d);
	s2=s.substr(l-d,l-1);
	s.clear();
	s=s2+s1;
	stringstream ss2(s);
	int result;
	return ss2>>result ? result:0;
}

int dig(int n){
	string s;
	stringstream ss;
	ss<<n; s=ss.str();
	return s.length();
}

int main(){
	map<pair<int,int>,int> mp;
	int T;
	cin>>T;
	for(int k=0;k<T;k++){
		mp.clear();
		int A,B,n,m,sm=0,d;
		cin>>A>>B;
		d=dig(A);
		for(n=A;n<=B;n++){
			for(int i=1;i<=d;i++){
				m=recycle(n,i);
				if(n<m && m<=B && mp[make_pair(n,m)]==0 && mp[make_pair(m,n)]==0){
					sm++;
					mp[make_pair(n,m)]=1;
				}
			}
		}
		cout<<"Case #"<<k+1<<": "<<sm<<endl;
	}
}