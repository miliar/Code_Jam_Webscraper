#include<iostream>
#include<limits>
using namespace std; 

typedef unsigned long long int u64;

int main(){
	int _ncases; cin>>_ncases;
	const int ncases=_ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		cerr<<"Doing case: "<<ncase<<endl;
		int R,K,N; cin>>R>>K>>N;
		int G[N];
		for (int i=0;i<N;++i)cin>>G[i];
		u64 A[N]; 
		int B[N];
		for (int i=0;i<N;++i){
			A[i]=0; int p=0;
			for (int j=0;j<N;++j){
				int k=(i+j)%N;
				if (A[i]+G[k]<=K)A[i]+=G[k],++p;
				else break;
			}
			B[i]=(i+p)%N;
		}
		u64 t=0;
		int s=0;
		for (int i=0;i<R;++i){
			t+=A[s]; s=B[s];	
		}
		cout<<"Case #"<<ncase<<": "<<t<<endl;
	}
 	return 0;
}

