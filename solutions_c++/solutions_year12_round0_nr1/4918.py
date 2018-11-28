#include<iostream>
#include<sstream>
#include<cstdio>
#include<vector>
using namespace std;

string proc(string s){

	char p[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	for(int i=0;i<s.size();i++){
		s[i]=p[int(s[i])-97];
	}
	return s;
}

int main(){



	int t;
	int count=0;
	//stringstream ss;
	string s;
	scanf("%d",&t);
	getline(cin,s);
	while(t--){
		cout<<"Case #"<<(++count)<<": ";
		stringstream ss;
		vector<string>v;
		getline(cin,s);
		//cout<<s<<endl;
		ss<<s;
		while(ss>>s){
			v.push_back(s);
			//cout<<s<<endl;
		}

		for(int i=0;i<v.size()-1;i++){
			cout<<proc(v[i])<<" ";
		}
		cout<<proc(v[v.size()-1])<<endl;

	}
	return 0;
}
