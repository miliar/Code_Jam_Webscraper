
#include<iostream>

using namespace std;

int T,N,res;
int A[1000+2],B[1000+2];

bool isInts(int a, int b){
	if((A[a]>A[b] && B[a]<B[b]) || (A[a]<A[b] && B[a]>B[b])) return true;
	return false;
}

void count(int n){
	int i;

	for(i=0; i<n; i++){
		if(isInts(i, n)) res++;
	}
}

int main(){
	freopen("A-large.in","r", stdin);
	freopen("A-large.in.out", "w", stdout);

	int cas=0,i;
	cin>>T;

	while(cas++<T){
		cin>>N;
		res=0;

		for(i=0; i<N; i++){
			cin>>A[i]>>B[i];
			count(i);
		}
		cout<<"Case #"<<cas<<": "<<res<<endl;
	}
	return 0;
}