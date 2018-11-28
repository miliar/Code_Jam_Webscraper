#include <iostream>
#include <math.h>
#include <string>
#include <set>
using namespace std;
#define MAX(a, b) (((a)<(b))?(b):(a))
#define LL long long
LL gcd(LL a, LL b){
	if(a<0){
		a=-a;
	}
	if(b<0){
		b=-b;
	}
	if(b==0){
		return a;
	}
	return gcd(b, a%b);
}
int N, L, H;
int A[10000];
void solve(int c){

	for(int x=L;x<=H;++x){
		bool ok=true;
		for(int j=0;j<N;++j){
			if(A[j]<x){
				if(x%A[j]!=0){
					ok=false;
					break;
				}
			}else{
				if(A[j]%x != 0){
					ok=false;
					break;
				}
			}
		}
		if(ok){
			cout<<"Case #"<<c<<": "<<x<<endl;
			return;
		}
	}
	cout<<"Case #"<<c<<": "<<"NO"<<endl;
}


int main(int argc, char *argv){
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		cin>>N>>L>>H;
		for(int i=0;i<N;++i){
			cin>>A[i];
		}
		solve(c+1);
	}
	return 0;
}
