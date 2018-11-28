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
typedef long long int64;
typedef long long int32;
typedef vector<int> vi;
typedef vector<int32> vi32;

int main() {
	int T,N;
	int32 R, K;
	int64 money;
	int32 *gi;
	// for each run variables
	int32 cK; //current Kap
	int cG;   //current Group
	int iG;   //initial Group
	//-------------------
	cin>>T;
	for(int c=1;c<=T;c++){
		money=0;
		cG=0;
		cin>>R>>K>>N;
		gi= new int32[N];
		for(int i=0; i<N ; i++)
			cin>>gi[i];		
		for(int32 i=0; i<R; i++){
			cK=0;
			iG=cG;
			while((cK==0)||((cK+gi[cG]<=K)&&(cG!=iG))){
				cK+=gi[cG];
				cG++;
				if(cG==N) cG=0;
			}
			money+=cK;
		}
		delete [] gi;
		cout<<"Case #"<<c<<": "<<money<<endl;
	}
	return 0;
}