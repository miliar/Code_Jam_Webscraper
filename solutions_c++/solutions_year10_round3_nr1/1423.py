#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef long long int64;
typedef long long int32;
typedef vector<int> vi;
typedef vector<int32> vi32;

int main() {
	int T,N;
	int64 inter;
	int32 *ai;
	int32 *bi;
	cin>>T;
	for(int c=1;c<=T;c++){
		inter=0;		
		cin>>N;
		ai= new int32[N];
		bi= new int32[N];		
		for(int i=0; i<N ; i++)
			cin>>ai[i]>>bi[i];
		for(int i=0; i<N ; i++){
			for(int j=i+1; j<N; j++){
				if(((bi[i]>bi[j])&&(ai[i]<ai[j]))||((bi[i]<bi[j])&&(ai[i]>ai[j])))
					inter++;
			}
		}	
		delete [] ai;
		delete [] bi;
		cout<<"Case #"<<c<<": "<<inter<<endl;
	}
	return 0;
}