#include<iostream>
#include<cstdio>
#include<sstream>
#include<cmath>
using namespace std;
int main(){
	int t; cin>>t;
	for (int ii = 1; ii <= t; ii++) {
		int a,b;
		cin>>a>>b;
		int count=0;
		for (int n = a; n < b; n++) {
			stringstream ss;
		//	cin>>n;
			ss<<n;
		string s; ss>>s;
		int len = s.size();
		s+=s;
		for(int i=len-1;i>0 ; i--){
			int m;
			//cout<<m<<endl;
			sscanf(s.substr(i,len).c_str(),"%d",&m);
			if(n>=a && n<m && n<b && m>n && m>a && m<=b){count++;}
		}
	}
		cout<<"Case #"<<ii<<": ";
		cout<<count<<endl;
	}
}
