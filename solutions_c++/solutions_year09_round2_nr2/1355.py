#include <iostream>
#include <string>
using namespace std;

struct tms{
	int t[9];
}ref;

tms profile(const long long &in);
bool eq(const tms &a, const tms &b);

int main(){
	int N;
	long long in;
	cin>>N;
	for(int n=0; n<N; n++){
		cin>>in;
	ref=profile(in);
	long long cmp=in+1;
	while(!eq(ref,profile(cmp)))
		cmp++;
	cout<<"Case #"<<n+1<<": "<<cmp<<'\n';
	}
	return 0;
}

tms profile(const long long &in){
	tms ret;
	long long tmp=in;
	for(int i=0; i!=9; ++i)
		ret.t[i]=0;
	while(tmp){
		if(tmp%10!=0)
			ret.t[tmp%10 -1]++;
		tmp-=tmp%10;
		tmp/=10;
	}
	return ret;
}

bool eq(const tms &a, const tms &b){
	for(int i=0; i<9; ++i)
		if(a.t[i]!=b.t[i])
			return 0;
	return 1;
}