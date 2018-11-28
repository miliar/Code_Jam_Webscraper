#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<sstream>
using namespace std;
int solve(int S,int P,vector<int> ts){
	int result=0;
	int pass=3*P-2;
	int pass1=P;
	int pass2=P-1;
	int pass3=P-1;
	if(pass2<0) pass2=0;
	if(pass3<0) pass3=0;
	pass=pass1+pass2+pass3;
	bool sup=true;	
	int surprise=3*P-4;
	int surprise1=P;
	int surprise2=P-2;
	int surprise3=P-2;
	surprise=surprise1+surprise2+surprise3;	
	if(P<2) sup=false;
	for(int i=0;i!=ts.size();++i){
		int value=ts[i];
		if(value>=pass) result++;
		else if(value>=surprise && S>0 && sup){
			S--;
			result++;
		}
	}
	return result;
}
int main(){
	int T;
	cin>>T;
	string dumb;
	getline(cin,dumb);
	for(int i=0;i<T;++i){
		string line;
		getline(cin,line);
		stringstream ss(line);
		int N,S,P;
		vector<int> value;
		ss>>N>>S>>P;
		for(int j=0;j<N;++j){
			int n;
			ss>>n;
			value.push_back(n);
		}
		int ret=solve(S,P,value);
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
}
