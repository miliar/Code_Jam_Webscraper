#include<iostream>
#include<set>
#include<string>

using namespace std;

int main(){
	int n;
	cin>>n;
	string str;
	getline(cin,str);
	for(int t=1;t<=n;t++){
		int s,q,m=0,r=0;
		set<string> w;
		cin>>s;
		for(int i=0;i<=s;i++)
			getline(cin,str);
		cin>>q;
		getline(cin,str);
		for(int i=0;i<q;i++){
			getline(cin,str);
			if(w.find(str)==w.end()){
				if(++m==s){
					r++;
					m=1;
					w.clear();
				}
				w.insert(str);
			}
		}
		cout<<"Case #"<<t<<": "<<r<<endl;
	}
	return 0;
}