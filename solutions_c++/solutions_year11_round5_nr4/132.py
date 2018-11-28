#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

template<typename T> T isqrt(T N){
	T res=0;
	for(int i=sizeof(T)*4-1; i>=0; i--){
		res^=(1<<i);
		if(res*res>N)
			res^=(1<<i);
	}
	return res;
}

template<typename T> bool issq(T N){ T root=isqrt(N); return N==root*root; }

void eval(){
	string s;
	cin>>s;
	long long qmask=0, num=0;
	for(int i=0; i<s.size(); i++){
		int pos=s.size()-1-i;
		if(s[i]=='?')
			qmask|=1ll<<pos;
		else if(s[i]=='1')
			num|=1ll<<pos;
	}
	bool found=0;
	long long res;
	for(long long m=qmask; m>0; m=(m-1)&qmask){
		if(issq(m|num)){
			res=m|num;
			found=true;
			break;
		}
	}
	if(!found){
		if(issq(num)){
			res=num;
			found=true;
		}
	}
	assert(found);
	for(int i=s.size()-1; i>=0; i--){
		putchar('0'+(((res)>>i)&1));
	}
	putchar('\n');
	cout<<flush;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
