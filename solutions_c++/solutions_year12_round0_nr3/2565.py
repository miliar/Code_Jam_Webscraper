#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin(); i!=(v).end(); ++i)
#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
using namespace std;

const int MAXN=2000000;
vector<int> conv[MAXN+1];

string str(int x) {
	ostringstream ss;
	ss<<x;
	return ss.str();
}

int num(const string s) {
	istringstream ss(s);
	int res;
	ss>>res;
	return res;
} 

void initConv() {
	for(int i=0; i<=MAXN; i++) {
		string s=str(i);
		for(int r=1; r<s.length(); r++) {
			int j=num(s.substr(r) + s.substr(0,r));
			if(j<=MAXN && j>i) conv[i].push_back(j);
		}
		sort(conv[i].begin(), conv[i].end());
		vector<int>::iterator fin = unique(conv[i].begin(),conv[i].end());
		conv[i].resize(fin-conv[i].begin());
	}
}

int solve(int A, int B) {
	int res=0;
	for(int i=A; i<=B; i++) {
		vector<int>::const_iterator iter = lower_bound(conv[i].begin(),conv[i].end(), A);
		for(;iter!=conv[i].end() && *iter<=B; ++iter, res++) ;
	}
	return res;

}


int main()
{
	initConv();
	cerr<<"inicia";
	int T;
	cin>>T;
	for(int caseid=1; caseid<=T; caseid++) {
		int A, B;
		cin>>A>>B;
		cout<<"Case #"<<caseid<<": "<<solve(A,B)<<endl;
	}
}
