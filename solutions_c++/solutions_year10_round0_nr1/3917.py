#include <iostream>
#include <cstring>
#include <cmath>

#define inf 0x3f3f3f3f
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FILL(c) memset(c,0,sizeof(c));
using namespace std;

int main(){

	int N,K,T;
	cin>>T;
	FOR(t,T){
		cin>>N>>K;
		int c=(K+1)%(int)pow(2,(double)N);
		cout<<"Case #"<<(t+1)<<": "<<(c==0?"ON":"OFF")<<endl;
	}



}
