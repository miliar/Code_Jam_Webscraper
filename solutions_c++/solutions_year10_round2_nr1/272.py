#include <iostream>
#include <string>
#include <map>
using namespace std;
int N,M;

struct S {
	map<string,S> m;
} root;

void create(S& s, string ss)
{
	int a = ss.find_first_of('/');
	if (a!=(int)string::npos) {
		string x = ss.substr(0,a);
		string y = ss.substr(a+1,string::npos);
		create(s.m[x],y);
	} else {
		s.m[ss];
	}
}
int size(const S& s)
{
	int r=1;
	for(map<string,S>::const_iterator i=s.m.begin(); i!=s.m.end(); ++i) {
		r += size(i->second);
	}
	return r;
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		root.m.clear();
		cin>>N>>M;
		for(int i=0; i<N; ++i) {
			string s;
			cin>>s;
			create(root, s.substr(1,string::npos));
		}
		int s0 = size(root);
		for(int i=0; i<M; ++i) {
			string s;
			cin>>s;
			create(root, s.substr(1,string::npos));
		}
		cout<<"Case #"<<a<<": "<<size(root)-s0<<'\n';
	}
}
