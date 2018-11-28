#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;
#define LL __int64
#define MIN(a,b) (((a)<(b))?(a):(b))
LL D[10000];
LL L[10000];
int A[200][200];
int N;

int reachable(int current, int prev){
	int &sol=A[current][prev];
	if(sol!=-1){
		return sol;
	}
	if(current==(N+1)){
		return (sol=1);
	}
	LL len=MIN(D[current]-D[prev], L[current]);
	for(int i=current+1;i<=(N+1);++i){
		if(D[i]-D[current]<=len){
			int opc=reachable(i,current);
			if(opc){
				return (sol=1);
			}
		}
	}
	return (sol=0);

}
int main(int argc, char *argv[]){
	int T;
	cin>>T;
	for(int c=1;c<=T;++c){
		memset(A,-1,sizeof(A));
		cin>>N;
		D[0]=0;
		for(int i=1;i<=N;++i){
			cin>>D[i]>>L[i];
		}
		cin>>D[N+1];
		L[0]=D[1];
		int sol=reachable(1,0);
		if(sol){
			cout<<"Case #"<<c<<": YES"<<endl;
		}else{
			cout<<"Case #"<<c<<": NO"<<endl;
		}
		
	}

	return 0;
}

