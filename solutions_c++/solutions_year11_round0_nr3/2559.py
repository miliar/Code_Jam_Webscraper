#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

#define X first
#define Y second
int casen=1;
#define caseout cout<<"Case #"<<casen++<<": "
typedef pair<int,int> pii;

void func(){
	int N,C;
	cin>>N;
	vector<int> Ci;
	for(int iN;iN<N;iN++){
		cin>>C;
		Ci.push_back(C);
	}
	// created list of Ci
	sort(Ci.begin(),Ci.end());

	// test it works
	int ans = Ci[0];
	for(int i=1;i<Ci.size();i++) ans^=Ci[i];
	if(ans != 0) caseout<<"NO"<<endl;
	else {
		int ret = 0;
		for(int i=1;i<Ci.size();i++) ret += Ci[i];
		caseout<<ret<<endl;
	}
}
int main(){
	int T;
	cin>>T;
	for(int iT=0;iT<T;iT++) func();
	return 0;
}
