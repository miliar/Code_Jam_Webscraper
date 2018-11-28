#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

#define LL long long
#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

int N;
LL L,H;
vector<LL> freq;

LL gcd(LL a,LL b){return (b==0?a:gcd(b,a%b));}
LL lcm(LL a,LL b){return a/gcd(a,b)*b;}

bool check(LL a,LL b){
	LL c = max(a,b);
	return c==lcm(a,b);
}

LL small(){
	int res = -1;
	for(LL i=L ; i<=H ; i++){
		bool can = true;
		REP(j,N){
			if(!check(i,freq[j])){
				can = false;
				break;
			}
		}
		if(can){
			res = i;
			break;
		}
	}
	return res;
}

int main(){
	int T;cin>>T;
	REP(tt,T){
		cin>>N>>L>>H;
		freq.resize(N);
		REP(i,N)cin>>freq[i];

		LL res = small();

		printf("Case #%d: ",tt+1);
		if(res==-1){
			printf("NO\n");
		}
		else{
			printf("%lld\n",res);
		}
	}
	return 0;
}
