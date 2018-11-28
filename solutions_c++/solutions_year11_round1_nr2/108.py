#include <iostream>
#include <vector>
#include <map>
using namespace std;
int N,M;
string ss[1<<20];
string ls[1<<20];
typedef vector<int> ivec;
int Res=0;
int ri;
void solve(const ivec& v, const string s, int k, int C=0) {
//	cout<<"called solve: ";for(size_t i=0; i<v.size(); ++i) cout<<v[i]<<' ';cout<<'\n';
	if (v.size()==1) {
		if (C>Res || (C==Res && v[0]<ri)) Res=C, ri=v[0];
		return;
	}
	if (v.empty()) return;
	if (k==(int)s.size()) return;
	char c = s[k];
	map<ivec,ivec> M;
	for(size_t i=0; i<v.size(); ++i) {
		ivec z;
		for(size_t j=0; j<ss[v[i]].size(); ++j)
			if (ss[v[i]][j]==c) z.push_back(j);
		M[z].push_back(v[i]);
	}
	for(map<ivec,ivec>::iterator i=M.begin(); i!=M.end(); ++i) {
		int a = i->first.empty() && i->second.size()<v.size() ? 1 : 0;
//		cout<<"rec call: "<<i->second.size()<<' '<<a<<" ; "<<k<<' '<<C<<' '<<i->first.size()<<' '<<c<<'\n';
//		for(size_t j=0; j<i->second.size(); ++j) cout<<i->second[j]<<' ';cout<<'\n';
		solve(i->second, s, k+1, C+a);
	}
}
int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N>>M;
		for(int i=0; i<N; ++i) cin>>ss[i];
		map<int,ivec> mm;
		for(int i=0; i<N; ++i) mm[ss[i].size()].push_back(i);
		for(int i=0; i<M; ++i) cin>>ls[i];

		cout<<"Case #"<<a<<":";
		for(int j=0; j<M; ++j) {
			Res=-1;
			string o = ls[j];
			for(map<int,ivec>::iterator i=mm.begin(); i!=mm.end(); ++i) {
//				cout<<"iter: "<<i->first<<'\n';
				solve(i->second, o, 0);
//				cout<<"solve res "<<Res<<" ; "<<i->first<<' '<<i->second.size()<<'\n';
	//			cout<<r<<'\n';
	//			cout<<' '<<ss[best];
			}
			cout<<' '<<ss[ri];
		}
		cout<<'\n';
	}
}
