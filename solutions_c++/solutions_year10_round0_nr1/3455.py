#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef long long int64;
typedef long long int32;

int main() {
	int T,N;
	int32 K,n2;
	cin>>T;
	for(int c=1;c<=T;c++){
		cin>>N>>K;
		n2=pow(2,N)-1;				
		cout<<"Case #"<<c<<": "<<((n2&K)==n2?"ON":"OFF")<<endl;
	}
	return 0;
}