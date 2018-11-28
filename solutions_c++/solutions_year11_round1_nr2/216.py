#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define vs vector<string>
#define vi vector<int>
#define pii pair<int,int>
#define vvi vector< vector<int> >
#define vpi vector< pair<int,int> >
#define LL long long

vs D;

void pm(vi& inds,string p,vector<bool>& b, vector<bool>& rev) {
	vi good;
	for(int i=0;i<inds.size();++i) {
		bool f = true;
		for(int j=0;f && j<p.length();++j) {
			if(b[D[inds[i]][j]-'a'] || (p[j]!='*' && p[j]!=D[inds[i]][j])) f = false;
			if(p[j]=='*' && rev[D[inds[i]][j]-'a']) f =false;
			}
		if(f) good.pb(inds[i]);
	}
	inds = good;
}

int score(string& w, string& L) {
	vi inds;
	for(int i=0;i<D.size();++i) if(D[i].length()==w.length()) inds.pb(i);
	int ret = 0;
	string p="";
	for(int i=0;i<w.length();++i) p+="*";
	vector<bool> banned(26,0);
	vector<bool> rev(26,0);
	for(int ii=0;ii<26;++ii) {
		bool o = false;
		for(int i=0;!o && i<inds.size();++i)
			for(int j=0;!o && j<D[inds[i]].length();++j)
				o = (D[inds[i]][j]==L[ii]);
		if (!o) continue;
		//cout<<" Patter is " << p << " for word " << w <<"\n";
		//cout<<"Candies:\n";
		//for(int i=0;i<inds.size();++i)
		//	cout<<D[inds[i]]<<"\n";
		//cout<<"\n";
		//cout<<"Trying..."<<L[ii]<<"\n";
		bool f = false;
		for(int j=0;j<w.length();++j) 
			if(w[j] == L[ii]) { f = true; p[j] = L[ii];}
		ret += !f;
		if(!f) banned[L[ii]-'a'] = true;
		else rev[L[ii]-'a'] = true;
		pm(inds,p,banned,rev);
		f = false;
		for(int i=0;i<p.length();++i) if(p[i]=='*') f = true;
		if (!f || inds.size()==1) break;
	}
	if(inds.size()!=1)
		cerr<<"Locha!\n";
	return ret;
}

int main() {
        int T; cin >> T;
        for(int iter1=0;iter1<T;iter1++) {
		int N,M;
		cin >> N >> M;
		D.resize(N); for(int i=0;i<N;++i) cin>>D[i];
		vs L(M); for(int i=0;i<M;++i) cin>>L[i];
		vector<string> best(M);
		for(int iter = 0; iter<M;++iter) {
			int bs = -1;
			for(int i=0;i<N;i++) {
				int sc = score(D[i],L[iter]);
				if (sc > bs) {
					bs = sc; best[iter] = D[i];
				}
			}
		}
		cout<<"Case #"<<(iter1+1)<<": ";
		for(int i=0;i<best.size();++i) 
		if (i+1==best.size())
			cout<<best[i]<<"\n";
		else
			cout<<best[i]<<" ";
	}
}

